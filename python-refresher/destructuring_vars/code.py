x, y = 5, 11


t = 5, 11
x, y = t
print(x, y)


student_attendance = {'Yogeshwar': 94, 'Prathyu': 95, 'Danush': 99}

for student, percentage in student_attendance.items():
    # getting keys,values from dict items() using for loop
    print(f"{student}:{percentage}%")


# de-structuring List of Tuples
family_people = [('Yogesh', 28, 'Engineer'), ('Danush', 21, 'Doctor'),
                 ('Prathyu', 26, 'Asst.Commissioner')]


for name, age, profession in family_people:
    print(f'Name: {name}, Age: {age}, Profession: {profession}')


person = ('Yogeshwar', 28, 'Engineer')

name, _, profession = person  # underscore don't care about the variable
print(f'{name,profession}')


l = [1, 2, 3, 4, 5]
# to split list into two lists

head, *tail = l

print(head)
print(tail)


*head, tail = l

print(head)
print(tail)
