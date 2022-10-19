def add(x, y): return x+y  # gets input and returns output


print(add(5, 7))


def double(x):
    return x*2


sequence = [1, 2, 3, 4]

doubled = [double(x) for x in sequence]  # list comphrehension

doubled = map(double, sequence)  # map(func(),list items)

# lambda
doubled = [(lambda x:x*2)(x) for x in sequence]

doubled = list(map(lambda x: x*2, sequence))


print(doubled)
