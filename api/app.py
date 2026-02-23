##This script runs the API connections

#from flask import Flask, jsonify, render_template, request
#import psycopg2
#from datetime import datetime, timedelta


DB_NAME = "madeira_trails"    #replace with your database name
DB_USER = "postgres"          #replace with your username         
DB_PASSWORD = "postgres"      #replace with your password
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

## These are the api connections for the post-end, converts data from users on the front-end back to pg admin
# For user reviews
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

## For user maintenance reports 
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


# This takes the stored maintenance reports on pg admin and returns the most recent report within 2 weeks
# to display on the front end website
# Latest trail report for popup
@app.get("/api/latest_report")
def get_latest_report():
    trail_name = request.args.get("trail_name")
    if not trail_name:
        return jsonify({"error": "trail_name is required"}), 400

    conn = get_db_connection()
    cur = conn.cursor()

    # Adjust column name if not `created_at`
    cur.execute("""
        SELECT maint_comment, created_at
        FROM pa.maintenance
        WHERE trail_name = %s
        ORDER BY created_at DESC
        LIMIT 1;
    """, (trail_name,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if not row:
        # No reports at all for this trail
        return jsonify({"has_recent": False})

    maint_comment, created_at = row

    cutoff = datetime.utcnow() - timedelta(days=14)
    if created_at < cutoff:
        # Report exists but is older than 2 weeks
        return jsonify({"has_recent": False})

    return jsonify({
        "has_recent": True,
        "trail_name": trail_name,
        "maint_comment": maint_comment,
        "created_at": created_at.isoformat()
    })

# For ratings - This takes the stored user rating data on pg admin and aggregates it 
# to return average rating per trail to display on the front end website
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


## To read the html file that establishes the front-end
@app.get("/")
def index():
    return render_template("map.html")

if __name__ == "__main__":
    app.run(debug=True)





