import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card, mask_card",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счёт 73654108430135874305", "Счёт **4305"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("", ""),
    ],
)
def test_mask_account_card(card: str, mask_card: str) -> None:
    assert mask_account_card(card) == mask_card


def test_get_date(fix_get_date: str) -> None:
    assert get_date(fix_get_date) == "11.03.2024"


def test_get_date_empty(fix_get_date_empty: str) -> None:
    assert get_date(fix_get_date_empty) == ""


def test_get_date_other(fix_get_date_other: str) -> None:
    assert get_date(fix_get_date_other) == "11.03.2024"
