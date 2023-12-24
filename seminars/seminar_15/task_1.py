# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# 📌 Например отлавливаем ошибку деления на ноль

import logging

logging.basicConfig(level=logging.ERROR, filename='loggingErrors', encoding='utf-8')


def div_func(num1: int | float, num2: int | float) -> float:
    try:
        result = num1 / num2

    except ZeroDivisionError as e:
        logging.error(f'Ошибка деления на ноль в формуле {num1} / {num2}\n {e}')
        return float('inf')

    return result

if __name__ == '__main__':
    print(div_func(1, 3))
    print(div_func(0, 3))
    print(div_func(1, 0))
    print(div_func(-1, 3))