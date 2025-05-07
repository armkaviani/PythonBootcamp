import requests
from config import GRAPH_API, TOKEN


class CreateGraph:
    def __init__(self):
       self.graph_params = {
           "id" : "graph-1",
           "name" : "Reading Graph",
           "unit" : "minutes",
           "type" : "int",     
           "color" : "ajisai"      
          } 
       
       self.headers = {
           "X-USER-TOKEN" : TOKEN
       }


    def create_graph(self):
        response = requests.post(url=GRAPH_API, json=self.graph_params, headers=self.headers)
        print(response.text)