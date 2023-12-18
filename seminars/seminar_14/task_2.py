# Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери
# символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)


from string import ascii_letters


def del_sim(text: str) -> str:
    """
    >>> del_sim('hello world')
    'hello world'
    >>> del_sim('Hi pEoPlE')
    'hi people'
    >>> del_sim('hello, my friend!')
    'hello my friend'
    >>> del_sim('hello друг')
    'hello '
    >>> del_sim('HelLo, друГ!')
    'hello '
    """
    return ''.join(symbol for symbol in text if symbol in ascii_letters + ' ').lower()


if __name__ == '__main__':
    # print(del_sim('wefffew wewefswf HJ jejfjsdf j JJJfedf s  2324 '))
    # help(del_sim)
    import doctest
    doctest.testmod(verbose=True)


# help(del_sim)