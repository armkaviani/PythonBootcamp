from tkinter import *
import requests

class KanyeGetQuote:
    def __init__(self):
        self.kanye_api = "https://api.kanye.rest"

    def get_quote(self):
        self.response = requests.get(self.kanye_api)
        self.response.raise_for_status()
        return self.response.json()
 