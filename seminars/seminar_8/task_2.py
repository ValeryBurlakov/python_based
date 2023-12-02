# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# 📌 После каждого ввода добавляйте новую информацию в
# JSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключём для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные
# должны сохраняться.

from pathlib import Path
import json


def create_person(path_file: Path) -> None:
    set_id = set()
    if path_file.is_file():
        with open(path_file, 'r', encoding='utf=8') as f:
            data = json.load(f)
            print(data)
            for _, id_name in data.items():
                set_id.update(id_name.keys())
    else:
        data = {str(level): {} for level in range(1, 7 + 1)}

    while True:
        name = input("Введите имя: ")
        if name == '':
            break
        id = input("Введите идентификатор: ")
        level = input("Введите уровень доступа от 1 до 7: ")
        if id not in set_id:
            data[level].update({id: name})
            set_id.add(id)
            with open(path_file, 'w', encoding='utf=8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    create_person(Path("users.json"))
