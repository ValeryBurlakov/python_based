class NegativeValueError(Exception):
    pass


class Rectangle:

    def __init__(self, width, height=None):
        self.set_width(width)
        if height is None:
            self.set_height(width)
        else:
            self.set_height(height)

    def set_width(self, width):
        if width < 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self.width = width

    def set_height(self, height):
        if height < 0:
            raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"


c1 = Rectangle(6, 3)
c2 = Rectangle(3, 5)

c1.length = 8
c2.width = 9
print(c1.length)
print(c2.width)
print(c1.__repr__())