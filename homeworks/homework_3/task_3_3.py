from pprint import pprint

#
#
#
#
#
#
#
#
#
#
#
# def find_backpack(items, max_weight):
#     def find_combinations(items, max_weight, curr_weight, curr_backpack, all_backpacks):
#         if curr_weight > max_weight:
#             return
#         if not items:
#             if curr_backpack:
#                 all_backpacks.append(dict(curr_backpack))
#             return
#         item, weight = items[0]
#         find_combinations(items[1:], max_weight, curr_weight, curr_backpack, all_backpacks)
#         if curr_weight + weight <= max_weight:
#             find_combinations(items[1:], max_weight, curr_weight + weight, curr_backpack + [(item, weight)], all_backpacks)
#
#     all_backpacks = []
#     items_list = list(items.items())
#     find_combinations(items_list, max_weight, 0, [], all_backpacks)
#
#     return all_backpacks
#
# items = {
#     "ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }
# max_weight = 1.0
#
# backpacks = find_backpack(items, max_weight)
# print(backpacks)
#
#
#
#
#
#
#
# def find_backpack(items, max_weight):
#
#     def find_combinations(items, max_weight, curr_weight, curr_backpack, all_backpacks):
#
#         if curr_weight > max_weight:
#             return
#         if not items:
#             if curr_backpack:
#                 all_backpacks.append(dict(curr_backpack[::1]))  # Reverse the order before appending
#             return
#         item, weight = items[0]
#         find_combinations(items[1:], max_weight, curr_weight, curr_backpack, all_backpacks)
#         if curr_weight + weight <= max_weight:
#             find_combinations(items[1:], max_weight, curr_weight + weight, curr_backpack + [(item, weight)],
#                               all_backpacks)
#
#     all_backpacks = []
#     items_list = list(items.items())
#     find_combinations(items_list, max_weight, 0, [], all_backpacks)
#
#     return all_backpacks
#
# items = {
#     "ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }
# max_weight = 1.0
#
# backpacks = find_backpack(items, max_weight)
# print(backpacks)
#
#
#
#



# #1
# items = {
#     "ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }
# max_weight = 1.0
#2
# items = {
#     "ноутбук": 2.0,
#     "книги": 1.5,
#     "зарядное устройство": 0.5,
#     "бутерброды": 0.3,
#     "вода": 1.0
# }
# max_weight = 5.0
#3
# items = {
#     "лодка": 3.0,
#     "велосипед": 4.0,
#     "мангал": 2.0
# }
# max_weight = 1.0
#4
# items = {
#     "спальник": 1.0,
#     "палатка": 2.0,
#     "термос": 0.5,
#     "карта": 0.1,
#     "фонарик": 0.2,
#     "котелок": 0.5,
#     "еда": 2.0,
#     "одежда": 1.0,
#     "обувь": 0.8,
#     "нож": 0.2
# }
# max_weight = 10
#6
items = {
    "спальник": 1.5,
    "палатка": 3.2,
    "термос": 0.6,
    "карта": 0.1,
    "фонарик": 0.3,
    "котелок": 0.8,
    "еда": 2.5,
    "одежда": 1.7,
    "обувь": 1.2,
    "нож": 0.2
}
max_weight = 1


def find_backpack(items, max_weight):

    def find_combinations(items, max_weight, curr_weight, curr_backpack, all_backpacks):
        if curr_weight > max_weight:
            return
        if not items:
            if curr_backpack:
                all_backpacks.append(dict(curr_backpack[::-1]))  # Reverse the order before appending
            return
        item, weight = items[0]
        find_combinations(items[1:], max_weight, curr_weight, curr_backpack, all_backpacks)
        if curr_weight + weight <= max_weight:
            find_combinations(items[1:], max_weight, curr_weight + weight, curr_backpack + [(item, weight)],
                              all_backpacks)

    all_backpacks = []
    items_list = list(items.items())[::-1]
    find_combinations(items_list, max_weight, 0, [], all_backpacks)

    return all_backpacks


backpacks = find_backpack(items, max_weight)

pprint(backpacks)