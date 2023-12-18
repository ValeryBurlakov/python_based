# На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# 📌 Напишите 3-7 тестов unittest для данного класса.

class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        if width:
            self.width = width
        else:
            self.width = length

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

    def __eq__(self, other):
        return self.width == other.width and self.length == other.length

    def __lt__(self, other):
        return self.square() < other.square()

    def __le__(self, other):
        return self.square() <= other.square()

    # def __gt__(self, other):
    #     return self.square() > other.square()