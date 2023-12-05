# Создайте класс прямоугольник.
# 📌 Класс должен принимать длину и ширину при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие периметр
# и площадь.
# 📌 Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.


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


rectangle = Rectangle(5, 8)
rectangle_2 = Rectangle(5)
print(rectangle.perimetr(), rectangle.square(), sep='\n')
