import requests
from config import PIXELA_API, TOKEN, USERNAME

class CreateUsername:
    def __init__(self):
        self.users_params = {
            "token" : TOKEN,
            "username" : USERNAME,
            "agreeTermsOfService" : "yes",
            "notMinor" : "yes",
        }

    def create_username(self):
        response = requests.post(url=PIXELA_API, json=self.users_params)
        print(response.text)

