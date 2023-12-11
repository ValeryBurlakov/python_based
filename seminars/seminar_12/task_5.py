# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.


class Rectangle:
    __slots__ = ('_length', '_width')

    def __init__(self, length, width=None):
        self._length = length
        if width:
            self._width = width
        else:
            self._width = length

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value > 0:
            self._length = value
        else:
            raise ValueError(f'длина должна быть положительной')

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError(f'ширина должна быть положительной')

    def __repr__(self):
        return f'rectangle({self.length}, {self._width})'

    # def perimetr(self):
    #     return 2 * (self.length + self.width)
    #
    # def square(self):
    #     return self.width * self.length
    #
    # def __add__(self, other):
    #     perimeter = self.perimetr() + other.perimetr()
    #     width = self.width + other.width
    #     length = (perimeter / 2) - width  # получили длину
    #     # print(length, self.length + other.length)
    #     return Rectangle(width, length)
    #
    # def __sub__(self, other):
    #     if self.perimetr() < other.perimetr():
    #         self, other = other, self
    #     if self.width > self.length:
    #         self.width, self.length = self.length, self.width
    #     if other.width > other.length:
    #         other.width, other.length = other.length, other.width
    #     perimeter = self.perimetr() - other.perimetr()
    #     width = self.width - other.width
    #     length = (perimeter / 2) - width  # получили длину
    #     return Rectangle(width, length)

c1 = Rectangle(6, 3)
c2 = Rectangle(3, 5)

c1.length = 8
c2.width = 9
print(c1.length)
print(c2.width)
print(c1.__repr__())