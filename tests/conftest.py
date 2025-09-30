import pytest


@pytest.fixture
def fix_get_mask_account_empty() -> str:  # masks
    return ""


@pytest.fixture
def fix_get_mask_account() -> str:  # masks
    return "73654108430135874305"


@pytest.fixture
def fix_get_mask_card_number_empty() -> str:  # masks
    return ""


@pytest.fixture
def fix_sort_by_date() -> list:  # processing
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]


@pytest.fixture
def fix_sort_by_date_other() -> list:  # processing
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12"},
    ]


@pytest.fixture
def fix_sort_by_date_empty() -> list:  # processing
    return [{}]


@pytest.fixture
def fix_get_date() -> str:  # widget
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def fix_get_date_other() -> str:  # widget
    return "2024-03-11"


@pytest.fixture
def fix_get_date_empty() -> str:  # widget
    return ""


@pytest.fixture
def fix_get_date_error() -> str:  # widget
    return "24-03-11"
