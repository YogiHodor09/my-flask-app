from unicodedata import name


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:  # returns python class obj into str
        return f'Person {self.name},{self.age} years old.'

    def __repr__(self) -> str:  # re-create original obj , re-initiate
        return f'<Person {self.name},{self.age} years old>.'


yogesh = Person('Yogesh', 28)

print(yogesh)
