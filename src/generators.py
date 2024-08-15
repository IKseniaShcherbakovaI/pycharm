def filter_by_currency(transactions: list, state: str) -> list:
    '''Функция выдающая список тразакций по определенной валюте'''
    if transactions == []:
        exit('Нет транзакций')

    for i in transactions:
        if i.get("operationAmount").get('currency').get('code') == state:
            yield i

    for i in transactions:
        if state not in i.get("operationAmount").get('currency').get('code') or state == '':
            exit('С данной валютой не было транзакций')


def transaction_descriptions(transactions):
    if transactions == []:
        exit('Нет транзакций')

    for i in transactions:
        if i.get("description"):
            yield i.get("description")



def card_number_generator(start= 1, stop= 99):
    for _ in range(start, stop + 1):
        card_number = str(_)
        while len(card_number) < 16:
            card_number = '0' + card_number
        yield f'{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}'




































