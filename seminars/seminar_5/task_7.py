# функция генератор простые числа

def check_prime(number):
    if number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def generator(num):
    prime_num = 2
    yield prime_num
    num -= 1
    while num:
        prime_num += 1
        if check_prime(prime_num):
            num -= 1
            yield prime_num


n = int(input("Введите число: "))

for number in generator(n):
    print(number)
