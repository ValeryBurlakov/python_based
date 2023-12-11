# Доработаем задачу 1.
# 📌 Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

from collections import deque
import json
import time

class Factorial:
    def __init__(self, k: int):
        self.memory = deque(maxlen=k)

    def __call__(self, number, *args, **kwargs):
        result = number
        for mult in range(2, number):
            result *= mult
        self.memory.append({number: result})
        return self.memory[-1]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        dict_result = {}
        # while self.memory:
        #     dict_result.update(self.memory.popleft())
        for cur_dict in self.memory:
            dict_result.update(cur_dict)
        with open(f'{int(time.time())}.json', 'w', encoding='utf-8') as f_write:
            json.dump(dict_result, f_write, indent=2)

    def print_memory(self):
        return self.memory




factorial1 = Factorial(3)
print(factorial1(5))
print(factorial1.print_memory())
print(factorial1(7))
print(factorial1.print_memory())
print(factorial1(6))
print(factorial1.print_memory())
print(factorial1(4))
print(factorial1.print_memory())
with factorial1 as f:
    f(5)
