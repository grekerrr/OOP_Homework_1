class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def mid_grade(self):
        grades = []
        for _, grades_list in self.grades.items():
            grades.extend(grades_list)
        if grades:
            middle_grade = round(sum(grades) / len(grades), 2)
            return middle_grade
        else:
            return "Оценок нет, несчитаемо!"

    def add_courses(self, course):
        self.finished_courses.append(course)

    def __str__(self):
        return f"""
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.mid_grade()}
Курсы в процессе изучения: {",".join(self.courses_in_progress)}
Завершённые курсы: {",".join(self.finished_courses)}
"""

    def __lt__(self, other):
        if not isinstance(self, Student) or not isinstance(other, Student):
            return "Несравнимые студенты!"
        if self.mid_grade() > other.mid_grade():
            print(f"Средняя оценка выше у студента: {self.surname}")
        else:
            print(f"Средняя оценка выше у студента: {other.surname}")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor, Student):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def mid_grade(self):
        return Student.mid_grade(self)

    def __str__(self):
        return f"""
Имя: {self.name}
Фамилия: {self.surname}
Средний рейтинг за лекции: {self.mid_grade()}
"""

    def __lt__(self, other):
        if not isinstance(self, Lecturer) or not isinstance(other, Lecturer):
            return "Несравнимые лекторы!"
        if self.mid_grade() > other.mid_grade():
            print(f"Средний рейтинг выше у лектора: {self.surname}")
        else:
            print(f"Средний рейтинг выше у лектора: {other.surname}")


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return f"""
Имя: {self.name}
Фамилия: {self.surname}
"""


student_1 = Student("Ivan", "Petrov", "mail")
student_1.add_courses("Английский для программистов")
student_1.courses_in_progress += ["Git", "Основы Python"]

student_2 = Student("Elena", "Sidorova", "femail")
student_2.add_courses("Английский для программистов")
student_2.courses_in_progress += ["Git", "Основы Python"]


lecturer_1 = Lecturer("Lector", "Gannibal")
lecturer_1.courses_attached += ["Git", "Основы Python"]

lecturer_2 = Lecturer("Marfa", "Vasileva")
lecturer_2.courses_attached += ["Git", "Основы Python"]


reviewer_1 = Reviewer("Vasya", "Pupkin")
reviewer_1.courses_attached += ["Git", "Основы Python"]

reviewer_2 = Reviewer("Ekaterina", "Ivanova")
reviewer_2.courses_attached += ["Git", "Основы Python"]


student_1.rate_hw(lecturer_1, "Git", 7)
student_1.rate_hw(lecturer_1, "Основы Python", 9)
student_1.rate_hw(lecturer_2, "Git", 8)
student_1.rate_hw(lecturer_2, "Основы Python", 10)

student_2.rate_hw(lecturer_1, "Git", 9)
student_2.rate_hw(lecturer_1, "Основы Python", 8)
student_2.rate_hw(lecturer_2, "Git", 6)
student_2.rate_hw(lecturer_2, "Основы Python", 7)

reviewer_1.rate_hw(student_1, "Git", 3)
reviewer_1.rate_hw(student_1, "Основы Python", 10)
reviewer_1.rate_hw(student_2, "Git", 5)
reviewer_1.rate_hw(student_2, "Основы Python", 7)

reviewer_2.rate_hw(student_1, "Git", 8)
reviewer_2.rate_hw(student_1, "Основы Python", 6)
reviewer_2.rate_hw(student_2, "Git", 10)
reviewer_2.rate_hw(student_2, "Основы Python", 7)


print(f"""Студенты:
{student_1}
{student_2}
\n""")

print(f"""Лекторы:
{lecturer_1}
{lecturer_2}
\n""")

print(f"""Ревьюверы:
{reviewer_1}
{reviewer_2}
\n""")


lecturer_1.__lt__(lecturer_2)
student_1.__lt__(student_2)
print()


students = [student_1.grades, student_2.grades]
lecturers = [lecturer_1.grades, lecturer_2.grades]

def average_score_students(student_list, course_name):
    sum_score = 0
    len_score = 0
    for student in student_list:
        for key, value in student.items():
            if key == course_name:
                len_score += len(value)
                sum_score += sum(value)
    average = sum_score / len_score
    print(f'Средняя оценка студентов по курсу "{course_name}": {round(average, 2)}')
average_score_students(students, "Git")
average_score_students(students, "Основы Python")
print()

def average_grade_lecturers(lecturers_list, course_name):
    sum_grade = 0
    len_grade = 0
    for lecture in lecturers_list:
        for key, value in lecture.items():
            if key == course_name:
                len_grade += len(value)
                sum_grade += sum(value)
    average = sum_grade / len_grade
    print(f'Средний рейтинг лекторов по курсу "{course_name}": {round(average, 2)}')
average_grade_lecturers(lecturers, "Git")
average_grade_lecturers(lecturers, "Основы Python")
print()