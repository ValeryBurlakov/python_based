# Напишите для задачи 1 тесты pytest. Проверьте следующие
# варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери
# символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

from string import ascii_letters
from task_1 import del_sim
import pytest


def test_no_change():
    assert del_sim('hello world') == 'hello world'


def test_lower():
    assert del_sim('Hi pEoPlE') == 'hi people'


def test_punctuation():
    assert del_sim('hello, my friend!') == 'hello my friend'


def test_language():
    assert del_sim('hello друг') == 'hello '


def test_all():
    assert del_sim('HelLo, друГ!') == 'hello '


if __name__ == '__main__':
    pytest.main()
