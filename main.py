class Student:
    courses_in_progress = []
    finished_courses = []
    grades = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.average_grades = {}
        self.__grades = []
        self.__average = -1

    def rate_lecturer(self, lecturer, course_attached, grade):
        if isinstance(lecturer, Lecturer) and course_attached in lecturer.courses and course_attached in lecturer.grade_for_lecturer:
            lecturer.grade_for_lecturer[course_attached] += [grade_for_lecturer]
        else:
            lecturer.grades[course_attached] = [grade_for_lecturer]

# Курсы в процессе изучения: Python, Git
# Завершенные курсы: Введение в программирование

    def __str__(self):
        if len(self.grades) > 0:
            avg_grades = sum(self.grades) / len(self.grades)
        else:
            avg_grades = "-"

        in_progress = ""
        for x in self.courses_in_progress: 
            in_progress += x+", "

        finished = ""
        for x in self.finished_courses: 
            finished += x+", "

        some_student = f"Имя: {self.name}, \n"
        some_student+=f"Фамилия: {self.surname}, \n"
        some_student+=f"Средняя оценка за домашние задания: {avg_grades}, \n"
        some_student+=f"Курсы в процессе изучения: {in_progress} \n"
        some_student+=f"Завершенные курсы: {finished}"
        return some_student

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    __lecturer_grades = []

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __lt__(self, student):
        lecturer = len(self.__lecturer_grades)
        if lecturer == 0:
            averageLecturer = "-"
            return "-"
        else:
            averageLecturer = sum(self.__lecturer_grades) / lecturer

        studentCount = len(student.grades)
        if studentCount == 0:
            averageStudent = "-"
            return "-"
        else:
            averageStudent = sum(student.grades) / studentCount

        return averageLecturer < averageStudent

    def addGrade(self, grade):
        self.__lecturer_grades.append(grade)

    def __str__(self):
        count = len(self.__lecturer_grades)
        if count == 0:
            average = "-"
        else:
            average = sum(self.__lecturer_grades) / count

        return f"Имя: {self.name} \nФамилия:  {self.surname} \nСредняя оценка за лекции: {average}"

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


    # def __lt__(self, student):
    #     return self.average < student.average_grades

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'  

    def __str__(self):
        return 'Имя: ' + self.name + '\nФамилия: ' + self.surname

    def average(students, course):
        for student in Student:
            average_grades = sum(student.grades) / len(student.grades)
        return average_grades

best_student = Student('Ruoy', 'Eman', 'M')
best_student.courses_in_progress = ['Python', 'C']
best_student.finished_courses = ['C++']
best_student.grades = [5]

second_student = Student('Mike', 'Baloon', 'M')
second_student.courses_in_progress = ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

second_mentor = Mentor('Donald', 'Trump')
second_mentor.courses_attached += ['Python']

first_lecturer = Lecturer('Lola', 'Lomova')
second_lecturer = Lecturer('Daria', 'Umnica')

first_reviewer = Reviewer('Sergey', 'Ivanov')
second_reviewer = Reviewer('Alex', 'Little')

first_lecturer.addGrade(4)
# print(first_lecturer < best_student)

# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

print(first_lecturer)
print()
print(best_student)
print()
print(first_lecturer < best_student)
