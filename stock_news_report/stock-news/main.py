
# request data from stock websites and news website,when specific stock price move 5% in a day,send sms to inform
# here we implement Tesla
# put in on Pythonanywhere the code automatically run every day
# account_sid and auth_token can change to environmental variable for extra security


import requests
import datetime as dt
import os
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# CRYPTO = "BITCOIN" option for crypto news

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = "720c3c6117cd47ebb9ac6d62fea3f47f"
STOCK_PRICE_API_KEY = "VMSVFMNQZZJEXNBI"

# account_sid = "AC1e4d2ae05ea49d10c12e38b4fb3f96cb"
# auth_token = "eac9b137ba75d3c092982ba1431e0750"
account_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("AUTH_TOKEN")

SENDER = "+12057975541"
RECERVER = "+60 17 907 1293"
# edit sender and receiver(yourself)


DATE = str(dt.date.today())
DATE = DATE[:8]+str(int(DATE[8:])-3)
yesterday = int(DATE[8:])-1
SEMALAM_DATE = DATE[:8]+str(yesterday)

stock_news_parameter = {
    "apiKey":NEWS_API_KEY,
    "q":STOCK,
    "searchIn":"title,content",
    "from":DATE,
    "language":"en",
    "sortBy":"relevancy",
    "pageSize":10
}

stock_price_parameter = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "outputsize":5,
    "apikey":STOCK_PRICE_API_KEY


}


## Use https://newsapi.org/docs/endpoints/everything

stock_news = requests.get(url=NEWS_ENDPOINT,params=stock_news_parameter)
stock_response = stock_news.json()


# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Use stock_price api

stock_price = requests.get(url=STOCK_ENDPOINT,params=stock_price_parameter)
stock_price = stock_price.json()


TODAY_CLOSING = float(stock_price["Time Series (Daily)"][DATE]["4. close"])
SEMALAM_CLOSING = float(stock_price["Time Series (Daily)"][SEMALAM_DATE]["4. close"])

# Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices.
move_percentage = 0

# check current day(3 days ago) and yesterday's(from current day) differences
def two_days_differences():
    global move_percentage

    differences = abs(TODAY_CLOSING-SEMALAM_CLOSING)
    move_percentage = (differences/SEMALAM_CLOSING)*100
    move_percentage = float(format(move_percentage,".2f"))
    # the value of 5% of yerstday's closing stock price.

    if TODAY_CLOSING > SEMALAM_CLOSING:
        return STOCK+":🔺"+str(move_percentage)+"%"
    else:
        return STOCK+":🔻" + str(move_percentage)+"%"

def send_msg(msg):
    # Use twilio.com/docs/sms/quickstart/python
    # Send a separate message with each article's title and description to your phone number.

    client = Client(account_sid, auth_token)
    for text in msg:
        message = client.messages \
            .create(
            body=text,
            from_=SENDER,
            to=RECERVER
        )
        print(message.status)

two_days_differences()
msg = []



if move_percentage > 5.0:
    # Use https://newsapi.org/docs/endpoints/everything
    # to fetch the first 3 articles for the COMPANY_NAME.
    articles = stock_response["articles"][:3]

    for news in articles:
        headline = news["title"]
        content = news["description"]
        message =(f"{two_days_differences()}\n"
              f"Headline : {headline}\n"
              f"Content : {content}")
        msg.append(message)

    send_msg(msg)




