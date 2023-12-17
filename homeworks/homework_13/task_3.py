# В организации есть два типа людей: сотрудники и обычные люди. Каждый человек
# (и сотрудник, и обычный) имеет следующие атрибуты:
#
# Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая)
# Возраст (целое положительное число) Сотрудники имеют также уникальный идентификационный номер (ID),
# который должен быть шестизначным положительным целым числом.
#
# Ваша задача:
# Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях
# (Фамилия, Имя, Отчество, Возраст). Класс должен проверять валидность входных данных и
# генерировать исключения InvalidNameError и InvalidAgeError, если данные неверные.
#
# Создать класс Employee, который будет наследовать класс Person и
# добавлять уникальный идентификационный номер (ID). Класс Employee также должен
# проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.
# Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
# Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника
# на основе суммы цифр в его ID (по остатку от деления на 7).
# Создать несколько объектов класса Person и Employee с разными данными и проверить,
# что исключения работают корректно при передаче неверных данных.


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


class Employee(Person):
    MAX_LEVEL = 7

    def __init__(self, name: str, surname: str, patronymic: str, age: int, id: int):
        super().__init__(name, surname, patronymic, age)
        if 100_000 <= id < 1_000_000:
            self.id = id
        else:
            self.id = 100_000

    def get_level(self):
        sum_num = sum(int(num) for num in str(self.id))
        return sum_num % self.MAX_LEVEL


new_employee = Employee('Vasya', 'Pupkin', 'Andreevich', 24, 102_342)
print(new_employee.full_name())
print(new_employee.get_level())