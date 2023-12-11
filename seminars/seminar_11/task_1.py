# Создайте класс Моя Строка, где:
# 📌 будут доступны все возможности str
# 📌 дополнительно хранятся имя автора строки и время создания
# (time.time)

import time


class myStr(str):
    '''
    Документация для класса myStr
    '''
    def __new__(cls, value: str, author: str):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time.time()
        # print(f'Создал класс {cls}')
        return instance

# help(myStr)
my_text = myStr('Моя жизнь тяжела', 'Вася')
print(my_text, my_text.author, my_text.time)
