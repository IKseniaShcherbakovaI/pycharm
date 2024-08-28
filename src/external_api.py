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
        return 0
    elif currency != "RUB":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        rub_amount = requests.request("GET", url=url, headers=headers)
        result = rub_amount.json()
        return result["result"]
    else:
        return float(amount)


# print(
#     transaction_amount(
#         transaction={
#             "id": 441945886,
#             "state": "EXECUTED",
#             "date": "2019-08-26T10:50:58.294041",
#             "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "USD"}},
#             "description": "Перевод организации",
#             "from": "Maestro 1596837868705199",
#             "to": "Счет 64686473678894779589",
#         }
#     )
# )
#
# print(type(
#     transaction_amount({
#         "id": 441945886,
#         "state": "EXECUTED",
#         "date": "2019-08-26T10:50:58.294041",
#         "operationAmount": {
#             "amount": "31957.58",
#             "currency": {
#                 "name": "руб.",
#                 "code": "RUB"}
#         },
#         "description": "Перевод организации",
#         "from": "Maestro 1596837868705199",
#         "to": "Счет 64686473678894779589"
#     })
# ))
