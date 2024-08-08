from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str | None:
    """Функция возвращающая как маску карты так и маску счета"""
    accounts_card = account_card.split()
    name = ""
    number = ""
    for items in accounts_card:
        if items.isalpha():
            name += items + " "
        else:
            number += items
    if name.replace(" ", "") == "Счет":
        return f"{name}{get_mask_account(number)}"
    else:
        return f"{name}{get_mask_card_number(number)}"


def get_date(date: str) -> str | None:
    """Функция возвращающая дату"""
    result = date.replace("-", "")
    for date in result:
        return f"{result[6:8]}.{result[4:6]}.{result[0:4]}"


print(get_date('2024-03-11T02:26:18.671407'))
print(get_date('2023-12-12'))
print(get_date('2020-11-10'))