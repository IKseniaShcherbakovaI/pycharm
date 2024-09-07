import re
from collections import Counter


def search_string(transaction, string):
    """
    функция для поиска в списке словарей операций по заданной строке
    """
    result_search = []
    for i in transaction:
        our_str = i["description"]
        if re.findall(string, our_str, re.IGNORECASE):
            result_search.append(i)
    return result_search


def category_search(transaction, *description_):
    """
    функция для подсчета количества банковских операций определенного типа
    """
    description_search = []
    search_result = []
    for i in transaction:
        description_search.append(i["description"])
    counted = Counter(description_search)
    for item in description_:
        for item_ in item:
            search_result.append(f"{item_} {counted[item_]}")
    return search_result
