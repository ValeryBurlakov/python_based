# вводим строку
# сколько раз встречается каждая буква в строке без использования count и с ним
# результат сохраните в словаре где ключ - символ- значение - частота встречи символа
# порядок ключей, почему совпадают или не совпадают

user_text = input('Введите строку: ')

dict_words = {}

for item in set(user_text):
    dict_words[item] = user_text.count(item)

# print(dict_words)
print({item: user_text.count(item) for item in set(user_text)})

# 2 var
user_text = input('Введите строку: ')

dict_words_2 = {}

for item in user_text:
    dict_words_2[item] = dict_words_2.get(item, 0) + 1

print(dict_words_2)
