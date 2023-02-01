##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
# 2. Check if TODAY matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
import random

import pandas as pd
import datetime as dt
import smtplib

data = pd.read_csv("birthdays.csv")
now = dt.datetime.now()
for index, rows in data.iterrows():
    birthday = dt.datetime(year=rows["year"], month=rows["month"], day=rows["day"])
    if now.month == birthday.month and now.day == birthday.day:
        with open(f"letter_templates\letter_{random.randint(1,3)}.txt") as f:
            letter = f.read()
        letter = letter.replace("[NAME]", rows["name"])
        letter = letter.replace("Angela", "Can")

        from_addr = "thirtydays03@gmail.com"
        password = "qfuldnvkkjbccidn"
        to_addrs = rows["email"]

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=from_addr, password=password)
            connection.sendmail(from_addr=from_addr, to_addrs=to_addrs,
                                msg=f"Subject:Happy Birthday!\n\n{letter}")