# нарисовать в консоли елку спроси у пользователя количество рядов

STAR = '*'
SPACE = ' '

rows = int(input("Сколько рядом у ёлки: "))
stars = 1
spaces = rows - 1

while rows > 0:
    print(f'{SPACE * spaces}{STAR * stars}')
    rows -= 1
    spaces -= 1
    stars += 2
