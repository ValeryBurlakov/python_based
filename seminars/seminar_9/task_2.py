# Дорабатываем задачу 1.
# 📌 Превратите внешнюю функцию в декоратор.
# 📌 Он должен проверять входят ли переданные в функцию-
# угадайку числа в диапазоны [1, 100] и [1, 10].
# 📌 Если не входят, вызывать функцию со случайными числами
# из диапазонов.

from random import randint
from typing import Callable


def number_control(func: Callable) -> Callable:
    low_num = 1
    up_num = 100
    low_count = 1
    up_count = 10

    def wrapper(num: int, count: int):
        if not low_num <= num <= up_num:
            num = randint(low_num, up_num)
        if not low_count <= count <= up_count:
            count = randint(low_count, up_count)
        result = func(num, count)
        return result

    return wrapper


@number_control
def guessing_game(num, count):
    for i in range(1, count + 1):
        print(f"Попытка {i}")
        guess_number = int(input("Введите число: "))
        if guess_number == num:
            print(f"Вы угадали, число равно {guess_number}")
            break
        elif guess_number > num:
            print("Число больше загаданного")
        elif guess_number < num:
            print("Число меньше загаданного")


if __name__ == '__main__':
    number = guessing_game(42, 6)
