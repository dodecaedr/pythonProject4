from pytest import mark

from src.masks import get_mask_account, get_mask_card_number


@mark.parametrize('card, mask', [
       ('7000792289606361', '7000 79** **** 6361'),
       ('7600924456123', '7600 92** **** 6123'),
       ('430000000000077722', '4300 00** **** 7722'),
       ('', 'Некорректный номер карты'),
])
def test_get_mask_card_number(card, mask):
    assert get_mask_card_number(card) == mask


def test_get_mask_account(fix_get_mask_account):
    assert get_mask_account(fix_get_mask_account) == '**4305'


def test_get_mask_account_empty(fix_get_mask_account_empty):
    assert get_mask_account(fix_get_mask_account_empty) == 'Вы ничего не ввели'