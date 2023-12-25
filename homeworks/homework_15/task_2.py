import argparse
import logging
import sys
from datetime import datetime

logging.basicConfig(filename='num.log', encoding='utf-8', level=logging.INFO)
DATE_NOW = datetime.now().replace(microsecond=0)


def check_num(num):
    """
    Проверка числа
    """
    try:
        if num <= 1 or num >= 100000:
            logging.error(f'{DATE_NOW}, число {num} находится за границами диапазона: 1 > num < 100000 ')
            return "Число должно быть больше 1 и меньше 100000"
        else:
            for i in range(2, num):
                if num % i == 0:
                    logging.info(f'{DATE_NOW}, число {num} является составным числом')
                    return f"{num} - является составным числом"
            logging.info(f'{DATE_NOW}, число {num} является простым числом')
            return f"{num} - является простым числом"
    except TypeError as e:
        logging.error(f'{DATE_NOW}, Некорректный ввод: check_num({num})')
        return f'Некорректный ввод: check_num({num})'


def parser():
    if len(sys.argv) != 2:
        arguments = tuple(sys.argv)
        print("вводите команду в терминале корректно: python task_2.py a\nПример: python task_2.py 777")
        logging.error(f'{DATE_NOW}, Некорректный ввод параметров в терминале {arguments[1:]}')
        sys.exit(1)
    parser = argparse.ArgumentParser(description='Проверка числа')
    parser.add_argument('a', type=int, help='наше число')
    args = parser.parse_args()

    return check_num(args.a)


if __name__ == '__main__':
    # запуск файла
    print(check_num(234))
    print(check_num(234344334))
    print(check_num('fsdf'))
    print(check_num(-2j))
    print('=================================================================')
    # при запуске из терминала
    print(parser())
