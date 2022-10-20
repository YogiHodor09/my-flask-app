def named(**kwargs):
    print(kwargs)


details = {'name': 'Yogeshwar', 'age': 28}
named(**details)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f'{arg}:{value}')


print_nicely(name='Yogeshwar', age=28)


def both(*args, **kwargs):
    print(args, kwargs)


print(both(1, 3, 5, name='Yogeshwar', age=28))
