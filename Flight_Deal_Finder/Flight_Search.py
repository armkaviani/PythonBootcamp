import requests
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_API_SECRET"]
        self._token = self._get_new_token()

    # For making any requests to Amadeus needs a token
    def _get_new_token(self):
        header = {
            'Conten-Type': 'application/x-www-form-urlencoded'
        }
        body = {
        'grant_type': 'client_credentials',
        'client_id': self._api_key,
        'client_secret': self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)

        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']


    def get_destination(self, city_name):
        code = "TESTING"
        return code