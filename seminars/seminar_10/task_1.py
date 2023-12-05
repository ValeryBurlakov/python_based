# Создайте класс окружность.
# 📌 Класс должен принимать радиус окружности при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

class Circle:
    def __init__(self, radius):
        self.radius = radius


    def perimetr(self):
        return 2 * 3.14 * self.radius

    def square(self):
        return 3.14 * self.radius**2


c = Circle(3)
print(c.square(), c.perimetr(), sep='\n')
