from datetime import datetime


def filter_by_state(list_dictionary: list, state='EXECUTED') -> list:
    """ Фильтрация словарей по значению 'state' """
    list_clean = []  # Здесь будут храниться подходящие словари
    for dictionary in list_dictionary:
        if dictionary.get("state") == state:  # Проверяем значение поля "state"
            list_clean.append(dictionary)
    return list_clean


def sort_by_date(list_dictionary: list, ascending=False) -> list:
    """ Сортирует список словарей по дате """
    return sorted(list_dictionary, key=lambda d: datetime.fromisoformat(d["date"]), reverse=not ascending)


# Данные с одинарными кавычками
input_data = input()

# Преобразовываем одинарные кавычки в двойные
fixed_data = input_data.replace("'", '"')

# Преобразуем строку обратно в список словарей
user_dictionary = eval(fixed_data)

# Применяем фильтры и сортировку
filtered_executed = filter_by_state(user_dictionary)
sorted_descending = sort_by_date(filtered_executed)

# Вывод результатов
print("Отфильтрованные операции (только EXECUTED):")
print(filtered_executed)

print("\nОтсортированные операции (по убыванию):")
print(sorted_descending)

# [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]