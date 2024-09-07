import pytest
from unittest.mock import patch
from src.search import search_string, category_search

# @pytest.fixture
# def test_df():
#     test_dict = {
#         "id": [650703.0, 3598919.0],
#         "state": ["EXECUTED", "EXECUTED"],
#         "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z"],
#         "amount": [16210.0, 29740.0],
#         "currency_name": ["Sol", "Peso"],
#         "currency_code": ["PEN", "COP"],
#         "from": ["Счет 58803664561298323391", "Discover 3172601889670065"],
#         "to": ["Счет 39745660563456619397", "Discover 0720428384694643"],
#         "description": ["Перевод организации", "Перевод с карты на карту"]
#     }
#
#     return test_dict



@pytest.fixture
def test_df():
    test_dict = [{'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
                  'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
                  'description': 'Перевод со счета на счет',
                  'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}]

    return test_dict

@pytest.fixture
def test_df2():
    test_dict = [
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  }]

    return test_dict



def test_search_string(test_df):
    assert search_string(test_df, "Перевод со счета на счет") == test_df

    assert search_string(test_df, "Перевод организации") == []


def test_category_search(test_df2):
    assert category_search(test_df2, ["Перевод организации",
                                      "Перевод со счета на счет"]) == ['Перевод организации 1',
                                                                       'Перевод со счета на счет 1']
    assert category_search(test_df2, ["fff"]) == ['fff 0']

    assert category_search(test_df2) == []
