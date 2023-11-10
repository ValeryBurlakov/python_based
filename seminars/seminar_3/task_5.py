# создать список с повторяющимися целыми
# сформировать список с порядковыми номерами нечетных элементов
# нумерация с единицы

list_numbers = [1, 2, 5, 7, 16, 23, 5, 2, 1, 8, 6, 7]
result = []
for item, num in enumerate(list_numbers, 1):
    if num % 2:
        result.append(item)

print(result)
