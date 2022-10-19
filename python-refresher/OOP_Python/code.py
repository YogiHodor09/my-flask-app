student = {'name': 'Yogeshwar', 'grades': (89, 90, 91, 92)}


def average(sequence):
    return sum(sequence)/len(sequence)


# print(average(student['grades']))

# OOP


class Student:
    def __init__(self, name, grades) -> None:
        self.name = name
        self.grades = grades

    def average_grades(self):
        return sum(self.grades)/len(self.grades)


student = Student('Yogesh', (100, 30, 40, 67))
print(student.name)
print(student.average_grades())
