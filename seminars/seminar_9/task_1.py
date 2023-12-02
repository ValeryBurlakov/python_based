# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# 📌 Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

from random import randint
from typing import Callable


def outer_func(num: int, count: int) -> Callable[[], None]:
    def inner_func():
        for i in range(1, count + 1):
            print(f"Попытка {i}")
            guess_number = int(input("Введите число: "))
            if guess_number == num:
                print(f"Вы угадали, число равно {guess_number}")
                return
            elif guess_number > num:
                print("Число больше загаданного")
            elif guess_number < num:
                print("Число меньше загаданного")

    return inner_func




if __name__ == '__main__':
    number = outer_func(randint(1, 100), randint(1, 10))
    number()
