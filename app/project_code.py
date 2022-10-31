

import os
import json
import requests

from dotenv import load_dotenv
from plotly.express import line

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

response = requests.get(request_url)

parsed_response = json.loads(response.text)
print(type(parsed_response))

data = parsed_response["data"]

# Challenge A

print("-------------------------")
print("LATEST UNEMPLOYMENT RATE:")
print(f"{data[0]['value']}%", "as of", data[0]["date"])


# Challenge C

dates = [d["date"] for d in data]
rates = [float(d["value"]) for d in data]

fig = line(x=dates, y=rates, title="United States Unemployment Rate over time", labels= {"x": "Month", "y": "Unemployment Rate"})
fig.show()