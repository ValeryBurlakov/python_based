# Доработайте прошлую задачу добавив декоратор wraps в
# каждый из декораторов.
from functools import wraps
from typing import Callable
import json
from random import randint
from pathlib import Path




def counter(num: int = 1):
    def deco(func: Callable) -> Callable:
        list_res = []
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                result = func(*args, **kwargs)
                list_res.append(result)
            return list_res

        return wrapper

    return deco


def number_control(func: Callable) -> Callable:
    low_num = 1
    up_num = 100
    low_count = 1
    up_count = 10

    @wraps(func)
    def wrapper(num: int, count: int):
        if not low_num <= num <= up_num:
            num = randint(low_num, up_num)
        if not low_count <= count <= up_count:
            count = randint(low_count, up_count)
        result = func(num, count)
        return result

    return wrapper


def my_logger(func: Callable) -> Callable:
    file = Path(f'{func.__name__}.json')
    if file.is_file():
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []

    @wraps(func)
    def wrapper(*args, **kwargs):
        dict_json = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        dict_json['result'] = result
        data.append(dict_json)

        with open(file, 'w', encoding='utf-8') as f_write:
            json.dump(data, f_write, ensure_ascii=False, indent=2)
        return result

    return wrapper


@counter(2)
@number_control
@my_logger
def guessing_game(num, count):
    """Угадай число"""
    for i in range(1, count + 1):
        print(f"Попытка {i}")
        guess_number = int(input("Введите число: "))
        if guess_number == num:
            print(f"Вы угадали, число равно {guess_number}")
            return f'Число отгадано, {num=}'
        elif guess_number > num:
            print("Число больше загаданного")
        elif guess_number < num:
            print("Число меньше загаданного")
    else:
        return f'Число не отгадано, {num=}'


if __name__ == '__main__':
    guessing_game(1234, 23)
    print(guessing_game.__name__)
    print(guessing_game.__doc__)
    # help(guessing_game)