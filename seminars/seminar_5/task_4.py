
my_gen = (i for i in range(0, 100, 2) if i // 10 + i % 10 != 8)

print(*my_gen)