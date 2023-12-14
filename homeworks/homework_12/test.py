import csv


class NameValidator:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not all(word.istitle() and word.isalpha() for word in value.split()):
            raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        instance.__dict__[self.name] = value


class Student:
    name = NameValidator()

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r') as file:
            reader = csv.reader(file)
            subjects = next(reader, [])
            for subject in subjects:
                self.subjects[subject] = {'grades': [], 'test_scores': []}

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        if grade not in [2, 3, 4, 5]:
            raise ValueError("Оценка должна быть целым числом от 2 до 5")
        self.subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, test_score):
        if not 0 <= test_score <= 100:
            raise ValueError("Результат теста должен быть целым числом от 0 до 100")
        self.subjects[subject]['test_scores'].append(test_score)

    # def get_average_test_score(self, subject):
    #     scores = self.subjects[subject]['test_scores']
    #     return sum(scores) / len(scores) if scores else 0

    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        scores = self.subjects[subject]['test_scores']
        return sum(scores) / len(scores) if scores else 0

    def get_average_grade(self):
        all_grades = [grade for subject in self.subjects for grade in self.subjects[subject]['grades']]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __getattr__(self, name):
        if name not in self.subjects:
            raise AttributeError(f"Предмет {name} не найден")
        return self.subjects[name]

    def __str__(self):
        subjects_list = [subject for subject in self.subjects if
                         self.subjects[subject]['grades'] or self.subjects[subject]['test_scores']]
        subjects_str = ', '.join(subjects_list)
        return f"Студент: {self.name}\nПредметы: {subjects_str}"



student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)

student = Student("Сидоров Сидор", "subjects.csv")

average_history_score = student.get_average_test_score("Биология")