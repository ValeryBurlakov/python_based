# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида 10.25%.
# В результате result получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
#
# Сумма рассчитывается как ставка умноженная на процент премии.
#
# Не забудьте распечатать в конце результат.

# names = ["Alice", "Bob", "Charlie"]
# salary = [5000, 6000, 7000]
# bonus = ["10%", "5%", "15%", "2"]
# names = ["Eva", "David", "Frank"]
# salary = [7500, 8000, 9000]
# bonus = ["8%", "12%", "7%"]
names = ["Grace", "John", "Linda"]
salary = [6200, 5800, 7500]
bonus = ["9%", "3%", "12%"]
len_salary = len(salary)
len_names = len(names)
len_bonus = len(bonus)
# result = {name: salary * float(prize[:-1])/100 for name, salary, prize in zip(names, salary, bonus)}
result = {name: salary * float(prize[:-1])/100 for name, salary, prize in zip(names, salary, bonus) if len_bonus == len_salary == len_names}
print(result)
# результат словарь, ключ - имя, значение - премия
# {'Alice': 500.0, 'Bob': 300.0, 'Charlie': 1050.0}