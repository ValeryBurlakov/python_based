# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# 📌 Возвращается строка в нижнем регистре.

from string import ascii_letters


def del_sim(text: str) -> str:
    # result = ''
    # for symbol in text:
    #     if symbol in ascii_letters + ' ':
    #         result += symbol
    # return result.lower()
    return ''.join(symbol for symbol in text if symbol in ascii_letters + ' ').lower()


# if __name__ == '__main__':
    # print(del_sim('wefffew wewefswf HJ jejfjsdf j JJJfedf s  2324 '))