import requests
import os

class RainAlert():

    def __init__(self, lat, lon):
       
        self.api_key = os.environ.get("API_KEY")
        self.weather_params = {"lat":lat, "lon":lon, "appid":self.api_key, "cnt": 4}
        



