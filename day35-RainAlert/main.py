import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "69f04e4613056b159c2761a9d9e664d2"

part = "current,minutely,daily,alerts"

weather_params = {
    "lat": 41.008240,
    "lon": 28.978359,
    "appid": api_key,
    "exclude": part
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()["hourly"][0:12]
for hour_data in data:
    condition = int(hour_data["weather"][0]["id"])
    if condition < 700:
        print("Bring an umbrella!")

# print(data["weather"][0]["id"])