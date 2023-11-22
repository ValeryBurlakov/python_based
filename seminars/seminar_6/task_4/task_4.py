

def secrets(riddle: str, var_answers: list[str], count = 3) -> int:
    print(f"угадай загадку за {count} попыток: '{riddle}' ")
    for i in range(1, count + 1):
        answer = input(f'Попытка {i}. Введите отгадку - ').lower()
        if answer in var_answers:
            return i
    return 0

def storage():
    riddles = {'Зимой и летом одним цветом': ['ель', 'Ёлка', 'сосна', 'елка'],
               'Не лает, не кусает, а в дом не пускает': ['замок', 'домофон', 'шпингалет', 'щеколда'],
               'Сидит дед, во сто шуб одет, кто его раздевает, слёзы проливает': ['лук', 'луковица']}
    for key, value in riddles.items():
        result = secrets(key, value)
        print(f'Угадал с {result} попытки' if result > 0 else 'Не угадал')


if __name__ == '__main__':
    storage()
    # result = secrets("Зимой и летом одним цветом", ['Ель', 'Ёлка', 'сосна', 'елка'])
    # print(f'Угадал с {result} попытки' if result > 0 else 'Не угадал')
