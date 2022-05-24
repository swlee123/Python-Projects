# Stock News Reminder 
Lately the stock market is facing huge fear due to the hike of interest of by US Federal Reserve.
I don't trade stocks (still young,dumb and broke) but I am a bit interested about it.

## Usage
The code used [news API](https://newsapi.org/) and [stock market API](https://www.alphavantage.co/) to retrieve information.
If the stock price increased or decreased by **5%** (at least) compare to the previous day,it will send a SMS using [Twilio](https://www.twilio.com/) into my phone with 3 trending articles about the stocks.
In my code, I chose TESLA stock since I was quite interested and impressed by TESLA's edge-cutting technology.

## Automation
The code was set in [pythonanywhere](https://www.pythonanywhere.com/user/wei489/) webstite and will run daily on a specific time.
