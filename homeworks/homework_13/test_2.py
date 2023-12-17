from typing import Union


from typing import Union



class Archive:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        if not isinstance(text, str) or not text:
            raise InvalidTextError(text)
        if not isinstance(number, (int, float)) or number <= 0:
            raise InvalidNumberError(number)
        self.text = text
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'

class InvalidTextError(Exception):
    def __init__(self, text):
        self.text = text
        super().__init__(f"Invalid text: {self.text}. Text should be a non-empty string.")


class InvalidNumberError(Exception):
    def __init__(self, number):
        self.number = number
        super().__init__(f"Invalid number: {self.number}. Number should be a positive integer or float.")

# help(Archive)
archive = Archive("дом", 5)
archive_2 = Archive(6, 7)
print(archive)

print(repr(archive_2))
# print(archive.archive_text)
# print(archive_2.archive_numbers)