# Разработайте программное обеспечение для ведения журнала событий.
# Вам необходимо создать класс, который будет представлять строки журнала и
# включать в себя информацию об авторе и времени создания каждой записи.
# Условие задачи:
# Создайте класс MyStr, который наследуется от встроенного класса str и
# добавлять дополнительную информацию о создателе строки и времени ее создания.
# Этот класс будет представлять строки с информацией о событиях.
# Класс MyStr должен иметь следующие атрибуты и методы:
# value (str): Строковое значение с описанием события.
# author (str): Имя автора, создавшего запись.
# time: Время создания записи в формате '%Y-%m-%d %H:%M'.
# Магические методы (Dunder-методы):
# Реализуйте метод __new__(cls, value, author), который создает новый объект класса MyStr с заданным value и author.
# Метод также автоматически фиксирует время создания записи. В этом методе создается новый объект MyStr
# с указанными атрибутами и текущим временем в атрибуте time.
# Реализуйте метод __str__(self), который возвращает строковое представление объекта класса MyStr
# с информацией о событии, авторе и времени создания.
# Реализуйте метод __repr__(self), который возвращает строковое представление объекта класса MyStr.
# Метод __repr__ возвращает строку, которая может быть использована для создания точно такого же объекта
# MyStrс теми же значениями valueиauthor`


import time


class MyStr(str):

    def __new__(cls, value: str, author: str):
        instance = super().__new__(cls, value)
        instance.author = author
        # instance.time = time.time()
        instance.time = time.strftime('%Y-%m-%d %H:%M', time.localtime())
        # print(f'Создал класс {cls}')
        # return f'{instance} (Автор: {instance.author}, Время создания: {instance.time})'

        return instance

    def __init__(self, value: str, author: str):
        self.value = value
        self.author = author

    def __str__(self):
        return f'{self.value} (Автор: {self.author}, Время создания: {self.time})'

    def __repr__(self):
        return f"MyStr('{self.value}', '{self.author}')"


# help(MyStr)
# my_text = MyStr('Моя жизнь тяжела', 'Вася')
# print(my_text, my_text.author, my_text.time)


event = MyStr("Завершилось тестирование", "John")
print(event)

# Пример текста (Автор: Иван, Время создания: 2023-10-10 15:56)
my_string = MyStr("Пример текста", "Иван")
print(my_string)

# MyStr('Мама мыла раму', 'Маршак')
my_string = MyStr("Мама мыла раму", "Маршак")
print(repr(my_string))
