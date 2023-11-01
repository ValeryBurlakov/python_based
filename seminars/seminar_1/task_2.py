# вводим число от 1 до 999
# ну и короче условия понятны по задаче

MIN_NUM = 1
MAX_NUM = 999
ONE = 1
TEN = 10
HUNDRED = 100

num = MAX_NUM + ONE

while num < MIN_NUM or num > MAX_NUM:
    num = int(input(f"Введите число: от {MIN_NUM} до {MAX_NUM}: "))

if num < TEN:
    result = f"Число {num} - цифра, её квадрат равен: {num * num}"

elif num < HUNDRED:
    num_1 = num // TEN
    num_2 = num % TEN
    result = f"Число {num} - двузначное, произведение цифр равно: {num_1 * num_2}"
else:
    num_1 = num // HUNDRED
    num_2 = num // TEN % TEN
    num_3 = num % TEN
    result = f"Число {num} - трехзначное, его зеркальное число {num_3 * HUNDRED + num_2 * TEN + num_1}"

print(result)




