items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}

max_weight = 1.0

backpack = {}

current_weight = 0.0

for item, weight in items.items():
    if current_weight + weight <= max_weight:
        backpack[item] = weight
        current_weight += weight

