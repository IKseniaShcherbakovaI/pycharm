import os

from src.processing import filter_by_state, sort_by_date
from src.reading_files import transaction_csv, transaction_excel
from src.search import search_string
from src.utils import transaction
from src.widget import get_date, mask_account_card


def main():
    """
    Функция которая отвечает за основную логику проекта с пользователем и связывает функциональности между собой.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    work = True
    while work:
        print(
            """Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла""",
        )

        input_item = input("-> ")

        if input_item == "1":
            current_dir = os.path.dirname(os.path.abspath(__file__))
            rel_file_path = os.path.join(current_dir, "..//data//operations.json")
            abs_file_path = os.path.abspath(rel_file_path)
            result = transaction(abs_file_path)
            print("Для обработки выбран JSON-файл.")
            work = False
        elif input_item == "2":
            current_dir = os.path.dirname(os.path.abspath(__file__))
            rel_file_path = os.path.join(current_dir, "..//data//transactions.csv")
            abs_file_path = os.path.abspath(rel_file_path)
            result = transaction_csv(abs_file_path)
            print("Для обработки выбран csv-файл.")
            work = False
        elif input_item == "3":
            current_dir = os.path.dirname(os.path.abspath(__file__))
            rel_file_path = os.path.join(current_dir, "..//data//transactions_excel.xlsx")
            abs_file_path = os.path.abspath(rel_file_path)
            result = transaction_excel(abs_file_path)
            print("Для обработки выбран excel-файл.")
            work = False
        else:
            print("Вы выбрали вариант которого нет")

    work = True
    while work:
        print(
            """Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )
        status = input("-> ").upper()
        state_variant = ["EXECUTED", "CANCELED", "PENDING"]
        if status in state_variant:
            result_2 = filter_by_state(result, state=status)
            work = False
        if status not in state_variant:
            print(f'Статус операции "{status}" недоступен.')
    print(f'Операции отфильтрованы по статусу "{status}"')

    work = True
    while work:
        print("Отсортировать операции по дате? Да/Нет")
        value_input = input("-> ").lower()
        if value_input == "да":
            job = True
            while job:
                print("Отсортировать по возрастанию или по убыванию?")
                method_input = input("-> ")
                if method_input == "по убыванию":
                    result_3 = sort_by_date(result_2)
                    job = False
                    work = False
                elif method_input == "по возрастанию":
                    result_3 = sort_by_date(result_2, ascending=True)
                    job = False
                    work = False
        elif value_input == "нет":
            result_3 = result_2
            work = False

    work = True
    while work:
        print("Выводить только рублевые тразакции? Да/Нет")
        currency_input = input("-> ").lower()
        result_4 = []
        if currency_input == "да":
            try:
                for trans in result_3:
                    if trans["currency_code"] == "RUB":
                        result_4.append(trans)
                        work = False
            except Exception:
                for trans in result_3:
                    if trans["operationAmount"]["currency"]["code"] == "RUB":
                        result_4.append(trans)
                        work = False
        elif currency_input == "нет":
            result_4 = result_3
            work = False

    work = True
    while work:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        reply_input = input("-> ").lower()
        if reply_input == "да":
            print("Введите слово: ")
            word_input = input("-> ")
            result_5 = search_string(result_4, word_input)
            work = False
        elif reply_input == "нет":
            result_5 = result_4
            work = False

    print("Распечатываю итоговый список транзакций...\n")

    print(f"Всего банковских операций в выборке: {len(result_5)}\n")
    if len(result_5) == 0:
        return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
    else:
        our_result = ""
        for operations in result_5:
            try:
                currency = operations["operationAmount"]["currency"]["name"]
                date = get_date(operations["date"])
                description = operations["description"]
            except Exception:
                currency = operations["currency_name"]
                date = get_date(operations["date"])
                description = operations["description"]
            try:
                account = mask_account_card(operations["from"]) + " -> " + mask_account_card(operations["to"])
            except Exception:
                account = mask_account_card(operations["to"])
            try:
                sum_ = operations["operationAmount"]["amount"]
                our_result += f"{date} {description}\n{account}\nСумма {sum_} {currency}\n\n"
            except Exception:
                sum_ = operations["amount"]
                our_result += f"{date} {description}\n{account}\nСумма {sum_} {currency}\n\n"
        return our_result
