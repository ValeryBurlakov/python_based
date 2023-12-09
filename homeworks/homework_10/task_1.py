# class Animal:
#     def __init__(self, name, weight):
#         self.name = name.title()
#         self.weight = weight
#
#
# class Fish(Animal):
#
#     def __init__(self, name, weight, max_depth):
#         super().__init__(name, weight)
#         self.max_depth = max_depth
#
#     def get_max_depth(self):
#         if self.max_depth < 10:
#             return 'мелководная'
#         elif self.max_depth < 100:
#             return 'средневодная'
#         elif self.max_depth >= 100:
#             return 'глубоководная'
#
#     def info(self):
#         return f'{self.name}\n вес {self.weight}\n размер крыльев {self.max_depth}\n'
#
#
# class Bird(Animal):
#     def __init__(self, name, weight, wingspan):
#         super().__init__(name, weight)
#         self.wingspan = wingspan
#
#     def get_wing_length(self):
#         return round(self.wingspan / 2, 2)
#
#     def info(self):
#         return f'{self.name}\n вес {self.weight}\n размер крыльев {self.wingspan}\n'
#
#
# class Mammal(Animal):
#     def __init__(self, name, weight, size):
#         super().__init__(name, weight)
#         self.size = size
#
#     def get_category(self):
#         if self.size < 10:
#             return 'маленький'
#         if self.size < 100:
#             return 'средний'
#         if self.size > 100:
#             return 'гигант'
#
#     def info(self):
#         return f'{self.name}\n вес {self.weight}\n размер {self.size}\n'
#
#
# class AnimalFactory:
#     @staticmethod
#     def create_animal(animal_type, *args):
#         if animal_type == 'Bird':
#             return Bird(*args)
#         elif animal_type == 'Fish':
#             return Fish(*args)
#         elif animal_type == 'Mammal':
#             return Mammal(*args)
#         else:
#             raise ValueError('Недопустимый тип животного')
#
#


class Animal:
    def __init__(self, name):
        self.name = name


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return self.wingspan / 2


class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth < 10:
            return "Мелководная рыба"
        elif self.max_depth > 100:
            return "Глубоководная рыба"
        else:
            return "Средневодная рыба"


class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 1:
            return "Малявка"
        elif self.weight > 200:
            return "Гигант"
        else:
            return "Обычный"


class AnimalFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_animal(animal_type, *args):
        if animal_type == "Bird":
            return Bird(*args)
        elif animal_type == "Fish":
            return Fish(*args)
        elif animal_type == "Mammal":
            return Mammal(*args)
        else:
            raise ValueError("Недопустимый тип животного")


animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)
print(animal1.wing_length())
print(animal2.depth())
print(animal3.category())