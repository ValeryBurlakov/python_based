import re
from collections import Counter


def count_most_common_words(text):
    # Преобразование в нижний регистр
    text = text.lower()

    # Удаление знаков препинания
    text = re.sub(r'[^\w\s]', ' ', text)

    # Разбиение текста на слова
    words = text.split()

    # Подсчет повторений слов
    word_counts = Counter(words)

    # Удаление чисел из результатов
    word_counts = {word: count for word, count in word_counts.items() if not word.isdigit()}

    # Сортировка по убыванию количества повторений
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Возвращение первых 10 наиболее часто встречающихся слов
    return sorted_word_counts[:10]


text = "Hello world. Hello Python. Hello again. it's"
result = count_most_common_words(text)
print(result)
