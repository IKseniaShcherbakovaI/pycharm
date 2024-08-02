def mask_account_card(account_card: str) -> str:
    """Функция маскирующая как номер карты так и номер счета"""
    result = account_card.split()
    result_mask = ''
    if result[0] == 'Счет':
        for i in result:
            if i.isdigit():
                result_mask += f"{result[0]} {'*' * 2}{i[-4:]}"
    else:
        for i in result:
            if i.isalpha():
                result_mask += i + ' '
            elif i.isdigit():
                result_mask += f'{i[:4]} {i[4:6]} {'*' * 2} {'*' * 4} {i[12:]}'
    return result_mask
