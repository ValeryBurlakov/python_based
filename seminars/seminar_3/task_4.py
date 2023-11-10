# создать список, удалить повторяющиеся элементы

list_numbers = [1, 2, 5, 7, 16, 23, 5, 2, 1, 8, 6, 7]
COUNT = 2
for item in set(list_numbers):
    if list_numbers.count(item) == COUNT:
        for _ in range(COUNT):
            list_numbers.remove(item)


print(list_numbers)