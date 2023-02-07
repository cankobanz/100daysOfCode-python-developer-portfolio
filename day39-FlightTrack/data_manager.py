import requests
import tqdm

SHEET_ENDPOINT = "https://api.sheety.co/f1ff9f304e3d80af454c807ac038766d/flightDeals/prices"
SHEET_ENDPOINT_USERS = "https://api.sheety.co/f1ff9f304e3d80af454c807ac038766d/flightDeals/users"
class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_data(self):
        sheet_response_get = requests.get(SHEET_ENDPOINT)
        self.destination_data = sheet_response_get.json()["prices"]
        return self.destination_data

    def edit_iata_code(self, city_code, id):
        sheet_params = {"price": {"iataCode": city_code}}
        sheet_endpoint_get = f"{SHEET_ENDPOINT}/{id}"
        sheet_response = requests.put(sheet_endpoint_get, json=sheet_params)

    def edit_price(self, price, id):
        sheet_params = {"price": {"lowestPrice": price}}
        sheet_endpoint_get = f"{SHEET_ENDPOINT}/{id}"
        sheet_response = requests.put(sheet_endpoint_get, json=sheet_params)


    def get_users(self):
        sheet_response_get = requests.get(SHEET_ENDPOINT_USERS)
        self.destination_data = sheet_response_get.json()
        return self.destination_data

    def add_user(self, first_name, last_name, e_mail):
        sheet_params = {"user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": e_mail
        }}
        sheet_response = requests.post(SHEET_ENDPOINT_USERS, json=sheet_params)


