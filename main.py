class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rete_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and (course in self.finished_courses or course in self.courses_in_progress) and lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return print('Ошибка оценки лектора')

    def __str__(self):
        sum_grade = 0
        qty_grade = 0
        for lst_grades in self.grades.values():
            for grade in lst_grades:
                sum_grade += grade
                qty_grade += 1
        avg_grade = sum_grade / qty_grade
        massage = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {avg_grade} \nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}\n'
        return massage

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это не студент')
            return

        sum_grades_1 = 0
        sum_grades_2 = 0
        qty_grade_1 = 0
        qty_grade_2 = 0

        for lst_grades in self.grades.values():
            for grade in lst_grades:
                sum_grades_1 += grade
                qty_grade_1 += 1
        avg_grade_1 = sum_grades_1 / qty_grade_1

        for lst_grades in other.grades.values():
            for grade in lst_grades:
                sum_grades_2 += grade
                qty_grade_2 += 1
        avg_grade_2 = sum_grades_2 / qty_grade_2

        return avg_grade_1 < avg_grade_2


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        sum_grade = 0
        qty_grade = 0
        for lst_grades in self.grades.values():
            for grade in lst_grades:
                sum_grade += grade
                qty_grade += 1
        avg_grade = sum_grade / qty_grade
        massage = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade} \n'
        return massage

    def __lt__(self, other):
        if not isinstance(other, Mentor):
            print('Это не лектор')
            return

        sum_grades_1 = 0
        sum_grades_2 = 0
        qty_grade_1 = 0
        qty_grade_2 = 0

        for lst_grades in self.grades.values():
            for grade in lst_grades:
                sum_grades_1 += grade
                qty_grade_1 += 1
        avg_grade_1 = sum_grades_1 / qty_grade_1

        for lst_grades in other.grades.values():
            for grade in lst_grades:
                sum_grades_2 += grade
                qty_grade_2 += 1
        avg_grade_2 = sum_grades_2 / qty_grade_2

        return avg_grade_1 < avg_grade_2


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def rate_student(self, student, course, grade):
        if isinstance(
                student, Student
        ) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return print('Ошибка оценки студента')

    def __str__(self):
        massage = f'Имя: {self.name} \nФамилия: {self.surname}\n'
        return massage


stud1 = Student('Ruoy', 'Eman', 'your_gender')
stud1.courses_in_progress += ['Python']
stud1.courses_in_progress += ['Java']
stud1.finished_courses += ['C++']

stud2 = Student('Егор', 'Егоров', 'your_gender')
stud2.courses_in_progress += ['Ruby']
stud2.courses_in_progress += ['Java']
stud2.finished_courses += ['SWIFT']

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['Java']
reviewer1.rate_student(stud1, 'Python', 10)
reviewer1.rate_student(stud1, 'Python', 10)
reviewer1.rate_student(stud1, 'Python', 10)
reviewer1.rate_student(stud1, 'Java', 5)
reviewer1.rate_student(stud1, 'Java', 5)
reviewer1.rate_student(stud1, 'Java', 5)

reviewer2 = Reviewer('Alex', 'Valex')
reviewer2.courses_attached += ['Ruby']
reviewer2.courses_attached += ['Java']
reviewer2.rate_student(stud2, 'Ruby', 3)
reviewer2.rate_student(stud2, 'Java', 2)
reviewer2.rate_student(stud2, 'Java', 1)
reviewer2.rate_student(stud2, 'Ruby', 5)
reviewer2.rate_student(stud2, 'Ruby', 5)
reviewer2.rate_student(stud2, 'Ruby', 5)

lecturer1 = Lecturer('Иван', 'Иванов')
lecturer1.courses_attached += ['Java']
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Петя', 'Васичкин')
lecturer2.courses_attached += ['Ruby']
lecturer2.courses_attached += ['Java']

stud1.rete_lecturer(lecturer1, 'Python', 10)
stud1.rete_lecturer(lecturer1, 'Python', 10)
stud1.rete_lecturer(lecturer1, 'Java', 5)
stud1.rete_lecturer(lecturer1, 'Java', 5)

stud2.rete_lecturer(lecturer2, 'Ruby', 5)
stud2.rete_lecturer(lecturer2, 'Ruby', 5)
stud2.rete_lecturer(lecturer2, 'Java', 5)
stud2.rete_lecturer(lecturer2, 'Java', 5)

print(stud1)
print(lecturer1)
print(reviewer1)
print(lecturer1 > lecturer2)
print(stud1 < stud2)