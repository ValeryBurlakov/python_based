# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
import string
from random import choices, randint
from string import ascii_lowercase, digits


def create_file(extension: str, min_len_name: int = 6, max_len_name: int = 30, min_size: int = 256,
                max_size: int = 4096, count: int = 42):
    for _ in range(count):
        name = ''.join(choices(ascii_lowercase + '_', k=randint(min_len_name, max_len_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        # for _ in range(randint(min_len_name, max_len_name)):
        with open(f'{name}.{extension}', 'wb') as f:
            f.write(data)


if __name__ == '__main__':
    create_file('bin', 8, 15, 400, 2000, 1)
