# Напишите код, который анализирует число num и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если это число натуральное и
# делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
# Если подается отрицательное число или число более ста тысяч, выведите на экран сообщение:
# "Число должно быть больше 1 и меньше 100000".
#
# Внимание! Число 1 — не является ни простым, ни составным числом, так как у него только один делитель — 1.

num = 1
# num = 6
def check_num(num):
    if num <= 1 or num >= 100000:
        return "Число должно быть больше 1 и меньше 100000"
    else:
        for i in range(2, num):
            if num % i == 0:
                return f"{num} является составным числом"
        return f"{num} является простым числом"

print(check_num(num))
