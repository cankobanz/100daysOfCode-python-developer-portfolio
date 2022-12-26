# Challenge
from random import choice
import datetime as dt
import smtplib

with open("quotes.txt") as f:
    all_quotes = f.readlines()
quote = choice(all_quotes)  # Random quote

now = dt.datetime.now()
weekday = now.weekday()

from_addr = "thirtydays03@gmail.com"
password = "qfuldnvkkjbccidn"
to_addrs = "thirthydays03@yahoo.com"

if weekday == 6: # 6 means Sunday. 0 monday etc.
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Transport Layer Security, decrypted the email and makes it impossible to read
        connection.login(user=from_addr, password=password)
        connection.sendmail(from_addr=from_addr, to_addrs=to_addrs,
                            msg=f"Subject:Motivational Quote\n\n{quote}")
