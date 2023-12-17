# Добавьте в задачу Rectangle, которую писали ранее, исключение NegativeValueError,
# которое выбрасывается при некорректных значениях ширины и высоты, как при создании объекта,
# так и при установке их через сеттеры.


class Rectangle:
    """
    Класс, представляющий прямоугольник.

    Атрибуты:
    - width (int): ширина прямоугольника
    - height (int): высота прямоугольника

    Методы:
    - perimeter(): вычисляет периметр прямоугольника
    - area(): вычисляет площадь прямоугольника
    - __add__(other): определяет операцию сложения двух прямоугольников
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
    - __lt__(other): определяет операцию "меньше" для двух прямоугольников
    - __eq__(other): определяет операцию "равно" для двух прямоугольников
    - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
    - __str__(): возвращает строковое представление прямоугольника
    - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта
    """

    def __init__(self, width, height=None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Возвращает:
        - int: периметр прямоугольника
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Возвращает:
        - int: площадь прямоугольника
        """
        return self.width * self.height

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
        """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        Аргументы:
        - other (Rectangle): вычитаемый прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площади равны, иначе False
        """
        return self.area() == other.area()

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
        """
        return self.area() <= other.area()

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self.width}, {self.height})"


c1 = Rectangle(-6, 3)
c2 = Rectangle(3, 5)

c1.length = 8
c2.width = 9
print(c1.length)
print(c2.width)
print(c1.__repr__())




























# class Range:
#     def __init__(self):
#         pass
#
#     def __set_name__(self, owner, name):
#         self.param_name = '_' + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.param_name)
#
#     def __set__(self, instance, value):
#         self.validate(value)
#         setattr(instance, self.param_name, value)
#
#
# class Rectangle:

#     width = Range()
#     length = Range()
#
#     def __init__(self, length, width=None):
#         self._length = length
#         if width:
#             self._width = width
#         else:
#             self._width = length
#
#     def __repr__(self):
#         return f'rectangle({self.length}, {self._width})'
#
#     def perimetr(self):
#         return 2 * (self.length + self.width)
#
#     def square(self):
#         return self.width * self.length
#
#     def __add__(self, other):
#         perimeter = self.perimetr() + other.perimetr()
#         width = self.width + other.width
#         length = (perimeter / 2) - width  # получили длину
#         # print(length, self.length + other.length)
#         return Rectangle(width, length)
#
#     def __sub__(self, other):
#         if self.perimetr() < other.perimetr():
#             self, other = other, self
#         if self.width > self.length:
#             self.width, self.length = self.length, self.width
#         if other.width > other.length:
#             other.width, other.length = other.length, other.width
#         perimeter = self.perimetr() - other.perimetr()
#         width = self.width - other.width
#         length = (perimeter / 2) - width  # получили длину
#         return Rectangle(width, length)
#
#     def __eq__(self, other):
#         return self.square() == other.square()
#
#     def __lt__(self, other):
#         return self.square() < other.square()
#
#     def __le__(self, other):
#         return self.square() <= other.square()
#
#     # def __gt__(self, other):
#     #     return self.square() > other.square()