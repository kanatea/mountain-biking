##This script loads the data from strava onto our database on pg admin. Since each request only allows for 10 "segments" or bike trails,
##we broke the area of inquiry up into tiles to maximize the number of trails we can import across madeira.
##Run the update_polylines script after this to add polyline data

#import requests
#import psycopg2
#import time

# Database credentials

ACCESS_TOKEN = "95ece59d960098fe62ecbff2c03f4e211150f700"  #update this with the refresh access token obtained from the script refresh_access_token in the strava api folder

DB_NAME = "madeira_trails"   #update this with your database name
DB_USER = "postgres"         #update this with your username
DB_PASSWORD = "postgres"     #update this with your password
DB_HOST = "localhost"
DB_PORT = "5432"

# 3x3 grid of bounding boxes covering Madeira: South, West, North, East
TILES = [
    "32.60,-17.31,32.73,-17.04",
    "32.60,-17.04,32.73,-16.77",
    "32.60,-16.77,32.73,-16.50",
    "32.73,-17.31,32.86,-17.04",
    "32.73,-17.04,32.86,-16.77",
    "32.73,-16.77,32.86,-16.50",
    "32.86,-17.31,32.99,-17.04",
    "32.86,-17.04,32.99,-16.77",
    "32.86,-16.77,32.99,-16.50",
]

def fetch_segments():
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    all_segments = []
    seen_ids = set()

    for bounds in TILES:
        print(f"Requesting segments for bounds: {bounds}")
        params = {
            "bounds": bounds,            # each tile
            "activity_type": "riding",
            "min_cat": 0,
            "max_cat": 5,
        }
        url = "https://www.strava.com/api/v3/segments/explore"

        response = requests.get(url, headers=headers, params=params)
        print("  Strava status code:", response.status_code)

        if response.status_code != 200:
            print("  Skipping this tile due to non 200 response")
            continue

        data = response.json()
        segments = data.get("segments", [])
        print(f"  Found {len(segments)} segments in this tile")

        for seg in segments:
            seg_id = seg.get("id")
            if seg_id in seen_ids:
                continue
            seen_ids.add(seg_id)
            all_segments.append(seg)

    print(f"Total unique segments collected from all tiles: {len(all_segments)}")
    return all_segments


def insert_segments_into_db(segments):
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
        )
        cur = conn.cursor()

        insert_sql = """
            INSERT INTO strava.trails (
                strava_segment_id,
                name,
                region,
                distance_m,
                elevation_gain_m,
                climb_category,
                climb_category_desc,
                avg_grade,
                start_lat,
                start_lon,
                end_lat,
                end_lon
            )
            VALUES (%s, %s, 'Madeira', %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (strava_segment_id) DO NOTHING;
        """


        for seg in segments:
            seg_id = seg.get("id")
            name = seg.get("name")
            distance = seg.get("distance")  # meters
            elev_diff = seg.get("elev_difference")  # meters
            climb_cat = seg.get("climb_category")
            climb_cat_desc = seg.get("climb_category_desc")
            avg_grade = seg.get("avg_grade")
            start_latlng = seg.get("start_latlng") or [None, None]
            end_latlng = seg.get("end_latlng") or [None, None]

            start_lat = start_latlng[0]
            start_lon = start_latlng[1]
            end_lat = end_latlng[0]
            end_lon = end_latlng[1]

            print(f"Inserting segment {seg_id} - {name}")

            cur.execute(
                insert_sql,
                (
                    seg_id,
                    name,
                    distance,
                    elev_diff,
                    climb_cat,
                    climb_cat_desc,
                    avg_grade,
                    start_lat,
                    start_lon,
                    end_lat,
                    end_lon,
                ),
            )

        conn.commit()
        cur.close()
        print("Done inserting segments into DB.")

    except Exception as e:
        print("Error inserting into database:")
        print(e)
        if conn is not None:
            conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def update_polylines():
    """
    For each segment in the database, fetch its detail from Strava
    and store the summary_polyline in the polyline column.
    """
    conn = None
    try:
        conn = psycopg2.connect(
             dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
        )
        cur = conn.cursor()

        # Get all segment IDs that we have
        cur.execute("SELECT strava_segment_id FROM strava.trails;")
        rows = cur.fetchall()
        segment_ids = [r[0] for r in rows]

        print(f"Found {len(segment_ids)} segments in DB to update polylines for.")

        # For each segment, call Strava segment detail endpoint
        headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

        for i, seg_id in enumerate(segment_ids, start=1):
            print(f"[{i}/{len(segment_ids)}] Fetching polyline for segment {seg_id}...")
            url = f"https://www.strava.com/api/v3/segments/{seg_id}"

            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                print(f"  Skipping segment {seg_id}, status code {response.status_code}")
                # Sleep a bit to avoid hitting rate limits
                time.sleep(0.3)
                continue

            data = response.json()
            # Strava returns a 'map' object with polyline/summary_polyline
            seg_map = data.get("map", {}) or {}
            polyline = seg_map.get("summary_polyline") or seg_map.get("polyline")

            if not polyline:
                print(f"  No polyline found for segment {seg_id}, skipping.")
                time.sleep(0.3)
                continue

            # Update the database
            cur.execute(
                """
                UPDATE strava.trails
                SET polyline = %s
                WHERE strava_segment_id = %s;
                """,
                (polyline, seg_id),
            )
            conn.commit()

            # Sleep a bit to avoid hitting rate limits
            time.sleep(0.3)

        cur.close()
        print("Done updating polylines.")

    except Exception as e:
        print("Error updating polylines:")
        print(e)
        if conn is not None:
            conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def main():
    segments = fetch_segments()
    if not segments:
        print("No segments to insert.")
        return
    insert_segments_into_db(segments)


if __name__ == "__main__":
    main()


