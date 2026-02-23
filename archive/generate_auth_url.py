#import os
##run this first, gives us an authorization/authentication code within the url encoded on your console to activate the connection between the strava api and our device

CLIENT_ID = "201696"  # replace with your actual client id
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

