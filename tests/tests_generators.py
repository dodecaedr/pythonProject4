from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency():
    transactions = [
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
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
    # Тест 1: Фильтрация по USD
    usd_result = list(filter_by_currency(transactions, 'USD'))
    assert len(usd_result) == 3, 'Должно быть 3 транзакции в USD'

    for item in usd_result:
        assert item['operationAmount']['currency']['code'] == 'USD'

    # Тест 2: Фильтрация по RUB
    rub_result = list(filter_by_currency(transactions, 'RUB'))
    assert len(rub_result) == 2, 'Должно быть 2 транзакции в RUB'
    for item in rub_result:
        assert item['operationAmount']['currency']['code'] == 'RUB'

    # Тест 3: Фильтрация по несуществующей валюте (например EUR)
    eur_result = list(filter_by_currency(transactions, 'EUR'))
    assert len(eur_result) == 0, 'Не должно быть транзакций в EUR'

    # Тест 4: Пустой список транзакций
    empty_result = list(filter_by_currency([], 'USD'))
    assert len(empty_result) == 0, 'Пустой список должен дать пустой результат'

    # Тест 5: Транзакция без поля currency
    partial_tx = [
        {
            'id': 1,
            'operationAmount': {}  # Нет поля currency
        }
    ]
    partial_result = list(filter_by_currency(partial_tx, 'USD'))
    assert len(partial_result) == 0, 'Транзакция без currency не должна попасть в результат'


def test_transaction_descriptions():
    transactions = [
        {"description": "Кофе"},
        {"description": "Чай"},
        {},
        {"description": "Булочка"},
    ]

    result = list(transaction_descriptions(transactions))

    expected = ["Кофе", "Чай", None, "Булочка"]

    assert result == expected


def test_card_number_generator():
    # Тест 1: числа от 1 до 3
    result1 = list(card_number_generator(1, 3))
    expected1 = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003"
    ]
    assert result1 == expected1

    # Тест 2: одно число (42)
    result2 = list(card_number_generator(42, 42))
    expected2 = ["0000 0000 0000 0042"]
    assert result2 == expected2

    # Тест 3: большие числа (почти максимум)
    result3 = list(card_number_generator(9999999999999998, 9999999999999999))
    expected3 = [
        "9999 9999 9999 9998",
        "9999 9999 9999 9999"
    ]
    assert result3 == expected3
