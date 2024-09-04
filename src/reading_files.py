import pandas as pd


def transaction_csv(path_csv):
    ''' Функция принимающая на вход путь до csv файла и возвращающая список словарей с данными о финансовых транзакциях'''
    if not path_csv:
        return []
    try:
        df = pd.read_csv(path_csv, delimiter=';')
        return df.to_dict(orient="records")
    except Exception:
        return []


def transaction_excel(path_excel):
    ''' Функция принимающая на вход путь до excel файла и возвращающая список словарей с данными о финансовых транзакциях'''
    if not path_excel:
        return []
    try:
        df = pd.read_excel(path_excel)
        return df.to_dict(orient="records")
    except Exception:
        return []

# print(transaction_csv('C:/Users/Ксения/Desktop/homework/data/transactions.csv'))
# print(transaction_csv(''))
# print(transaction_excel(''))
# print(transaction_excel('C:/Users/Ксения/Desktop/homework/data/transactions_excel.xlsx'))
