# таблица умножения

LOWER_LIMIT = 2
UPPER_LIMIT = 10
COLUMN = 4

# for i in (LOWER_LIMIT, COLUMN + LOWER_LIMIT):
#     for j in range(LOWER_LIMIT, UPPER_LIMIT + 1):
#         for k in range(i, i + COLUMN):
#             print(f'{k:>2} * {j:>2} = {k * j:>2}', end='\t')
#         print()
#     print()

my_gen = (f'{k:>2} * {j:>2} = {k * j:>2}\t' if k != i + COLUMN - 1 else \
              f'{k:>2} * {j:>2} = {k * j:>2}\n' if j != UPPER_LIMIT else \
                  f'{k:>2} * {j:>2} = {k * j:>2}\n\n' \
          for i in (LOWER_LIMIT, COLUMN + LOWER_LIMIT)
          for j in range(LOWER_LIMIT, UPPER_LIMIT + 1)
          for k in range(i, i + COLUMN))

print(*my_gen, end="")
