class InvalidNameError(Exception):
    pass


class InvalidAgeError(Exception):
    pass


class InvalidIdError(Exception):
    pass


class Person:

    def __init__(self, name: str, surname: str, patronymic: str, age: int):
        if not name:
            raise InvalidNameError(f'Invalid name: {name}. Name should be a non-empty string.')
        if not surname:
            raise InvalidNameError(f'Invalid surname: {surname}. Surname should be a non-empty string.')
        if not patronymic:
            raise InvalidNameError(f'Invalid patronymic: {patronymic}. Patronymic should be a non-empty string.')
        if age <= 0:
            raise InvalidAgeError(f'Invalid age: {age}. Age should be a positive integer.')

        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self._age = age

    def birthday(self):
        self._age += 1

    def full_name(self):
        return f'{self.name} {self.surname} {self.patronymic}'

    def get_age(self):
        return self._age


class Employee(Person):
    MAX_LEVEL = 7

    def __init__(self, name: str, surname: str, patronymic: str, age: int, id: int):
        super().__init__(name, surname, patronymic, age)
        if 100_000 <= id < 1_000_000:
            self.id = id
        else:
            raise InvalidIdError(f'Invalid id: {id}. Id should be a 6-digit positive integer between 100000 and 999999.')

    def get_level(self):
        sum_num = sum(int(num) for num in str(self.id))
        return sum_num % self.MAX_LEVEL



new_employee = Employee('Vasya', 'Pupkin', 'Andreevich', 24, 102_342)
print(new_employee.full_name())
print(new_employee.get_level())
# try:
#     person1 = Person('John', 'Doe', 'Smith', 30)
#     print(person1.full_name())
#     print(person1.get_age())
#     person1.birthday()
#     print(person1.get_age())
#
#     employee1 = Employee('Alice', 'Johnson', 'Maria', 25, 102_342)
#     print(employee1.full_name())
#     print(employee1.get_level())
# except (InvalidNameError, InvalidAgeError, InvalidIdError) as e:
#     print(str(e))