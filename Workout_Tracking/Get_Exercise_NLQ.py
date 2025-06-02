import requests
from datetime import datetime
import os
from config import GENDER, WEIGHT_KG, HEIGHT_CM, AGE

today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")

exercise_text = input("Tell me which exercises you did: ")  

class GetExercise:
    def __init__(self):
        self.APP_ID = os.environ["ENV_NIX_APP_ID"]
        self.API_KEY = os.environ["ENV_NIX_API_KEY"]
        self.exercise_endpoint = os.environ["ENV_NIX_ENDPOINT"]
        self.sheet_endpoint = os.environ["ENV_SHEETY_ENDPOINT"]

        self.header_params = {
            "x-app-id": self.APP_ID,
            "x-app-key": self.API_KEY,
        }

        self.params = {
            "query": exercise_text,
            "gender": GENDER,
            "weight_kg": WEIGHT_KG,
            "height_cm": HEIGHT_CM,
            "age": AGE
        }

    def get_exercise_nlq(self):
        response = requests.post(self.exercise_endpoint, json=self.params, headers=self.header_params)
        self.result = response.json()
        print(self.result)

    def saving_data_in_googlesheet(self):
        for exercise in self.result["exercises"]:
            data_inputs = {
                "workout": {
                    "date": today_date,
                    "time": today_time,
                    "exercise": exercise["name"].title(),
                    "duration": exercise["duration_min"],
                    "calories": exercise["nf_calories"]
                }
            }

            # Basic Auth
            sheet_response = requests.post(
                self.sheet_endpoint,
                json=data_inputs,
                auth=(
                    os.environ["ENV_SHEETY_USERNAME"],
                    os.environ["ENV_SHEETY_PASSWORD"]
                )
            )
            print(sheet_response.text)

            # Bearer Token (optional alternative)
            bearer_headers = {
                "Authorization": f"Bearer {os.environ['ENV_SHEETY_TOKEN']}"
            }
            sheet_response = requests.post(
                self.sheet_endpoint,
                json=data_inputs,
                headers=bearer_headers
            )