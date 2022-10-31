import os
import json
import requests

from dotenv import load_dotenv
from plotly.express import line

load_dotenv()

API_KEY = os.getenv("API_KEY")

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

response = requests.get(request_url)

raw_data = json.loads(response.text)
print(type(raw_data))

