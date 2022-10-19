from cmath import sqrt


numbers = [2, 6, 8, 9]
sqtroot = [sqrt(num) for num in numbers]
doubled_twice = [num*2 for num in numbers]

print(f'Square root : {sqtroot} "\n" Multiple of two : {doubled_twice}')


friends = ['bob', 'yogesh', 'brindha', 'bubbles']

starts_b = [friend for friend in friends if friend.startswith('b')]
print(f"B word firends {starts_b}")
