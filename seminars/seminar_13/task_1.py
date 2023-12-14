# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# 📌 Обрабатывайте не числовые данные как исключения.


def validate() -> int | float:
    while True:
        data = input('Введите число: ')
        try:
            result = float(data)
            break
        except ValueError as e:
            print(f'Данные {data} не удалось преобразовать к вещественнону типy')

    try:
        result = int(data)
    except ValueError as e:
        pass

    return result


if __name__ == '__main__':
    print(validate())