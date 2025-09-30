from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_string: str) -> str:
    """Маскировка карт и счетов"""
    # Проверка на пустую строку или только пробелы
    if not info_string or not info_string.strip():
        return ""

    parts = info_string.split()
    if len(parts) < 2:
        return ""

    number = parts[-1]
    name = " ".join(parts[:-1])

    # Очищаем номер от нецифровых символов
    clean_number = "".join(filter(str.isdigit, number))

    # Определяем тип по названию
    if name.lower() == "счет":
        masked = get_mask_account(clean_number)
        if "Некорректный" not in masked:
            return f"{name} {masked}"

    else:  # Карта или другое
        masked = get_mask_card_number(clean_number)
        if "Некорректный" not in masked:
            return f"{name} {masked}"

    # Автоопределение по длине номера (если по названию не определилось)
    if len(clean_number) == 16:
        masked = get_mask_card_number(clean_number)
        if "Некорректный" not in masked:
            return f"{name} {masked}"
    elif len(clean_number) >= 4:
        masked = get_mask_account(clean_number)
        if "Некорректный" not in masked:
            return f"{name} {masked}"

    return ""


def get_date(date_string: str) -> str:
    """Преобразует дату из формата '2024-03-11T02:26:18.671407'в 'ДД.ММ.ГГГГ'"""
    try:
        # Парсим дату с помощью datetime
        dt: datetime = datetime.fromisoformat(date_string.replace("Z", "+00:00"))

        # Форматируем в нужный формат
        return dt.strftime("%d.%m.%Y")

    except (ValueError, TypeError, AttributeError):
        # Обрабатываем все возможные ошибки парсинга
        return ""
