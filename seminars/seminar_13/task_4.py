# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# 📌 Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# 📌 Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.

from pathlib import Path
import json


class User:
    def __init__(self, name, id, level):
        self.name = name
        self.id = id
        self.level = level

    def __str__(self):
        return f'{self.name=} {self.id=} {self.level=}'


def read_json(file_path: Path) -> set[User]:
    set_users = set()
    with open(file_path, 'r', encoding='utf-8') as f:
        file_users = json.load(f)
    for level, ids_names_dict in file_users.items():
        for id, name in ids_names_dict.items():
            set_users.add(User(level=int(level), id=int(id), name=name))
    return set_users



if __name__ == '__main__':
    # for user in read_json(Path("users.json")):
    #     print(user)
    print(*read_json(Path("users.json")), sep='\n')