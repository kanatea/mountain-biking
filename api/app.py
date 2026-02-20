from flask import Flask, jsonify, render_template, request
import psycopg2

DB_NAME = "madeira_trails"   
DB_USER = "postgres"         
DB_PASSWORD = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname = DB_NAME,
        user = DB_USER,
        password = DB_PASSWORD,
        host = DB_HOST,
        port = DB_PORT,
    )
    return conn

## To read strava info from pgadmin to the website
@app.get("/api/trails")
def get_trails():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT
            id,
            strava_segment_id,
            name,
            region,
            distance_m,
            elevation_gain_m,
            avg_grade,
            start_lat,
            start_lon,
            end_lat,
            end_lon,
            polyline,
            climb_category,
            climb_category_desc
        FROM strava.trails;
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    # convert rows to list of dicts
    trails = []
    for row in rows:
        (
            id_,
            strava_segment_id,
            name,
            region,
            distance_m,
            elevation_gain_m,
            avg_grade,
            start_lat,
            start_lon,
            end_lat,
            end_lon,
            polyline,
            climb_cat,
            climb_cat_desc,
        ) = row

        trails.append({
            "id": id_,
            "strava_segment_id": strava_segment_id,
            "name": name,
            "region": region,
            "distance_m": distance_m,
            "elevation_gain_m": elevation_gain_m,
            "avg_grade": float(avg_grade) if avg_grade is not None else None,
            "climb_category_desc": climb_cat_desc,
            "start_lat": start_lat,
            "start_lon": start_lon,
            "end_lat": end_lat,
            "end_lon": end_lon,
            "polyline": polyline,
        })

    return jsonify(trails)

## THIS IS THE POST-END, CONVERTING USER INPUT FROM WEBSITE BACK TO PGADMIN
# For Reviews
@app.route('/api/reviews', methods=['POST'])
def submit_review():
    data = request.get_json()
    username   = data.get('username')
    trail_name = data.get('trail_name')
    rating     = data.get('rating')
    comment    = data.get('comment')

    conn = get_db_connection()
    cur = conn.cursor()
    # Insert user if they don't exist yet
    cur.execute(
        "INSERT INTO pa.users (username) VALUES (%s) ON CONFLICT DO NOTHING",
        (username,)
    )
    # Insert trail if it doesn't exist yet
    cur.execute(
        "INSERT INTO pa.trails (trail_name) VALUES (%s) ON CONFLICT DO NOTHING",
        (trail_name,)
    )
    # Insert review
    cur.execute(
        """INSERT INTO pa.trail_ratings (trail_name, rating, username, comment)
           VALUES (%s, %s, %s, %s)""",
        (trail_name, rating, username, comment)
    )

    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'success': True}), 201

## For Reports
@app.route('/api/reports', methods=['POST'])
def submit_report():
    data = request.get_json()
    trail_name   = data.get('trail_name')
    maint_comment      = data.get('maint_comment')

    conn = get_db_connection()
    cur = conn.cursor()
     # Insert trail if it doesn't exist yet
    cur.execute(
        "INSERT INTO pa.trails (trail_name) VALUES (%s) ON CONFLICT DO NOTHING",
        (trail_name,)
    )
    cur.execute(
        """INSERT INTO pa.maintenance (trail_name, maint_comment)
           VALUES (%s, %s)""",
        (trail_name, maint_comment)
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'success': True}), 201

# For ratings
@app.get("/api/trail_ratings")
def get_trail_ratings():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            trail_name,
            ROUND(AVG(rating), 2) AS avg_rating,
            COUNT(rating)         AS total_reviews
        FROM pa.trail_ratings
        GROUP BY trail_name
        ORDER BY avg_rating DESC;
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    ratings = []
    for row in rows:
        trail_name, avg_rating, total_reviews = row
        ratings.append({
            "trail_name":    trail_name,
            "avg_rating":    float(avg_rating) if avg_rating else None,
            "total_reviews": total_reviews
        })

    return jsonify(ratings)


## To read info from pgadmin to the website
@app.get("/")
def index():
    return render_template("map.html")

if __name__ == "__main__":
    app.run(debug=True)


