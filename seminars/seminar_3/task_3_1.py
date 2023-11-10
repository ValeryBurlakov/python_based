# вводим данные, сделать првоерку данных и преобразовать если можно в один из вариантов ниже
# целое положительное число. Вещественное положительное или отрицательное число
# строку в нижне регистре если в строке есть хотя бы одна заглавная буква
# строку в нижнем регистре в остальных случаях

user_data = input('Введите текст: ')

if user_data.isdigit():
    result = int(user_data), type(int(user_data))
elif user_data.replace('.', '').replace('-', '').isdecimal() \
        and user_data.count('-') <= 1 \
        and user_data.count('.') <= 1 \
        and user_data[1:].count('-') == 0:
    result = float(user_data)
elif not user_data.islower():
    #  elif user_data != user_data.lower():
    result = user_data.lower()
else:
    result = user_data.upper()

print(result, type(result))
