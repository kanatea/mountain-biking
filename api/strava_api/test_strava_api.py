import requests

ACCESS_TOKEN = "95ece59d960098fe62ecbff2c03f4e211150f700"

def main():
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    url = "https://www.strava.com/api/v3/athlete"

    response = requests.get(url, headers=headers)
    print("Status code:", response.status_code)
    print("Response JSON:", response.json())

if __name__ == "__main__":
    main()