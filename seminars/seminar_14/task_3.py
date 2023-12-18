# Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери
# символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import unittest
from task_1 import del_sim


class TestFilterLower(unittest.TestCase):

    def test_no_change(self):
        self.assertEqual(del_sim('hello world'), 'hello world')

    def test_lower(self):
        self.assertEqual(del_sim('Hi pEoPlE'), 'hi people')

    def test_punctuation(self):
        self.assertEqual(del_sim('hello, my friend!'), 'hello my friend')

    def test_language(self):
        self.assertEqual(del_sim('hello друг'), 'hello ')

    def test_all(self):
        self.assertEqual(del_sim('HelLo, друГ!'), 'hello ')

# python3 -m unittest task_3.py -v  - запуск через терминал

if __name__ == '__main__':
    unittest.main(verbosity=2)
