# Доработайте задачу 5.
# 📌 Вынесите общие свойства и методы классов в класс
# Животное.
# 📌 Остальные классы наследуйте от него.
# 📌 Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    def __init__(self, name, weight):
        self.name = name.title()
        self.weight = weight


class Fish(Animal):

    def __init__(self, name, weight, max_depth):
        super().__init__(name, weight)
        self.max_depth = max_depth

    def get_max_depth(self):
        if self.max_depth < 10:
            return 'мелководная'
        elif self.max_depth < 100:
            return 'средневодная'
        elif self.max_depth >= 100:
            return 'глубоководная'

    def info(self):
        return f'{self.name}\n вес {self.weight}\n размер крыльев {self.max_depth}\n'


class Bird(Animal):
    def __init__(self, name, weight, wingspan):
        super().__init__(name, weight)
        self.wingspan = wingspan

    def get_wing_length(self):
        return round(self.wingspan / 2, 2)

    def info(self):
        return f'{self.name}\n вес {self.weight}\n размер крыльев {self.wingspan}\n'


class Mammal(Animal):
    def __init__(self, name, weight, size):
        super().__init__(name, weight)
        self.size = size

    def get_category(self):
        if self.size < 10:
            return 'маленький'
        if self.size < 100:
            return 'средний'
        if self.size > 100:
            return 'гигант'

    def info(self):
        return f'{self.name}\n вес {self.weight}\n размер {self.size}\n'


fish_1 = Fish('акула', 200, 1000)
bird_1 = Bird('синица', 0.1, 1000)
mammal_1 = Mammal('тигр', 300, 3000)
print(fish_1.info(), bird_1.info(), mammal_1.info())

print(fish_1.get_max_depth(), bird_1.get_wing_length(), mammal_1.get_category())
