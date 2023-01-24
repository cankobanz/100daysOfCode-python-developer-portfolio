import requests
from datetime import datetime
import smtplib


def is_iss_overhead():
    MY_LAT = 51.507351  # Your latitude
    MY_LONG = -0.127758  # Your longitude

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_latitude <= MY_LONG + 5:
        return True


# Your position is within +5 or -5 degrees of the ISS position.

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now >= sunset or time_now <= sunrise:
        return True


from_addr = "thirtydays03@gmail.com"
password = "qfuldnvkkjbccidn"
to_addrs = "thirthydays03@yahoo.com"

if is_night() and is_iss_overhead():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Transport Layer Security, decrypted the email and makes it impossible to read
        connection.login(user=from_addr, password=password)
        connection.sendmail(from_addr=from_addr, to_addrs=to_addrs,
                            msg=f"Hey! Look up.")
