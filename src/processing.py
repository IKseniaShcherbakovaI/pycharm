def filter_by_state(incoming_list, state="EXECUTED"):
    """
    Функция возвращающая новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению.
    """
    result = []
    for items in incoming_list:
        if state == items.get("state"):
            result.append(items)
    return result


def sort_by_date(incoming_list, ascending=False):
    """
    Функция сортирующая список словарей по дате'
    """
    sorted_list = []
    for items in incoming_list:
        if ascending == False:
            sorted_list += sorted(incoming_list, key=lambda x: x["date"], reverse=True)
        else:
            sorted_list += sorted(incoming_list, key=lambda x: x["date"], reverse=False)
        return sorted_list
