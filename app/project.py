import json
import requests

from plotly.express import line
from app.alpha import API_KEY

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

response = requests.get(request_url)

raw_data = json.loads(response.text)
print(type(raw_data))

data = raw_data["data"]

# Challenge A

print("-------------------------")
print("Latest Unemployment Rate: "+f"{data[0]['value']}%")

# Challenge B

from statistics import mean

data_2022 = [d for d in data if "2022-" in d["date"]]

rates_2022 = [float(d["value"]) for d in data_2022]

print("-------------------------")
print("Average Unemployment this Year:", f"{mean(rates_2022)}%")
print("Number of Months:", len(data_2022))

# Challenge C

dates = [d["date"] for d in data]
rates = [float(d["value"]) for d in data]

fig = line(x=dates, y=rates, title="United States Unemployment Rate over Time", labels= {"x": "Time", "y": "Unemployment Rate"})
fig.show()