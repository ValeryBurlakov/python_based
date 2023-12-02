# Создайте декоратор с параметром.
# 📌 Параметр - целое число, количество запусков декорируемой
# функции.
from typing import Callable

def counter(num: int = 1):
    def deco(func: Callable) -> Callable:
        list_res = []
        def wrapper(*args, **kwargs):
            for _ in range(num):
                result = func(*args, **kwargs)
                list_res.append(result)
            return list_res
        return wrapper
    return deco


if __name__ == '__main__':
    deco_func()