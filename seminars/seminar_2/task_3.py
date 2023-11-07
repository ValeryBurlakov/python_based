BIN = 2
OCT = 8

num: int = int(input('Введите целое цисло: '))

for div in BIN, OCT:
    result: str = ''
    test_num = num
    while test_num > 0:
        new_num = test_num % div
        result: str = str(new_num) + result
        test_num //= div
    print(f'для {div}{result=}')

print(f'{bin(num)=} {oct(num)=}')

