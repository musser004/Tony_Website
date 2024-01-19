import requests
import os

# Environmental variables are pulled in

SHEETY_APP_ID = os.environ["SHEETY_APP_ID"]
SHEETY_API_KEY = os.environ["SHEETY_APP_KEY"]
SHEETY_AUTHORIZATION = os.environ["SHEETY_AUTHORIZATION"]
SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

# Headers defined for authorization purposes

sheety_headers = {
    "x-app-id": SHEETY_APP_ID,
    "x-app-key": SHEETY_API_KEY,
    "Authorization": SHEETY_AUTHORIZATION
}


class EventManager:

    def __init__(self):
        self.events_data = {}

    # Method to pull event data from "events" tab of spreadsheet

    def get_event_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=sheety_headers)
        data = response.json()
        self.events_data = data["events"]
        return self.events_data
