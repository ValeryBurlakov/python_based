import random
import json
import csv
from typing import Callable


def generate_csv_file(file_name, rows):
    # Открытие файла для записи данных
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)

        # Генерация заданного количества строк
        for i in range(rows):
            # Генерация трех случайных чисел
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            c = random.randint(1, 100)

            # Запись чисел в файл
            writer.writerow([a, b, c])


def find_roots_(a, b, c):
    D = b ** 2 - 4 * a * c  # Вычисление дискриминанта

    if D < 0:  # Дискриминант отрицателен
        return None
    elif D == 0:  # Дискриминант равен нулю
        x = -b / (2 * a)
        return x
    else:  # Дискриминант положителен
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        return x1, x2


def save_to_json(func: Callable) -> Callable:
    def wrapper(filename, *args):
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            # next(reader)  # Пропускаем заголовок

            results = []
            for row in reader:
                a, b, c = map(int, row)
                roots = func(a, b, c)

                result = {"a": a, "b": b, "c": c, "roots": roots}
                results.append(result)

        with open("results.json", 'w') as jsonfile:
            json.dump(results, jsonfile)

    return wrapper


@save_to_json
def find_roots(a, b, c):
    return find_roots_(a, b, c)


generate_csv_file("input_data.csv", 101)
find_roots("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

if 100 <= len(data) <= 1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")
#
print(len(data) == 101)
# print(len(data))
