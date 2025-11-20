import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions():
    """Список транзакций для тестирования (разные случаи: есть/нет currency, description)."""
    return [
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "A"},
        {"operationAmount": {"currency": {"code": "RUB"}}, "description": "B"},
        {"operationAmount": {}},  # нет currency
        {"description": "C"},  # нет operationAmount
    ]


@pytest.fixture
def card_ranges():
    """Диапазоны для тестирования генерации номеров карт (малый и близкий к максимуму)."""
    return [(1, 2), (9999999999999998, 9999999999999999)]


@pytest.mark.parametrize("currency, expected_count", [("USD", 1), ("RUB", 1), ("EUR", 0)])
def test_filter_by_currency(transactions, currency, expected_count):
    """Проверяет фильтрацию транзакций по коду валюты."""
    result = list(filter_by_currency(transactions, currency))
    assert len(result) == expected_count
    for item in result:
        assert item["operationAmount"]["currency"]["code"] == currency


def test_filter_empty():
    """Проверяет обработку пустого списка в filter_by_currency."""
    assert list(filter_by_currency([], "USD")) == []


def test_transaction_descriptions(transactions):
    """Проверяет извлечение description из транзакций (включая отсутствующие поля)."""
    result = list(transaction_descriptions(transactions))
    assert result == ["A", "B", None, "C"]


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
        (9999999999999998, 9999999999999999, ["9999 9999 9999 9998", "9999 9999 9999 9999"]),
    ],
)
def test_card_generator(start, end, expected):
    """Проверяет генерацию номеров карт в заданных диапазонах."""
    result = list(card_number_generator(start, end))
    assert result == expected


def test_filter_by_currency_detailed():
    """Полный тест filter_by_currency на полных данных транзакций."""
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]

    # Тест 1: Фильтрация по USD
    usd_result = list(filter_by_currency(transactions, "USD"))
    assert len(usd_result) == 3
    for item in usd_result:
        assert item["operationAmount"]["currency"]["code"] == "USD"

    # Тест 2: Фильтрация по RUB
    rub_result = list(filter_by_currency(transactions, "RUB"))
    assert len(rub_result) == 2
    for item in rub_result:
        assert item["operationAmount"]["currency"]["code"] == "RUB"

    # Тест 3: Фильтрация по несуществующей валюте (EUR)
    eur_result = list(filter_by_currency(transactions, "EUR"))
    assert len(eur_result) == 0

    # Тест 4: Транзакция без поля currency
    partial_tx = [{"id": 1, "operationAmount": {}}]  # Нет currency
    partial_result = list(filter_by_currency(partial_tx, "USD"))
    assert len(partial_result) == 0
