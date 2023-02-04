import requests
import datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "ad89g7ad8baz98dfg9as"
USERNAME = "canko12"
graph_id = "graph1"


user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': "yes",
    'notMinor': "yes"
}

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
today_date = dt.date.today()
pixel_enpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
pixel_config = {
    "date": today_date.strftime("%Y%m%d"),
    "quantity": "2.2"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.put(url=pixel_enpoint, json=config, headers=headers)
print(response.text)