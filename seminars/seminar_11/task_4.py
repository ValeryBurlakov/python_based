# Доработаем класс Архив из задачи 2.
# 📌 Добавьте методы представления экземпляра для программиста
# и для пользователя.


class Archive:
    '''
    Документация для класса архив
    '''
    _instance = None

    def __new__(cls, num, string):
        '''
        Документация для метода __new__:
        '''
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_numbers = []
        else:
            cls._instance.archive_text.append(cls._instance.string)
            cls._instance.archive_numbers.append(cls._instance.num)

        return cls._instance

    def __init__(self, num: int | float, string: str):
        '''
        Документация для метода __init__
        :param num:
        :param string:
        '''
        self.num = num
        self.string = string

    def __str__(self):
        return f'строка это = {self.string}. Номер = {self.num}. Архив строк = {self.archive_text}. ' \
                f'Архив чисел = {self.archive_numbers}'

    def __repr__(self):
        return f'Archive("{self.string}", {self.num})'



# help(Archive)
archive = Archive(5, "дом")
archive_2 = Archive(4, "дом_2")
print(archive)

print(repr(archive_2))
# print(archive.archive_text)
# print(archive_2.archive_numbers)
