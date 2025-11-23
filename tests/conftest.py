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
