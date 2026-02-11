import requests

# FILL THESE IN CAREFULLY:
CLIENT_ID = "201696"            # e.g. "12345" (from Strava API app page)
CLIENT_SECRET = "633f43ca5566dc20c8ba22cb10668f193a381cb8"    # long secret string from the same page
AUTH_CODE = "a82205bc0b7bc148927a5dc2a5f940762b58af47" # your code
REDIRECT_URI = "developers.strava.com"        # must match your app settings

def main():
    url = "https://www.strava.com/api/v3/oauth/token"
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": AUTH_CODE,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT_URI,
    }

    print("Sending data:", data)  # for debugging
    response = requests.post(url, data=data)
    print("Status code:", response.status_code)
    print("Response JSON:", response.json())

if __name__ == "__main__":
    main()

