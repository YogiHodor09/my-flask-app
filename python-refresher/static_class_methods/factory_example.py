class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name, book_type, weight) -> None:
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return (
            f'<Book {self.name} is type of {self.book_type} with {self.weight} gms.')

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight+100)

    @classmethod
    def softcover(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


book = Book.hardcover('Harry Potter', 1500)
lite = Book.softcover('Python', 700)
print(book)
print(lite)
