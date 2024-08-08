import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "entrance ,result",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Visa Platinum 7000 7922 8960 6361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 7365 4108 4301 3587 4305", "Счет **4305"),
    ],
)
def test_mask_account_card(entrance, result):
    assert mask_account_card(entrance) == result


@pytest.mark.parametrize(
    "date ,result_date",
    [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2023-12-12", "12.12.2023"), ("2020-11-10", "10.11.2020")],
)
def test_get_date(date, result_date):
    assert get_date(date) == result_date
