# вводим строку, вывести каждое слово с новой строки
# строки нумеруются с единицы
# слова выводятся отсортированными  unicode
# текст выравнивается во правому краю так что у самого длинного слова был 1 пробел между ним и номером строки

user_text = sorted(input(f'Введите текст: ').split())

# user_text.sort()
max_len_word = 0

for word in user_text:
    if len(word) > max_len_word:
        max_len_word = len(word)
for i, word in enumerate(user_text, 1):
    print(f'{i}. {word:>{max_len_word}}.')
