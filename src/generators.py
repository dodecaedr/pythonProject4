from typing import Any, Iterator


def filter_by_currency(transactions: list[dict[str, Any]], currency: str) -> Iterator[dict[str, Any]]:
    """Фильтрация транзакций по валюте"""
    return filter(lambda x: x.get('operationAmount', {}).get('currency', {}).get('code', '') == currency, transactions)
