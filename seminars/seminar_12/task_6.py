# Изменяем класс прямоугольника.
# 📌 Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.

class Range:
    def __init__(self):
        pass

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    @staticmethod
    def validate(value):
        if value <= 0:
            raise ValueError('значение должно быть больше нуля')


class Rectangle:
    width = Range()
    length = Range()

    def __init__(self, length, width=None):
        self._length = length
        if width:
            self._width = width
        else:
            self._width = length

    def __repr__(self):
        return f'rectangle({self.length}, {self._width})'

    def perimetr(self):
        return 2 * (self.length + self.width)

    def square(self):
        return self.width * self.length

    def __add__(self, other):
        perimeter = self.perimetr() + other.perimetr()
        width = self.width + other.width
        length = (perimeter / 2) - width  # получили длину
        # print(length, self.length + other.length)
        return Rectangle(width, length)

    def __sub__(self, other):
        if self.perimetr() < other.perimetr():
            self, other = other, self
        if self.width > self.length:
            self.width, self.length = self.length, self.width
        if other.width > other.length:
            other.width, other.length = other.length, other.width
        perimeter = self.perimetr() - other.perimetr()
        width = self.width - other.width
        length = (perimeter / 2) - width  # получили длину
        return Rectangle(width, length)


c1 = Rectangle(6, 3)
c2 = Rectangle(3, 5)

c1.length = 8
c2.width = 9
print(c1.length)
print(c2.width)
print(c1.__repr__())
