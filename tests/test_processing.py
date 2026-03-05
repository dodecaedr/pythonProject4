import pytest

from src.processing import sort_by_date, filter_by_state


def test_filter_by_state_default():
    """Фильтрация по умолчанию (state='EXECUTED')"""
    data = [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "CANCELED"}, {"id": 3, "state": "EXECUTED"}]
    result = filter_by_state(data)
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_by_state_custom_state():
    """Фильтрация по другому state"""
    data = [{"id": 1, "state": "PENDING"}, {"id": 2, "state": "CANCELED"}, {"id": 3, "state": "PENDING"}]
    result = filter_by_state(data, "PENDING")
    assert len(result) == 2
    assert all(item["state"] == "PENDING" for item in result)


def test_filter_by_state_no_matches():
    """Нет совпадений по state"""
    data = [{"id": 1, "state": "CANCELED"}]
    result = filter_by_state(data, "EXECUTED")
    assert result == []


def test_filter_by_state_empty_list():
    """Пустой входной список"""
    result = filter_by_state([])
    assert result == []


def test_filter_by_state_missing_state_key():
    """Элемент без ключа 'state'"""
    data = [{"id": 1}, {"id": 2, "state": "EXECUTED"}]  # нет 'state'
    result = filter_by_state(data)
    assert len(result) == 1
    assert result[0]["id"] == 2


def test_sort_by_date_desc():
    """Сортировка по убыванию (reverse=True)"""
    data = [
        {"id": 1, "date": "2020-01-03T00:00:00"},
        {"id": 2, "date": "2020-01-01T00:00:00"},
        {"id": 3, "date": "2020-01-02T00:00:00"},
    ]
    result = sort_by_date(data)
    assert [item["id"] for item in result] == [1, 3, 2]


def test_sort_by_date_asc():
    """Сортировка по возрастанию (reverse=False)"""
    data = [
        {"id": 1, "date": "2020-01-03T00:00:00"},
        {"id": 2, "date": "2020-01-01T00:00:00"},
        {"id": 3, "date": "2020-01-02T00:00:00"},
    ]
    result = sort_by_date(data, reverse=False)
    assert [item["id"] for item in result] == [2, 3, 1]


def test_sort_by_date_empty_list():
    """Пустой список"""
    result = sort_by_date([])
    assert result == []


def test_sort_by_date_single_item():
    """Один элемент"""
    data = [{"id": 1, "date": "2020-01-01T00:00:00"}]
    result = sort_by_date(data)
    assert result == data


def test_sort_by_date_invalid_date_format():
    """Некорректный формат даты → ValueError"""
    data = [{"id": 1, "date": "not-a-date"}]
    with pytest.raises(ValueError):
        sort_by_date(data)


def test_sort_by_date_missing_date_key():
    """Отсутствует ключ 'date' → KeyError"""
    data = [{"id": 1}]
    with pytest.raises(KeyError):
        sort_by_date(data)
