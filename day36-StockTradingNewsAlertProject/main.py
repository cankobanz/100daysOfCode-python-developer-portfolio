import requests
from datetime import date
from datetime import timedelta
import os
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

api_key_stock = "R0MMDJXR3OILUYR2"
api_key_news = "ad50ccbe0b574cc39335ac005425be24"

TODAY = date.today()

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": api_key_stock,
}

news_params = {
    "q": COMPANY_NAME,
    "from": TODAY,
    "sortBy": "popularity",
    "apiKey" : api_key_news
}

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response_stock = requests.get(STOCK_ENDPOINT, params=stock_params)
response_stock.raise_for_status()
data_stock = response_stock.json()
yesterday = TODAY - timedelta(days=1)
yesterday_data = data_stock["Time Series (Daily)"][str(yesterday)]
yesterday_close = yesterday_data["4. close"]
prev_day = yesterday - timedelta(days=1)

if prev_day.weekday() == 6:
    prev_day = prev_day - timedelta(days=2)

prev_day_data = data_stock["Time Series (Daily)"][str(prev_day)]
prev_day_close = prev_day_data["4. close"]
diff = abs(float(yesterday_close) - float(prev_day_close))
perc_diff = diff/float(yesterday_close)*100

if prev_day_close < yesterday_close:
    mark = "🔺"
else:
    mark = "🔻"

if perc_diff > 3:
    response_news = requests.get(NEWS_ENDPOINT, params=news_params)
    response_news.raise_for_status()
    data_news = response_news.json()["articles"][:3]

    account_sid = "AC81fb51c61d22fa7c615a5bf2aaeac525"
    auth_token = "f8279dbcca2e47e2d29b29801aa70a5d"
    client = Client(account_sid, auth_token)

    for m in data_news:
        headline = m["title"]
        brief = m["description"]
        message = client.messages.create(
            body=f"{COMPANY_NAME}: {mark}{perc_diff}%\n"
                 f"Headline: {headline}"
                 f"Brief: {brief}",
            from_="+12183775794",
            to="+905322266228"
        )

    response_news = requests.get(NEWS_ENDPOINT, params=news_params)
    response_news.raise_for_status()
    data_news = response_news.json()["articles"][:3]

    account_sid = "AC81fb51c61d22fa7c615a5bf2aaeac525"
    auth_token = "f8279dbcca2e47e2d29b29801aa70a5d"
    client = Client(account_sid, auth_token)

    for m in data_news:
        headline = m["title"]
        brief = m["description"]
        message = client.messages.create(
            body=f"{COMPANY_NAME}: {mark}{perc_diff}%\n"
                 f"Headline: {headline}"
                 f"Brief: {brief}",
            from_="+12183775794",
            to="+905322266228"
        )
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

