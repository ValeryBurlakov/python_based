from random import randint

__all__ = ['func', '_secret'] # прием перечисленных объектов, которые нужно импортировать
SIZE = 100
_secret = 'qwerty' # символ подчеркивания делает переменную защищенной
__top_secret = '1q2w3e4r5t6y' # приватная переменная не импортируются


def func(a: int, b: int) -> str:
    z = f'В диапазоне от {a} до {b} получили {randint(a, b)}'
    return z


result = func(1, 6)