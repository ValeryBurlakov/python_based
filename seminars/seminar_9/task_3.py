# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# 📌 Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# 📌 Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# 📌 Имя файла должно совпадать с именем декорируемой
# функции.

from pathlib import Path
import json
from typing import Callable


def my_logger(func: Callable) -> Callable:
    file = Path(f'{func.__name__}.json')
    if file.is_file():
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []

    def wrapper(*args, **kwargs):
        dict_json = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        dict_json['result'] = result
        data.append(dict_json)

        with open(file, 'w', encoding='utf-8') as f_write:
            json.dump(data, f_write)
        return result

    return wrapper


@my_logger
def get_all( *args: list, **kwargs) -> int:
    return sum(args)


if __name__ == '__main__':
    get_all(42, 6, x="2", z=True, f="bv")
