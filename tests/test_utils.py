import pytest


from utils import get_data


def test_get_date(test_url):
    """
    Проверки:
    1 - список не пуст
    2 - подключение к несуществубщему адресу
    3 - невозможность перевести в json
    4 - неправильный адрес
    """
    assert len(get_data(test_url)[0]) > 0
    assert get_data("https://wrong.url.com")[0] is None
    assert get_data("https://github.com/Kopjuk/test_develop")[0] is None
    assert get_data("https://github.com/Kopjuk/test_develope")[0] is None

def test_get_filtered_data():
    get_filtered_data