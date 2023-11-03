# На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
# Первый список ваш лотерейный билет.
# Второй список содержит список чисел, которые выпали в лотерею.
# Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.
# Числа в каждом списке не повторяются.

list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]


def count_matching_numbers(ticket, lottery_numbers):
    ticket_set = set(ticket)
    lottery_numbers_set = set(lottery_numbers)

    # Используем функцию intersection() для нахождения пересечения множеств
    matching_numbers = ticket_set.intersection(lottery_numbers_set)

    # Возвращаем количество совпадающих чисел
    return len(matching_numbers)


matching_count = count_matching_numbers(list1, list2)
print("Количество совпадающих чисел:", matching_count)
