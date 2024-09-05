
тут вся хуйня что ю не мешщалась

work = True
while work:
    print('''Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')
    status = input('-> ').upper()
    state_variant = ['EXECUTED', 'CANCELED', 'PENDING']
    if status not in state_variant:
        print(f'Статус операции "{status}" недоступен.')
        # status = input('-> ').upper()
    else:
        work = False
print(f'Операции отфильтрованы по статусу "{status}"')
