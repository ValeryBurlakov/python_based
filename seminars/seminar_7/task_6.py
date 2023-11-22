# Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
from pathlib import Path
from random import choices, randint
from string import ascii_lowercase, digits
import os


def generation_files(file_path: str | Path, **kwargs) -> None:
    # print(kwargs)
    if isinstance(file_path, str):
        file_path = Path(file_path)
    if not file_path.is_dir():
        file_path.mkdir(parents=True) # если отсутствуют директории, воссоздаст отсутствующие
    # print(os.path.isdir(file_path))

    for extension, count in kwargs.items():
        create_file(extension, count_file=count)


def create_file(extension: str, min_len_name: int = 6, max_len_name: int = 30, min_size: int = 256,
                max_size: int = 4096, count_file: int = 42):
    for _ in range(count_file):
        name = ''.join(choices(ascii_lowercase + '_', k=randint(min_len_name, max_len_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        name_ext = f'{name}.{extension}'

        while Path(name_ext).is_file() :
            name = ''.join(choices(ascii_lowercase + '_', k=randint(min_len_name, max_len_name)))
            data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
            # for _ in range(randint(min_len_name, max_len_name)):
            name_ext = f'{name}.{extension}'

        with open(name_ext, 'wb') as f:
            f.write(data)


if __name__ == '__main__':
    generation_files(os.getcwd(), jpg=1, pdf=1)
    # create_file('bin', 8, 15, 400, 2000, 1)
