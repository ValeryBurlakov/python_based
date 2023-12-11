# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# 📌 Экземпляр должен запоминать последние k значений.
# 📌 Параметр k передаётся при создании экземпляра.
# 📌 Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.
from collections import deque


class Factorial:
    def __init__(self, k: int):
        self.memory = deque(maxlen=k)

    def __call__(self, number, *args, **kwargs):
        result = number
        for mult in range(2, number):
            result *= mult
        self.memory.append({number: result})
        return self.memory[-1]

    def print_memory(self):
        return self.memory


factorial1 = Factorial(3)
print(factorial1(5))
print(factorial1.print_memory())
print(factorial1(3))
print(factorial1.print_memory())
print(factorial1(6))
print(factorial1.print_memory())
print(factorial1(4))
print(factorial1.print_memory())
