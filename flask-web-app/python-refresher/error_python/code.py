def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be 0')

    return dividend/divisor


grades = []

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:

    print('There are no grades in the list')
except ValueError as v:
    print(v)
else:
    print(f'The average grade is {average}')
finally:
    print('Thank you !')


# families = [
#     {'name': 'Yogeshwar', 'age': 28},
#     {'name': 'Danush', 'age': 21},
#     {'name': 'Uma', 'age': 58},
# ]

# for family in families:
#     name = family['name']
#     age = family['age']
#     print(f'Name is {name} and age is {age}')
