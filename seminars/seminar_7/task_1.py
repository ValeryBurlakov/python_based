from random import randint
from sys import argv


def guess_number(down: int = 0, up: int = 100, amount: int = 5) -> bool:
    num = randint(down, up)
    for _ in range(amount):
        num_yourself = int(input("Введите число: "))
        if num == num_yourself:
            return True
        elif num_yourself < num:
            print(f"Число {num_yourself} меньше загаданного")
        else:
            print(f"Число {num_yourself} больше загаданного")
    return False

if __name__ == '__main__':
    name, *param = argv
    # print(name, param)
    print(guess_number(*(int(num) for num in param)))
