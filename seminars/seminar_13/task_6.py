# Доработайте классы исключения так, чтобы они выдали
# подробную информацию об ошибках.
# 📌 Передавайте необходимые данные из основного кода
# проекта.

from pathlib import Path
import json


class ProjectException(Exception):
    pass


class LevelError(ProjectException):
    def __init__(self, level, user):
        self.level = level
        self.user = user

    def __str__(self):
        return (f'нельзя добавить пользователя с уровнем {self.level}'
                f'Вы вошли как {self.user} уровень ограничен с {self.user.level}')


class AccessError(ProjectException):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return (f'Отказано в доступе. Проверьте имя и или id'
                f'{self.name} и или {self.id}')


class User:
    def __init__(self, name, id, level):
        self.name = name
        self.id = id
        self.level = level

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name

    def __hash__(self):
        return hash((self.name, self.id))

    def __str__(self):
        return f'{self.name=} {self.id=} {self.level=}'

    def __repr__(self):
        return f'User(name = {self.name} id = {self.id}, level = {self.level})'


class Project:

    def __init__(self):
        self.user = None
        self.users = set()

    def read_json(self, file_path: Path) -> set[User]:
        with open(file_path, 'r', encoding='utf-8') as f:
            file_users = json.load(f)
        for level, ids_names_dict in file_users.items():
            for id, name in ids_names_dict.items():
                self.users.add(User(level=int(level), id=int(id), name=name))
        return self.users

    def add_user(self, name, id, level):
        if level < self.user.level:
            raise LevelError
        new_user = User(name, id, level)
        self.users.add(new_user)
        return new_user

    def enter_project(self, name, id):
        cur_user = User(name, id, 0)
        if cur_user not in self.users:
            raise AccessError
        for user in self.users:
            if cur_user == user:
                self.user = user
                return self.user

    def __str__(self):
        return f'Пользователи {self.users}'


if __name__ == '__main__':
    # for user in read_json(Path("users.json")):
    #     print(user)
    project1 = Project()
    project1.read_json(Path("users.json"))
    print(project1.enter_project('Роман', 6895))
    print(project1.add_user('Molodec', 36643, 5))
    print(project1)
