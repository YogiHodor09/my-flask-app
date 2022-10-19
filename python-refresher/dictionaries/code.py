friend_ages = {'Yogeshwar': 28, 'Danush': 21, 'Uma': 58}

friend_ages['Prathyu'] = 26

print(friend_ages)

friend_ages['Danush'] = 20

print(friend_ages)


friends = [
    {'name': 'Yogeshwar', 'age': 28},
    {'name': 'Prathyu', 'age': 26},
    {'name': 'Danush', 'age': 21},
]

print(friends[0]['name'])


student_attendance = {'Yogeshwar': 94, 'Prathyu': 95, 'Danush': 99}

for student in student_attendance:
    # getting keys,values from dict using for loop
    print(f"{student}:{student_attendance[student]}%")


for student, percentage in student_attendance.items():
    # getting keys,values from dict items() using for loop
    print(f"{student}:{percentage}%")



