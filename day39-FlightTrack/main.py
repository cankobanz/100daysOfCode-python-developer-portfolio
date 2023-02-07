#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

while True:
    print("Welcome to Can's Fight Club.")
    print("We want to find best deals and email it to.")
    first_name = input("What is your first name?")
    last_name = input("What is your last name?")
    e_mail = input("What is your e-mail address?")
    re_email = input("Type your e-mail again.")
    if e_mail == re_email:
        print("You are in the club!")
        break

data_manager = DataManager()
flight_searcher = FlightSearch()
notification_manager = NotificationManager()

data_manager.add_user(first_name, last_name, e_mail)

cities = data_manager.get_data()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

ORIGIN_CITY_IATA = "IST"

for city in cities:
    city_code = flight_searcher.get_destination_code(city["city"])
    data_manager.edit_iata_code(city_code, city["id"])

    flight = flight_searcher.check_flights(
        ORIGIN_CITY_IATA,
        city_code,
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight is not None:
        try:
            if flight.price < city["lowestPrice"]:
                # notification_manager.send_sms(
                #     message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
                # )
                data_manager.edit_price(flight.price, city["id"])

                users = data_manager.get_users()["users"]
                emails = [row["email"] for row in users]
                names = [row["firstName"] for row in users]
                message = f"Low price alert! Only {flight.price}GBP to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
                # if flight.stop_overs > 0:
                #     message += f"\n\nFlight has {flight.stop_overs}, via {flight.via_city}."
                # link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
                link ="a"
                notification_manager.send_emails(emails, message, link)
        except KeyError:
            data_manager.edit_price(flight.price, city["id"])







