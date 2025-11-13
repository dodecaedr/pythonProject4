from typing import Any, Iterator


def filter_by_currency(transactions: list[dict[str, Any]], currency: str) -> Iterator[dict[str, Any]]:
    """Фильтрация транзакций по валюте"""
    return filter(lambda x: x.get('operationAmount', {}).get('currency', {}).get('code', '') == currency, transactions)


def transaction_descriptions(transactions: list[dict[str, Any]]) -> Iterator[str]:
    """Описание операций"""
    for transaction in transactions:
        yield transaction.get('description')
