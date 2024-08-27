import json
from json import JSONDecodeError


def transaction(path):
    """функция возвращающая список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return []
    except JSONDecodeError:
        return []
    return data
