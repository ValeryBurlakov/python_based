# вручную кортеж элементов разных типов, получить словарь списков где
# ключ - тип элемента
# значение - список элементов 1 типа

data = (42, 73, 3.14, 'Hello world!', None, True, 'Text', 100500.2, False)

result = {}

for item in data:
    element_type = type(item)
    key = result.setdefault(element_type, []) # если нет ключа присваиваем новый ключ и значение в список словарю,
    key.append(item)
    # if element_type not in result:
    #     result[element_type] = [item]
    # else:
    #     result[element_type].append(item)
print(result)


