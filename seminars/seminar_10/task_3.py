# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# 📌 У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# 📌 Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

class Person:

    def __init__(self, name: str, surname: str, patronymic: str, age: int):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self._age = age

    def birthday(self):
        self._age += 1

    def full_name(self):
        return f'{self.name} {self.surname} {self.patronymic}'

    def get_age(self):
        return self._age


vasya_1 = Person('Vasya', 'Pupkin', 'Andreevich', 24)

# vasya_1.birthday()
# vasya_1.birthday()
# print(vasya_1.get_age())
# print(vasya_1.full_name())
