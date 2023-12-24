# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# 📌 Напишите аналогичный декоратор, но внутри используйте
# модуль logging.

from pathlib import Path
import json
from typing import Callable
import logging

logging.basicConfig(filename='loggingINFO_task_2', encoding='utf-8', level=logging.INFO)

logger = logging.getLogger(__name__)
def my_logger(func: Callable) -> Callable:

    def wrapper(*args, **kwargs):
        dict_json = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        dict_json['result'] = result
        logger.info(dict_json)


        return result

    return wrapper


@my_logger
def get_all(*args: list, **kwargs) -> int:
    return sum(args)


if __name__ == '__main__':
    get_all(42, 6, x="2", z=True, f="bv")