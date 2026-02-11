import os

CLIENT_ID = "12345"  # replace with your actual client id
REDIRECT_URI = "http://localhost/exchange_token"

url = (
    "https://www.strava.com/oauth/authorize"
    f"?client_id={CLIENT_ID}"
    "&response_type=code"
    f"&redirect_uri={REDIRECT_URI}"
    "&approval_prompt=force"
    "&scope=read,read_all,profile:read_all,activity:read_all"
)

print("Open this URL in your browser:")
print(url)
