# площадь круга и дли на окружности
import math
import decimal


PI = decimal.Decimal(math.pi)

diameter = decimal.Decimal(input("введите диаметр окружности: "))
area = PI * (diameter/2)**2
length = PI * diameter

print(f'Площадь круга = {area=}\n длина его окружности = {length=}')

