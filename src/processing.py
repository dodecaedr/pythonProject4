from datetime import datetime
from typing import List, Dict, Any


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует словари в списке по значению поля 'state'."""
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Сортирует список словарей по полю 'date' (ISO-формат), по умолчанию — в обратном порядке."""

    def get_date(item: Dict[str, Any]) -> datetime:
        # При обращении к item["date"] будет выброшен KeyError, если ключа нет
        date_str = item["date"]
        try:
            return datetime.fromisoformat(date_str)
        except ValueError as e:
            raise ValueError(f"Некорректный формат даты в элементе: {item}. Ошибка: {e}")

    return sorted(data, key=get_date, reverse=reverse)
