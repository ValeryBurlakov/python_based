import sys

data = [42, 73.0, 'Hello World!', True, 42, 'Hello World!', 256, 2 ** 8, 1, 'Привет, мир!']

for i, el in enumerate(data, 1):
    check_int = 'Объект является целым числом' if isinstance(el, int) else ''
    check_str = 'строкой' if isinstance(el, str) else ''
    # print(i, el)
    print(f'Номер по порядку = {i}, объект = {el}, адрес в памяти = {id(el)}, '
          f'размер в памяти = {sys.getsizeof(el)}, хэш объекта = {hash(el)} '
          f'{check_int}{check_str}')