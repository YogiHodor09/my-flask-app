friends = ['Rolf', 'Jen', 'Bob', 'Anne']

for friend in friends:
    print(f'{friend} is my friend')


for friend in range(4):
    print(f'{friend} is my friend')


grades = [35, 78, 3, 34, 4, 5]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(total/amount)


grades = [35, 78, 3, 34, 4, 5]
total = sum(grades)
amount = len(grades)

print(
    f'Without for loop getting avaerage by adding sum method : {total/amount}')
