from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция возвращающая как маску карты так и маску счета"""
    accounts_card = account_card.split()
    name = ""
    number = ""
    for items in accounts_card:
        if items.isalpha():
            name += items + " "
        else:
            number += items
    if name.replace(" ", '') == "Счет":
        return f"{name}{get_mask_account(number)}"
    else:
        return f"{name}{get_mask_card_number(number)}"


def get_date(date: str) -> str:
    """Функция возвращающая дату"""
    result = date.replace("-", "")
    for date in result:
        return f"{result[6:8]}.{result[4:6]}.{result[0:4]}"

