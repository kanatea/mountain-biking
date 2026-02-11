# import requests

## to obtain refresh and access tokens to access data from strava API
## want a 200 code 

CLIENT_ID = "201696"  # strava client ID
CLIENT_SECRET = "633f43ca5566dc20c8ba22cb10668f193a381cb8"  # strava secret 
AUTH_CODE = "a82205bc0b7bc148927a5dc2a5f940762b58af47" # authorization code generated to gain access to strava api from generate_auth_url.py
REDIRECT_URI = "http://localhost/exchange_token"

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


## Strava tokens
### 'refresh_token': '410bb7b5c879a1b4aeb0f52cb55deaab9006d964'
###'access_token': '7c7932203d34c8a597df4eb22cfa577fc743829e' 
