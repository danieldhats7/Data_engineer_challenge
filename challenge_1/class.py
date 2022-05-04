import requests
import json
import pandas as pd
from datetime import datetime



class Stackoverflow_questions:
    def __init__(self, URL):
        self.URL = URL
        self.resp_json = json.loads(requests.get(self.URL).text)
        self.df = pd.DataFrame(self.resp['items'])

