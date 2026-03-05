from typing import Any, Iterator, Union


def filter_by_currency(transactions: list[dict[str, Any]], currency: str) -> Iterator[dict[str, Any]]:
    """Фильтрация транзакций по валюте"""
    return filter(lambda x: x.get("operationAmount", {}).get("currency", {}).get("code", "") == currency, transactions)


def transaction_descriptions(transactions: list[dict[str, Any]]) -> Iterator[Union[str, None]]:
    """Описание операций"""
    for transaction in transactions:
        yield transaction.get("description")  # возвращает None, если ключа нет


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генератор номеров банковских карт"""
    if start < 0:
        print("Начальное значение должно быть >= 1")
        return
    if end > 9999999999999999:
        print("Конечное значение не может превышать 9999999999999999")
        return
    if start > end:
        print("Начальное значение не может быть больше конечного")
        return

    for num in range(start, end + 1):
        num_str = f"{num:016d}"  # Превращаем число в строку и дополняем нулями слева до 16 символов
        formatted = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:16]}"  # Разбиваем на группы по 4 цифры и соединяем пробелами
        yield formatted
