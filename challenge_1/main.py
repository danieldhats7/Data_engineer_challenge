import requests
import json
import pandas as pd
from datetime import datetime
from cfg import URL


url = URL
response = requests.get(url)
resp = json.loads(response.text)


print(df.head(2))







if __name__ == '__main__':
    pass