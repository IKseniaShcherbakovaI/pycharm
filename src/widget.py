def mask_account_card(account_card: str) -> str:
    """Функция маскирующая как номер карты так и номер счета"""
    result = account_card.split()
    result_mask = ""
    if result[0] == "Счет":
        for items in result:
            if items.isdigit():
                result_mask += f"{result[0]} {'*' * 2}{items[-4:]}"
    else:
        for items in result:
            if items.isalpha():
                result_mask += items + " "
            elif items.isdigit():
                result_mask += f"{items[:4]} {items[4:6]} {'*' * 2} {'*' * 4} {items[12:]}"
    return result_mask


def get_date(date: str) -> str:
    """Функция возвращающая даты"""
    result = date.replace("-", "")
    for date in result:
        return f"{result[6:8]}.{result[4:6]}.{result[0:4]}"
