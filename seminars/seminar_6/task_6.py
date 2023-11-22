def secrets(riddle: str, var_answers: list[str], count=3) -> int:
    print(f"угадай загадку за {count} попыток: '{riddle}' ")
    for i in range(1, count + 1):
        answer = input(f'Попытка {i}. Введите отгадку - ').lower()
        if answer in var_answers:
            save(riddle, i)
            return i
    save(riddle, 0)
    return 0


def storage():
    riddles = {'Зимой и летом одним цветом': ['ель', 'Ёлка', 'сосна', 'елка'],
               'Не лает, не кусает, а в дом не пускает': ['замок', 'домофон', 'шпингалет', 'щеколда'],
               'Сидит дед, во сто шуб одет, кто его раздевает, слёзы проливает': ['лук', 'луковица']}
    for key, value in riddles.items():
        result = secrets(key, value)
        print(f'Угадал с {result} попытки' if result > 0 else 'Загадка не отгадана')


def save(riddle: str, count: int) -> None:
    _data.update({riddle: count})


def print_result() -> None:
    result = (f'Загадку "{key}" -  угадали с {value} попытки' if value > 0 else f'Загадку {key} -  не угадали'
              for key, value in _data.items())
    print(*result, sep='\n')


_data = {}

if __name__ == '__main__':

    storage()
    print_result()
    # result = secrets("Зимой и летом одним цветом", ['Ель', 'Ёлка', 'сосна', 'елка'])
    # print(f'Угадал с {result} попытки' if result > 0 else 'Не угадал')
