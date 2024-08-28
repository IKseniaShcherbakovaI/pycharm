import os

import pytest

from src.utils import transaction


@pytest.fixture
def path():
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    return PATH_TO_FILE


@pytest.fixture
def path2():
    return '../data/operations__.json'



@pytest.fixture
def path3():
    return '../data/operations___.json'


@pytest.fixture
def trans():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
         "amount": "31957.58",
         "currency": {
          "name": "руб.",
          "code": "RUB"}
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"}


@pytest.fixture
def trans_1():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "USD"}
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"}


def test_transaction1():
    assert transaction('') == []


def test_transaction2(path):
    assert transaction(path)[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
             "name": "руб.",
             "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"}


def test_financial_transactions_empty_list(path2):
    assert transaction(path2) == []


def test_financial_transactions_mistake_json(path3):
    assert transaction(path3) == []

