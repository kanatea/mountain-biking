##This script is to test the device to strava api connection 
##If the connection is successful, your strava account information should display on the console
#import requests

ACCESS_TOKEN = "95ece59d960098fe62ecbff2c03f4e211150f700" # The new refresh access token code from running the refresh_access_token script should go here

def main():
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    url = "https://www.strava.com/api/v3/athlete"

    response = requests.get(url, headers=headers)
    print("Status code:", response.status_code)
    print("Response JSON:", response.json())

if __name__ == "__main__":

    main()
