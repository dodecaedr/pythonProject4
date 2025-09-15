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
    return sorted(list_dictionary, key=lambda d: datetime.fromisoformat(d.get("date")), reverse=reverse)


if __name__ == "__main__":
    test = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    # Данные с одинарными кавычками
    input_data = test

    # Применяем фильтры и сортировку
    filtered_executed = filter_by_state(input_data)
    sorted_descending = sort_by_date(filtered_executed)

    # Вывод результатов
    print("Отфильтрованные операции (только EXECUTED):")
    print(filtered_executed)

    print("\nОтсортированные операции (по убыванию):")
    print(sorted_descending)
