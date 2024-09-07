from unittest.mock import patch
import pytest
import pandas as pd
from src.reading_files import transaction_excel, transaction_csv


@pytest.fixture
def test_df():
    test_dict = {
        "id": [650703.0, 3598919.0],
        "state": ["EXECUTED", "EXECUTED"],
        "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z"],
        "amount": [16210.0, 29740.0],
        "currency_name": ["Sol", "Peso"],
        "currency_code": ["PEN", "COP"],
        "from": ["Счет 58803664561298323391", "Discover 3172601889670065"],
        "to": ["Счет 39745660563456619397", "Discover 0720428384694643"],
        "description": ["Перевод организации", "Перевод с карты на карту"]
    }

    return pd.DataFrame(test_dict)


@patch('src.reading_files.pd.read_csv')
def test_transaction_csv(mock_read, test_df):
    mock_read.return_value = test_df
    expected = test_df.to_dict(orient='records')
    assert transaction_csv('C:/Users/User/PycharmProjects/homework/data/transactions.csv') == expected


def test_transaction_csv_with_incorrect_path():
    assert transaction_csv("") == []


@patch('src.reading_files.pd.read_excel')
def test_transaction_excel(mock_read, test_df):
    mock_read.return_value = test_df
    expected = test_df.to_dict(orient='records')
    assert transaction_excel('C:/Users/User/PycharmProjects/homework/data/transactions_excel.xlsx') == expected


def test_transaction_excel_with_incorrect_path():
    assert transaction_excel("") == []
