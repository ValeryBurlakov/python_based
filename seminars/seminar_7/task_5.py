# Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

from random import choices, randint
from string import ascii_lowercase, digits


def generation_files(**kwargs) -> None:
    print(kwargs)
    for extension, count in kwargs.items():
        create_file(extension, count_file=count)


def create_file(extension: str, min_len_name: int = 6, max_len_name: int = 30, min_size: int = 256,
                max_size: int = 4096, count_file: int = 42):
    for _ in range(count_file):
        name = ''.join(choices(ascii_lowercase + '_', k=randint(min_len_name, max_len_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        # for _ in range(randint(min_len_name, max_len_name)):
        with open(f'{name}.{extension}', 'wb') as f:
            f.write(data)


if __name__ == '__main__':
    generation_files(txt=1, pdf=1)
    # create_file('bin', 8, 15, 400, 2000, 1)
