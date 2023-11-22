# функция, которая генерирует псевдоимена
# имя начинается с Заглавной буквы, состоит из 4-7 букв, обязательно должны быть гласные
# сохранить имена в файл
import random
from pathlib import Path
from random import randint, choice
VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'
MIN_LENGTH = 4
MAX_LENGTH = 7

def set_name(file_path: str | Path, amount: int) -> None:
    with open(file_path, 'a', encoding='utf-8') as f:
        for _ in range(amount):
            len_name = randint(MIN_LENGTH, MAX_LENGTH)
            name = ''
            flag = choice([True, False])
            for i in range(len_name):
                # letter = choice(choice([CONSONANTS, VOWELS]))
                if flag:
                    letter = choice(CONSONANTS)
                else:
                    letter = choice(VOWELS)
                name += letter
                flag = not flag
            print(name.capitalize(), file=f)

if __name__ == '__main__':
    set_name('names.txt', 15)