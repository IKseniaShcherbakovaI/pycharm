from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция возвращающая как маску карты так и маску счета"""
    result = account_card.split()
    result_mask = ""
    if result[0] == "Счет":
        for items in result:
            if items.isdigit():
                result_mask += f"{result[0]} {get_mask_account(items)}"
    else:
        for items in result:
            if items.isalpha():
                result_mask += items + " "
            elif items.isdigit():
                result_mask += f"{items[:4]} {get_mask_card_number(items)}"
    return result_mask


def get_date(date: str) -> str:
    """Функция возвращающая дату"""
    result = date.replace("-", "")
    for date in result:
        return f"{result[6:8]}.{result[4:6]}.{result[0:4]}"
