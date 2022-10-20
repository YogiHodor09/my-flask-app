from operator import itemgetter
# Example 1


def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be 0')

    return dividend/divisor


def calculate(*values, operator):
    return operator(*values)


# passing func as argument like : operator = divide func() so args will contain same atgs like divide
result = calculate(20, 4, operator=divide)
print(result)


# Example 2


def search(sequence, expected, finder):
    for friend in sequence:
        if finder(friend) == expected:  # finder(Yogeshwar) == Yogeshwar
            return friend
    raise RuntimeError(f'Could not find the expected frineds name.')


friends = [
    {'name': 'Yogeshwar', 'age': 28},
    {'name': 'Danush', 'age': 21},
    {'name': 'Uma', 'age': 58}

]

# normal first class func example
# def friend_finder(friend):
#     return friend['name']

# lambda example
# print(search(friends, 'Yogeshwar', lambda friend: friend['name']))
# itemgetter package

print(search(friends, 'Yogeshwar', itemgetter('name')))
