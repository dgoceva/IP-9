class Book:
    def __init__(self, book_name, book_code, book_price, book_year, book_author):
        self.book_name = book_name
        self.book_code = book_code
        self.book_price = book_price
        self.book_year = book_year
        self.book_author = book_author

    def __str__(self):
        return f'({self.book_code}, {self.book_name}, {self.book_author}, \
{self.book_price}, {self.book_year})'

    def __repr__(self):
        return f'({self.book_code}, {self.book_name}, {self.book_author}, \
{self.book_price}, {self.book_year})'


def sort_name(books):
    print(sorted(books, key=lambda x: x.book_name, reverse=True))


def author(books, book_author):
    print([book for book in books if book.book_author == book_author])


def search_book(books, book_code):
    for book in books:
        if book.book_code == book_code:
            print(book)
            return
    print('The book is not found')


if __name__ == '__main__':
    books = [
        Book('A1', 121, 12.34, 2022, 'BC'),
        Book('A2', 123, 34.56, 2021, 'BD'),
        Book('A3', 125, 56.78, 2021, 'AC'),
        Book('A4', 119, 12.43, 2020, 'BC'),
    ]
    sort_name(books)
    author(books, 'BC')
    search_book(books, 120)
    search_book(books, 119)
