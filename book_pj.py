class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'{self.title} by {self.author}'


class BookCase:
    def __init__(self, books=None):
        self.books = books

    @classmethod
    def create_books_case(cls, book_list):
        book = []
        for title, author in book_list:
            book.append(Book(title, author))
        return cls(book)


b = BookCase.create_books_case([('machine', 'mh.ahmad'), ('string', 'mohammad')])
print(b)
print(b.books)
print(str(b.books[0]))
