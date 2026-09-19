# Stock Trading News Alert

A Python application that monitors daily stock price movements using the Alpha Vantage API. If a significant price change is detected, it fetches relevant company news via the NewsAPI and dispatches alerts using the Twilio API.

## Features

- Fetches daily closing stock prices.
- Calculates daily percentage changes.
- Retrieves the top 3 related news articles when price movements occur.
- Sends instant notifications.

## Requirements

- Python 3.x
- `requests`
- `python-dotenv`
- `twilio`

## Environment Variables

Create a `.env` file in the root directory and define the following variables:

```env
STOCK_API_KEY=your_alpha_vantage_api_key
NEWS_API_KEY=your_news_api_key
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
MY_PHONE_NUMBER=whatsapp:+your_phone_number
TRILLO_NUMBER=whatsapp:+your_twilio_number
