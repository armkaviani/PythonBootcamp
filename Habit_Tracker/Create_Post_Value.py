import requests
from config import POST_VALUE_API, TOKEN, TODAY
from datetime import datetime


class CreatePostValue:
    def __init__(self):
        
        self.post_params = {
           "date" : TODAY.strftime("%Y%m%d"),
           "quantity" : "10",     
        } 

        self.headers = {
           "X-USER-TOKEN" : TOKEN
       }

    def create_value(self):
        response = requests.post(url=POST_VALUE_API, json=self.post_params, headers=self.headers)
        print(response.text)
    
    # For updating the data
    # def update_pixela(self):
    #     response = requests.put(url=UPDATE_API, json=self.update_params, headers=self.headers)
    #     print(response.text)