# Решить задания, которые не успели решить на семинаре. Возьмите любые 1 - 3 задания из
# прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.Также
# реализуйте возможность запуска из командной строки с передачей параметров.Данная промежуточная
# аттестация оценивается по системе "зачет" / "не зачет" "Зачет" ставится, если Слушатель
# успешно выполнил задание. "Незачет" ставится, если Слушатель не выполнил задание.Критерии
# оценивания: 1 - Слушатель написал корректный код для задачи, добавил к ним
# логирование ошибок и полезной информации.

import argparse
import logging
import sys
from datetime import datetime

logging.basicConfig(filename='triangle.log', encoding='utf-8', level=logging.INFO)
DATE_NOW = datetime.now().replace(microsecond=0)


def check_triangle(*args):
    """
    Проверка треугольника по его сторонам
    """
    if len(args) != 3:
        logging.error(f'{DATE_NOW}, Некорректное количество параметров. На входе: check_triangle{args}')
        return "Некорректное количество параметров"
    try:
        a, b, c = map(float, args)
        if a <= 0 or b <= 0 or c <= 0:
            logging.error(f'{DATE_NOW}, Отрицательные значения сторон треугольника: {a=} {b=} {c=}')
            return "Отрицательные значения сторон треугольника"
        elif a + b <= c or a + c <= b or b + c <= a:
            logging.error(f'{DATE_NOW}, Треугольник со сторонами: {a=} {b=} {c=} не существует')
            return "Такой треугольник не существует"
        else:
            logging.info(f'Треугольник существует:')
            if a == b == c:
                triangle_type = "равносторонний"
            elif a == b or a == c or b == c:
                triangle_type = "равнобедренный"
            else:
                triangle_type = "разносторонний"

            logging.info(f'{DATE_NOW}, Треугольник со сторонами: {a=} {b=} {c=} - {triangle_type}')
            return f'Треугольник со сторонами: {a=} {b=} {c=} - {triangle_type}'

    except (ValueError, TypeError):
        logging.error(f'{DATE_NOW}, Некорректный ввод параметров')
        return "Некорректный ввод параметров"


def parser():
    if len(sys.argv) != 4:
        arguments = tuple(sys.argv)
        print("вводите команду в терминале корректно: python task_1.py a b c\nПример: python task_1.py 7 7 7")
        logging.error(f'{DATE_NOW}, Некорректный ввод параметров в терминале {arguments[1:]}')
        sys.exit(1)
    parser = argparse.ArgumentParser(description='Проверка треугольника по его сторонам')
    parser.add_argument('a', type=float, help='Длина стороны a')
    parser.add_argument('b', type=float, help='Длина стороны b')
    parser.add_argument('c', type=float, help='Длина стороны c')
    args = parser.parse_args()

    return check_triangle(args.a, args.b, args.c)


if __name__ == '__main__':
    # запуск файла
    print(check_triangle(3, 4))
    print(check_triangle(3, -4, 5))
    print(check_triangle(3, 4, 5))
    print('=================================================================')
    # при запуске из терминала
    print(parser())
