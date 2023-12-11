# Разработайте программу для работы с прямоугольниками. Необходимо создать класс
# Rectangle, который будет представлять прямоугольник с заданными шириной и высотой.
#
# Атрибуты класса:
#
# width (int): Ширина прямоугольника. height (int): Высота прямоугольника.
#
# Методы класса:
#
# __init__(self, width, height=None): Конструктор класса. Принимает ширину и высоту прямоугольника.
# Если высота не указана (по умолчанию None), то считается, что прямоугольник является квадратом,
# и высота устанавливается равной ширине.
#
# perimeter(self): Метод для вычисления периметра прямоугольника. Возвращает целое число -
# значение периметра.
#
# area(self): Метод для вычисления площади прямоугольника. Возвращает целое число - значение площади.
#
# __add__(self, other): Магический метод, который определяет операцию сложения
# (+) для двух прямоугольников. Принимает другой прямоугольник other.
# Создает новый прямоугольник, который представляет собой объединение исходных прямоугольников
# по периметру. Новая ширина и высота вычисляются также на основе объединения.
# Возвращает новый прямоугольник.
#
# __sub__(self, other): Магический метод, который определяет операцию вычитания
# (-) одного прямоугольника из другого. Принимает вычитаемый прямоугольник other.
# Создает новый прямоугольник, представляющий разницу периметров исходных прямоугольников,
# и вычисляет высоту на основе этой разницы. Новая ширина вычисляется также на основе разницы.
# Возвращает новый прямоугольник.
#
# __lt__(self, other): Магический метод, который определяет операцию "меньше" (<)
# для двух прямоугольников. Принимает другой прямоугольник other. Возвращает True,
# если площадь первого прямоугольника меньше площади второго, иначе False.
#
# __eq__(self, other): Магический метод, который определяет операцию "равно" (==)
# для двух прямоугольников. Принимает другой прямоугольник other. Возвращает True,
# если площади равны, иначе False.
#
# __le__(self, other): Магический метод, который определяет операцию "меньше или равно" (<=)
# для двух прямоугольников. Принимает другой прямоугольник other. Возвращает True,
# если площадь первого прямоугольника меньше или равна площади второго, иначе False.
#
# __str__(self): Магический метод, возвращающий строковое представление прямоугольника.
# Возвращает строку, описывающую ширину и высоту прямоугольника в виде:
# Прямоугольник со сторонами 2 и 3,
# где первое число - это ширина, а второе - высота.
#
# __repr__(self): Магический метод, возвращающий строковое представление прямоугольника,
# которое может быть использовано для создания нового объекта такого же класса с теми же атрибутами.
#
# Пояснение:
#
# Метод __add__ объединяет два прямоугольника по периметру и создает новый прямоугольник.
# Метод __sub__ вычитает один прямоугольник из другого, представляя разницу периметров
# исходных прямоугольников, и создает новый прямоугольник.
# Методы сравнения __lt__, __eq__ и __le__ сравнивают прямоугольники по их площади.
# Методы __str__ и __repr__ предоставляют строковое представление объекта класса Rectangle.


class Rectangle:

    def __init__(self, width: int, height: int):
        if width <= height:
            self.length = width
            self.width = height
        else:
            self.length = height
            self.width = width

    def perimeter(self):
        return int(2 * (self.length + self.width))

    def area(self):
        return self.width * self.length

    def __add__(self, other):
        perimeter = self.perimeter() + other.perimeter()
        width = self.width + other.width
        length = (perimeter / 2) - width  # получили длину
        # print(length, self.length + other.length)
        return Rectangle(int(width), int(length))

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        if self.width > self.length:
            self.width, self.length = self.length, self.width
        if other.width > other.length:
            other.width, other.length = other.length, other.width
        perimeter = self.perimeter() - other.perimeter()
        length = int(self.width - other.width)
        width = int((perimeter / 2) - length)  # получили длину
        return Rectangle(width, length)

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f'Прямоугольник со сторонами {self.length} и {self.width}'

    def __repr__(self):
        return f'Rectangle({self.width}, {self.length})'

    # def __gt__(self, other):
    #     return self.square() > other.square()


# rectangle = Rectangle(6, 3)
# rectangle_2 = Rectangle(3, 5)
# c3 = rectangle + rectangle_2
# c4 = rectangle - rectangle_2
# print(f'{rectangle < rectangle_2 = }, {rectangle > rectangle_2= }, {rectangle == rectangle_2 = }, '
#       f'{rectangle != rectangle_2 = }, {rectangle <= rectangle_2 = }, {rectangle >= rectangle_2= }')
# print(c3.square(), c3.perimetr(), sep='\n')
# print(c4.square(), c4.perimetr(), sep='\n')
# # print(rectangle.perimetr(), rectangle.square(), sep='\n')

# rect1 = Rectangle(5, 10)
# rect2 = Rectangle(3, 7)
#
# print(f"Периметр rect1: {rect1.perimeter()}")
# print(f"Площадь rect2: {rect2.area()}")
# print(f"rect1 < rect2: {rect1 < rect2}")
# print(f"rect1 == rect2: {rect1 == rect2}")
# print(f"rect1 <= rect2: {rect1 <= rect2}")
#
# rect3 = rect1 + rect2
# print(f"Периметр rect3: {rect3.perimeter()}")
# rect4 = rect1 - rect2
# print(f"Ширина rect4: {rect4.width}")
# print(repr(rect1))
# print(rect4)


rect1 = Rectangle(4, 5)
rect2 = Rectangle(3, 3)

print(rect1)
print(rect2)

print(rect1.perimeter())
print(rect1.area())
print(rect2.perimeter())
print(rect2.area())

rect_sum = rect1 + rect2
rect_diff = rect1 - rect2

print(rect_sum)
print(rect_diff)

print(rect1 < rect2)
print(rect1 == rect2)
print(rect1 <= rect2)

print(repr(rect1))
print(repr(rect2))