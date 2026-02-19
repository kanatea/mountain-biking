import requests

CLIENT_ID = "201696"            # same as before
CLIENT_SECRET = "633f43ca5566dc20c8ba22cb10668f193a381cb8"    # same as before
REFRESH_TOKEN = "410bb7b5c879a1b4aeb0f52cb55deaab9006d964"    # from the previous 200 response

def main():
    url = "https://www.strava.com/api/v3/oauth/token"
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN,
    }

    response = requests.post(url, data=data)
    print("Status code:", response.status_code)
    print("Response JSON:", response.json())

if __name__ == "__main__":
    main()
