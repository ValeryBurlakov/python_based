# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# # возвращайтесь в его начало.

from pathlib import Path
from typing import TextIO


def read_line_of_begin(fd: TextIO) -> str:
    text = fd.readline()
    if not text:
        fd.seek(0)
        text = fd.readline()
    return text[:-1]



def convert_file(names: str | Path, numbers: str | Path, new_file: str | Path) -> None:
    with (
        open(names, 'r', encoding='utf-8') as f_names,
        open(numbers, 'r', encoding='utf-8') as f_numbers,
        open(new_file, 'w', encoding='utf-8') as new_f
    ):
        len_names = sum(1 for _ in f_names)
        len_numbers = sum(1 for _ in f_numbers)
        text = f_names.read()
        print([text])
        max_len = max(len_names, len_numbers)

        for item in range(max_len):
            name = read_line_of_begin(f_names)
            str_num = read_line_of_begin(f_numbers)
            num_i, num_f = str_num.split(' | ')
            mult = int(num_i) * float(num_f)

            if mult < 0:
                new_f.write(f'{name.lower()} {-mult}\n')
            elif mult > 0:
                new_f.write(f'{name.upper()} {int(mult)}\n')


if __name__ == '__main__':
    convert_file(Path('names.txt'), Path('numbers.txt'), Path('result.txt'))

