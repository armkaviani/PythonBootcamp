import requests
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
from pprint import pprint

load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/3bc42ef445e4e059e3fa4d68b4e50d15/myFlightDeals/prices"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.username = os.environ["SHEETY_USER"]
        self.password = os.environ["SHEETY_PASS"]
        self.authorization = HTTPBasicAuth(self.username, self.password)
        self.destination_data = {}

    def get_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self.authorization)
        data = response.json()
        pprint(data)
        self.destination_data = data["prices"]
        return self.destination_data
        
    
    def update_data(self):
        for city in self.destination_data:
            new_input = {
                "price": {"iataCode" : city["iataCode"]}
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",json=new_input, auth=self.authorization )
            print(response.text)


