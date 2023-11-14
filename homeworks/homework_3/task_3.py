def get_combinations(items, max_weight):
    backpack = {}
    result = []

    def backtrack(items, max_weight, curr_weight, start):
        if curr_weight > max_weight:
            return

        if curr_weight <= max_weight:
            if backpack:
                # result.append(backpack.copy())
                result.append(backpack.copy())

        for i in range(start, len(items)):
            item = list(items.keys())[i]
            weight = list(items.values())[i]

            backpack[item] = weight
            curr_weight += weight

            backtrack(items, max_weight, curr_weight, i + 1)

            backpack.pop(item)
            curr_weight -= weight

    backtrack(items, max_weight, 0, 0)
    # for combination in result:
    #     if combination:
    return result


items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

result = get_combinations(items, max_weight)
# for combination in result:
#     if combination:
#         print(combination)
print(result)
