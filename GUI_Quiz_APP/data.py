import requests

class QuestionData:

    def __init__(self):
        self.data_param = {"amount" : 10, "type" : "boolean"}


    def question_data(self):
        self.response = requests.get( "https://opentdb.com/api.php", params=self.data_param)
        self.response.raise_for_status()
        self.data = self.response.json()
        return self.data["results"]
    
        
 