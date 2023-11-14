from itertools import combinations


def get_combinations(items, max_weight):
    keys = list(items.keys())
    n = len(items)

    result = []

    for r in range(1, n + 1):
        combinations_list = list(combinations(range(n), r))

        for combination in combinations_list:
            total_weight = 0
            backpack = {}

            for index in combination:
                item = keys[index]
                weight = items[item]

                if total_weight + weight <= max_weight:
                    backpack[item] = weight
                    total_weight += weight
                else:
                    break

            if total_weight <= max_weight:
                result.append(backpack.copy())
    return result


items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

result = get_combinations(items, max_weight)
print(result)