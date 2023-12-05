# Создайте класс Сотрудник.
# # 📌 Воспользуйтесь классом человека из прошлого задания.
# # 📌 У сотрудника должен быть:
# # ○ шестизначный идентификационный номер
# # ○ уровень доступа вычисляемый как остаток от деления
# # суммы цифр id на семь

from task_3 import Person


class Employee(Person):
    MAX_LEVEL = 7

    def __init__(self, name: str, surname: str, patronymic: str, age: int, id: int):
        super().__init__(name, surname, patronymic, age)
        if 100_000 <= id < 1_000_000:
            self.id = id
        else:
            self.id = 100_000

    def get_level(self):
        sum_num = sum(int(num) for num in str(self.id))
        return sum_num % self.MAX_LEVEL


# vasya_2 = Person('Vasya', 'Pupkin', 'Andreevich', 24)


new_employee = Employee('Vasya', 'Pupkin', 'Andreevich', 24, 102_342)
print(new_employee.full_name())
print(new_employee.get_level())