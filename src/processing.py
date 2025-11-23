from datetime import datetime


def filter_by_state(data, state='EXECUTED'):
    """Фильтрует словари в списке по значению поля 'state'."""
    return [item for item in data if item.get('state') == state]


def sort_by_date(data, reverse=True):
    """Сортирует список словарей по полю 'date' (ISO-формат), по умолчанию — в обратном порядке."""
    return sorted(data, key=lambda x: datetime.fromisoformat(x['date']), reverse=reverse)
