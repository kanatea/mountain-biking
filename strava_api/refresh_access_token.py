##This script is to get the new refresh access token to establish the device to api connection
##Running this script should yield the new refresh access token, which should be plugged into the test_strava_api script
##The refresh token should also be plugged into the load_segments_to_db script in the etl folder

import requests

CLIENT_ID = "201696"            # your strava user ID - in this case it's cammy's
CLIENT_SECRET = "633f43ca5566dc20c8ba22cb10668f193a381cb8"    # strava secret client
REFRESH_TOKEN = "410bb7b5c879a1b4aeb0f52cb55deaab9006d964"    # from the previous trial
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



