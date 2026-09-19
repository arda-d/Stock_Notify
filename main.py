import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")
TRILLO_NUMBER = os.getenv("TRILLO_NUMBER")

STOCK_NAME = "AAPL"
COMPANY_NAME = "Apple Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data_json = response.json()



data = data_json["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_close = float(data_list[0]["4. close"])
day_before_close = float(data_list[1]["4. close"])

difference = yesterday_close - day_before_close
up_down = "🔺" if difference > 2 else "🔻"
diff_percentage = round((abs(difference) / yesterday_close) * 100, 2)

if diff_percentage >= 0:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json().get("articles", [])[:3]

    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percentage}%\nHeadline: {article['title']}\nBrief: {article['description']}"
        for article in articles
    ]

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    for article_text in formatted_articles:
        message = client.messages.create(
            body=article_text,
            from_=TRILLO_NUMBER,
            to=MY_PHONE_NUMBER,
        )