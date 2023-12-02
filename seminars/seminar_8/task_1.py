# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки
import json
from pathlib import Path


def create_json_file(file_path: Path) -> None:
    dict_names = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            name, number = line.rstrip().split()
            dict_names[name.title()] = float(number)
        print(dict_names)

    with open(f'{file_path.stem}.json', 'w', encoding='utf-8') as f:
        json.dump(dict_names, f, ensure_ascii=False, indent=2) # загружаем


if __name__ == '__main__':
    create_json_file(Path('/home/valery/PycharmProjects/basic-python/seminars/seminar_7/result.txt'))