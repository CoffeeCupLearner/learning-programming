class Book:
    """
    This class represents a book.
    """

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    This class represents an electronic book (eBook).
    """

    def __init__(self, title, author, size):
        super().__init__(title, author)
        self.size = size

    def __str__(self):
        return f"{super().__str__()} (eBook, size: {self.size} MB)"


class PaperBook(Book):
    """
    This class represents a paper book.
    """

    def __init__(self, title, author, num_pages):
        super().__init__(title, author)
        self.num_pages = num_pages

    def __str__(self):
        return f"{super().__str__()} (Paperback, {self.num_pages} pages)"


class Library:
    """
    This class represents a library.
    """

    def __init__(self):
        self.books = []

    def add_books(self, book):
        """Adds a book to the library.

        Args:
            book: A Book object.
        """
        self.books.append(book)

    def get_num_books(self):
        """Returns the number of books in the library.

        Returns:
            int: The number of books.
        """
        return len(self.books)

    def print_books(self):
        """Prints the details of all books in the library."""
        for book in self.books:
            print(book)


my_pb = PaperBook("Journey", "Emha", 321)
my_eb1 = EBook("Beyond", "Ainun", 101)
my_eb2 = EBook("Fantasy", "Nadjib", 786)

aadc = Library()
aadc.add_books(my_pb)
aadc.add_books(my_eb1)
aadc.add_books(my_eb2)

aadc.print_books()
print(f"Number of books: {aadc.get_num_books()}")
