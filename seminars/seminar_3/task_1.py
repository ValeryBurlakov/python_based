# вручную список чисел, которые повторяются, получить новый список,
# который содержит уникальные без повтора элементы исходного списка

list_nums = [3, 3, 7, 4, 2, 1, 2, 7]

result_list = list(set(list_nums))
print(f'список {result_list}')

new_list = []
for item in list_nums:
    if item not in new_list:
        new_list.append(item)

print(new_list)