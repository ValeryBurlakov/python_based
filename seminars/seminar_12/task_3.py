# Создайте класс-генератор.
# 📌 Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# 📌 Если переданы два параметра, считаем step=1.
# 📌 Если передан один параметр, также считаем start=1.

class Factorial:
    def __init__(self, *args):
        match len(args):
            case 1:
                self.start = 1
                self.step = 1
                self.stop = args[0]
            case 2:
                self.start, self.stop = args
                self.step = 1
            case 3:
                self.start, self.stop, self.step = args

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.stop:
            result = self.start
            for mult in range(2, self.start):
                result *= mult
            self.start += self.step
            return result
        raise StopIteration


fact = Factorial(3, 10, 2)
for num in fact:
    print(num)
