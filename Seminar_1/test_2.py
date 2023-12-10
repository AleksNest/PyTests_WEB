import pytest
from check_post import get_login, get_post_other, create_post, get_post_own




# проверка наличия определенного ID в ответе по запросу get
id_check = 91981
def test_1(token):
    out = get_post_other(token)['data']       # список словарей по ключу data Каждый словарь - это элемент списка
    res = []
    for item in out:
        res.append(item['id'])

    assert id_check in res


# проверка созданного поста по наименованию заголовка
title_check = 'Заголовок новый 2'
def test_2(token):
    create_post(token)
    out = get_post_own(token)['data']
    res = []
    for item in out:
        res.append(item['title'])

    assert title_check in res
