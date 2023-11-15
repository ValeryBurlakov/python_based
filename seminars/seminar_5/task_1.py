

one, two, three, *other = [int(i) for i in input("Введите не менее 4 чисел, разделенных символом '/': ").split('/')]

print([one, two, three, other])

result = {two: one, three: tuple(other)}

print(f'{result=}')