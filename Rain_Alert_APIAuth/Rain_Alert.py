import requests
import os
from twilio.rest import Client

class RainAlert():

    def __init__(self, lat, lon):
       
        self.api_key = os.environ.get("API_KEY")
        self.weather_params = {"lat":lat, "lon":lon, "appid":self.api_key, "cnt": 4}
        self.auth_token = os.environ.get("AUTH_TOKEN")
        self.weather_params = {"lat":lat, "lon":lon, "appid":self.api_key, "cnt": 4}
        self.twilio_from = os.environ.get("TWILIO_FROM") 
        self.twilio_to = os.environ.get("TWILIO_TO")    

    def request_api(self):
        self.responds = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=self.weather_params)
        self.responds.raise_for_status()
        weather_data = self.responds.json()

        will_rain = False
        for data in weather_data['list']:
            condition_code =  data["weather"][0]["id"]
            if int(condition_code) < 700:
                will_rain = True
                print(f"⛈️ Forecast: {data['weather'][0]['description']} at {data['dt_txt']}")

    
        if will_rain:
            client = Client(self.account_sid, self.auth_token)
            message = client.messages \
                .create(
                body="It is going to rain today. Bring an umbrella.",
                from_=self.twilio_from ,
                to=self.twilio_to 
                )
            print(f"✅ SMS sent: {message.sid}")

        else:
            print("🌤️ No rain expected in the next 12 hours.")
            



        



