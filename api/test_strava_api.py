import requests

ACCESS_TOKEN = "7c7932203d34c8a597df4eb22cfa577fc743829e"

def main():
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    url = "https://www.strava.com/api/v3/athlete"

    response = requests.get(url, headers=headers)
    print("Status code:", response.status_code)
    print("Response JSON:", response.json())

if __name__ == "__main__":
    main()