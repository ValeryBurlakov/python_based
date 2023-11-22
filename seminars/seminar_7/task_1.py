# функция которая заполняет файл случайными парами чисел.
# первуое число int второе - float разделены вертикальной чертой
# минимальное число - -1000 макси - +1000
# кол-во строк и имя файла передаются как аргументы функции

import random
from pathlib import Path

MIN_NUM = -1000
MAX_NUM = 1000

def fill_number(name: str | Path, rows: int):
    with open("numbers.txt", 'a', encoding='utf-8') as numbers:
        for _ in range(rows):
            num_int = random.randint(MIN_NUM, MAX_NUM)
            num_float = random.uniform(MIN_NUM, MAX_NUM)
            numbers.write(f'{num_int} | {num_float}\n')


if __name__ == '__main__':
    fill_number("numbers.txt", 50)