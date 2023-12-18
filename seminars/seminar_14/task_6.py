# На семинаре 13 был создан проект по работе с
# пользователями (имя, id, уровень).
# 📌 Напишите 3-7 тестов pytest для данного проекта.
# 📌 Используйте фикстуры.
import json
from pathlib import Path

from seminars.seminar_13.task_5 import User, Project, AccessError, LevelError

import pytest


@pytest.fixture
def new_set():
    data = {User('Ира', 432, 1),
            User('Иван', 567, 2),
            User('Мария', 123, 3),
            User('Роман', 6895, 4)}
    return data


@pytest.fixture
def new_user():
    return User('new', 7384, 5)

@pytest.fixture
def good_user():
    return User('Мария', 123, 3)


# def test_add_user(good_user):
#     project = Project()
#     project.read_json(Path('users.json'))
#     project.enter_project('Мария', 123)
#     result = project.add_user('new', 7384, 1)
#     assert new_user() == result


def test_load(new_set):
    project = Project()
    result = project.read_json(Path('users.json'))
    assert result == new_set


def test_enter(good_user):
    project = Project()
    project.read_json(Path('users.json'))
    result = project.enter_project('Мария', 123)
    assert result == good_user


def test_no_enter():
    project = Project()
    project.read_json(Path('users.json'))
    with pytest.raises(AccessError):
        project.enter_project('Леонид', 123)


if __name__ == '__main__':
    pytest.main(['-v'])
