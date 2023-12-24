# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# 📌 Соберите информацию о содержимом в виде объектов namedtuple.
# 📌 Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# 📌 В процессе сбора сохраните данные в текстовый файл используя
# логирование.

import logging
from pathlib import Path
from collections import namedtuple
import argparse

logging.basicConfig(filename='loggingINFO_task_6.txt', encoding='utf-8', level=logging.INFO)

logger = logging.getLogger(__name__)
File = namedtuple('File', 'name, extension, dir, parent')


def read_dir(file_path: Path):
    for file in file_path.iterdir():
        obj = File(file.stem if file.is_file() else file.name, file.suffix, file.is_dir(), file.parent)
        logger.info(obj)
        if obj.dir:
            read_dir(Path(obj.parent) / obj.name)


def walker():
    parser = argparse.ArgumentParser(prog='read_dir()', description='обход каталога с сохранением в файл')
    parser.add_argument('-f', '--file_path', help='какую директорию анализируем', required=True, type=Path)
    args = parser.parse_args()
    return read_dir(args.file_path)


if __name__ == '__main__':
    # read_dir(Path('/home/valery/PycharmProjects/basic-python/seminars/seminar_15'))
    walker()