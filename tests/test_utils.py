import pytest

from utils import get_data, get_filtered_data, get_lats_values, get_formatted_data


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


def test_get_filtered_data(test_data):
    """
    Проверяем филтрацию
    1 количество данных = 5
    2 количество отфильтрованых данных с отправителем = 4
    """
    assert len(get_filtered_data(test_data)) == 4
    assert len(get_filtered_data(test_data, filtered_empty_from=True)) == 3


def test_get_lats_values(test_data):
    """
    Проверяем сортировку по дате
    """
    data = get_lats_values(test_data, 4)
    assert data[0]["date"] == '2020-07-03T18:35:29.512364'
    assert len(data) == 4


def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data)
    assert data == ['26.08.2019 Перевод организации\nMaestro 1596 83** **** 5 -> Счет **9589\n31957.58 руб.', '03.07.2020 Перевод организации\nMasterCard 7158 30** **** 6 -> Счет **5560\n8221.37 USD', '30.06.2018 Перевод организации\nСчет 7510 68** **** 6 -> Счет **6702\n9824.07 USD', '23.03.2018 Открытие вклада\n  -> Счет **2431\n48223.05 руб.', '04.04.2019 Перевод со счета на счет\nСчет 1970 86** **** 8 -> Счет **4188\n79114.93 USD']

