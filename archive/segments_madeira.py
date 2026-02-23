#import requests

ACCESS_TOKEN = "7c7932203d34c8a597df4eb22cfa577fc743829e"

def main():
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

    # bbox: south, west, north, east
    params = {
        "bounds": "32.6,-17.3,32.9,-16.7",
        "activity_type": "riding",   # we can later filter further
        "min_cat": 0,
        "max_cat": 5,
    }

    url = "https://www.strava.com/api/v3/segments/explore"

    response = requests.get(url, headers=headers, params=params)
    print("Status code:", response.status_code)
    data = response.json()
    segments = data.get("segments", [])

    print(f"Found {len(segments)} segments")
    for seg in segments:
        seg_id = seg.get("id")
        name = seg.get("name")
        distance = seg.get("distance")
        elev_diff = seg.get("elev_difference")
        avg_grade = seg.get("avg_grade")
        start_latlng = seg.get("start_latlng")
        end_latlng = seg.get("end_latlng")

        print("-----")
        print(f"ID: {seg_id}")
        print(f"Name: {name}")
        print(f"Distance: {distance} m")
        print(f"Elevation change: {elev_diff} m")
        print(f"Avg grade: {avg_grade}")
        print(f"Start: {start_latlng}")
        print(f"End: {end_latlng}")

if __name__ == "__main__":

    main()
