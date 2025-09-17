def get_mask_card_number(card: str) -> str:
    """Маскировка номера карты в формате XXXX XX** **** XXXX"""
    clean_card: str = "".join(filter(str.isdigit, card))
    card_length: int = len(clean_card)

    if card_length == 16:
        first_part: str = clean_card[:4]
        second_part: str = clean_card[4:6]
        last_part: str = clean_card[-4:]
        return f"{first_part} {second_part}** **** {last_part}"

    return "Некорректный номер карты"


def get_mask_account(count: str) -> str:
    """Маскировка номера счёта в формате **XXXX"""
    clean_count: str = "".join(filter(str.isdigit, count))
    count_length: int = len(clean_count)

    if count_length >= 4:
        last_four: str = clean_count[-4:]
        return f"**{last_four}"

    return "Некорректный номер счёта"


# 7000792289606361
# 73654108430135874305
