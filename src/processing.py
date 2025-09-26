from datetime import datetime


def filter_by_state(list_dictionary: list, state: str = "EXECUTED") -> list:
    """Фильтрация словарей по значению 'state'"""
    list_clean = []  # Здесь будут храниться подходящие словари
    for dictionary in list_dictionary:
        if dictionary.get("state") == state:  # Проверяем значение поля "state"
            list_clean.append(dictionary)
    return list_clean


def sort_by_date(list_dictionary: list, reverse: bool = True) -> list:
    """Сортирует список словарей по дате"""
    if list_dictionary == {}:
        return []
    return sorted(list_dictionary, key=lambda d: datetime.fromisoformat(d.get("date")), reverse=reverse)
