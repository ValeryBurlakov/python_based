# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# 📌 При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-
# архивов
# 📌 list-архивы также являются свойствами экземпляра


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


help(Archive)
archive = Archive(5, "дом")
archive_2 = Archive(4, "дом_2")
print(archive.archive_text)
print(archive_2.archive_numbers)
