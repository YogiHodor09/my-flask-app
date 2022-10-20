
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg

    return total


def add(x, y):
    return x+y


nums = [3, 5]
add(*nums)

nums = {'x': 4, 'y': 3}

print(add(**nums))  # named argument x=3 , y=3


def apply(*args, operator):
    if operator == '*':
        return multiply(*args)
    elif operator == '+':
        return sum(args)
    else:
        return 'No valid operators found!'


print(apply(1, 3, 4, operator='+'))
