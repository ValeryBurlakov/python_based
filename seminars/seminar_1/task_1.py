# високосность

REFORM = 1582
BIG_LEAP_YEAR = 400
SMALL_LEAP_YEAR = 4
LARGE_NON_LEAP_YEAR = 100
MULTIPLY = 0
year = int(input("Введите какой год проверить: "))

if year < REFORM:
    result = "Григорианский календарь не введен"
elif year % BIG_LEAP_YEAR == MULTIPLY:
    result = f'{year} - вискокосный год'
elif year % LARGE_NON_LEAP_YEAR == MULTIPLY:
    result = f'{year} - год не високосный'
elif year % SMALL_LEAP_YEAR == MULTIPLY:
    result = f'{year} - вискокосный год'
else:
    result = f'{year} - год не високосный'

print(result)