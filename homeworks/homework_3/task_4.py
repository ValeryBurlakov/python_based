from collections import Counter

def get_duplicates(lst):
    counts = Counter(lst)
    duplicates = [element for element, count in counts.items() if count > 1]
    return list(set(duplicates))

lst = [1, 1, 2, 2, 3, 3, 4]
print(get_duplicates(lst))