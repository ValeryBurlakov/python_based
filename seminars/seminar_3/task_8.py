# три друга взяли вещи в поход
# ключ - имя друга, значение - кортеж вещей
# какие вещи вяли все 3 друга
# какие вещи уникальны, есть только у 1 друга
# какие вещи есть у всех друзей кроме 1 и имя того, у кого отсутствует
# используйте операции с множествами, код должен расширяться на любое колво друзей

hike = {'Aaz': ("спички", "спальник", "дрова", "топор"),
        'Skeeve': ("спальник", "спички", "вода", "еда"),
        'Tananda': ("вода", "спички", "косметичка")}

# какие вещи взяли все вместе
items = set()
for values in hike.values():
    # items = items.union(set(values)) # семинар
    items.update(set(values)) # мое решение
print(items)

# items_2 = set()
# for values in hike.values():
#     items_2 |= set(values) # преподаватель
# print(items_2)
#
# items_4 = set() # это жестко
# for values in hike.values():
#     for value in values:
#         items_4.add(value)
# print(items_4)



# какие вещи уникальны и есть только у 1 друга

unique = dict()

for values in hike.values():
    for value in values:
        unique[value] = unique.get(value, 0) + 1

print(unique)

for key, value in unique.items():
    if value == 1:
        print(key)
# 2
unique_2 = dict()
for master_key, master_values in hike.items():
    for slave_key, slave_values in hike.items():
        if master_key != slave_key:
            if not unique_2.get(master_key):
                unique_2[master_key] = set(master_values) - set(slave_values)
            else:
                unique_2[master_key] -= set(slave_values)
print(unique_2)

# какие вещи есть у всех друзей кроме 1 и имя того, у кого отсутствует
items_3 = set()
for values in hike.values():
    # items = items.union(set(values)) # семинар
    items_3.update(set(values)) # мое решение
print(items_3)
unique_3 = dict()

for master_key, master_values in hike.items():
    for slave_key, slave_values in hike.items():
        if master_key != slave_key:
            if not unique_3.get(master_key):
                unique_3[master_key] = set(master_values) - set(slave_values)
            else:
                unique_3[master_key] -= set(slave_values)
print(unique_3)

duplicates = set(items_3)

for value in unique_3.values():
    duplicates -= value
print(f'Дублирующие вещи: {duplicates = }')

for key, value in hike.items():
    other = (set(value) ^ duplicates) - set(unique_3[key])
    if other:
        print(f'У {key} отсутствует {other}, но есть у остальных')
