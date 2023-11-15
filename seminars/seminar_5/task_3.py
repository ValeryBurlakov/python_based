# развиваем предыдущую задачу
user_text = 'Задание'

my_dict = {symbol: ord(symbol) for symbol in user_text}

new_iter_dict = iter(my_dict.items())
# my_dict.items() # преобразование к словарю

count = 5

for _ in range(count):
    print(next(new_iter_dict)) # поставь * перед next, если не хочешь скобки
