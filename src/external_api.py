import os

import requests
from dotenv import load_dotenv

load_dotenv(".env.example")
api_key = os.getenv("API_KEY")
headers = {"apikey": api_key}


def transaction_amount(transaction):
    """
    Функция конвертации
    """
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    if amount == "0":
        return float(0)
    elif currency != "RUB":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        rub_amount = requests.request("GET", url=url, headers=headers)
        result = rub_amount.json()
        return float(result["result"])
    else:
        return float(amount)
