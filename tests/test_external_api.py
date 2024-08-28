from unittest.mock import patch

import pytest

from src.external_api import transaction_amount


@pytest.fixture
def trans_1():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "руб.",
                "code": "USD"}
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }


@pytest.fixture
def trans_2():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "руб.",
                "code": "RUB"}
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }


@patch('requests.request')
def test_transaction_amount(mock_get, trans_1):
    mock_get.return_value.json.return_value = {'success': True,
                                               'query': {'from': 'USD', 'to': 'RUB', 'amount': 31957.58},
                                               'info': {'timestamp': 1724845264, 'rate': 91.398757},
                                               'date': '2024-08-28', 'result': 2920883.088728}
    assert transaction_amount(trans_1) == 2920883.088728


@patch('requests.request')
def test_transaction_amount(mock_get, trans_2):
    mock_get.return_value.json.return_value = {'success': True,
                                               'query': {'from': 'RUB', 'to': 'RUB', 'amount': 8221.37},
                                               'info': {'timestamp': 1724845264, 'rate': 91.398757},
                                               'date': '2024-08-28', 'result': 8221.37}
    assert transaction_amount(trans_2) == 8221.37

