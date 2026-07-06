"""
Chapter 14 Project: Library Management System -- reference solution.
See README.md in this folder for the full brief and example output.

This project is built AROUND general classes as its core organizing
principle. The Book class (__init__, instance attributes like title/author/
isbn/is_checked_out, an instance method or two, and a __str__ for readable
printing) is the real centerpiece -- every menu operation works with real
Book objects instead of a pile of separate dicts and functions. A Library
class holds the running list of Book objects and the operations that act on
that collection (add, check out, return, search, list all), matching Chapter
10's function-library-turned-class organizing pattern, just now built around
a class instead of loose functions.
"""


class Book:
    """One book in the library, with its own title, author, ISBN, and
    checked-out status."""

    def __init__(self, title, author, isbn, is_checked_out=False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = is_checked_out

    def check_out(self):
        """Mark this book checked out. Returns True if it worked, False if
        the book was already checked out."""
        if self.is_checked_out:
            return False
        self.is_checked_out = True
        return True

    def return_book(self):
        """Mark this book returned. Returns True if it worked, False if the
        book wasn't checked out in the first place."""
        if not self.is_checked_out:
            return False
        self.is_checked_out = False
        return True

    def __str__(self):
        status = "checked out" if self.is_checked_out else "available"
        return f'"{self.title}" by {self.author} (ISBN {self.isbn}) -- {status}'


class Library:
    """Holds the running collection of Book objects for one session and the
    operations that act on it."""

    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        return book

    def find_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def search_by_title(self, keyword):
        return [b for b in self.books if keyword.lower() in b.title.lower()]

    def search_by_author(self, keyword):
        return [b for b in self.books if keyword.lower() in b.author.lower()]

    def all_books(self):
        return self.books


def print_books(books):
    """Print a list of Book objects, one per line, using each book's
    __str__."""
    if not books:
        print("No books to show.")
        return
    for book in books:
        print(f"  {book}")


# --- Session state ---
print("=== Library Management System ===")
library = Library()

# Seed a few starting books so the menu has something to work with right away.
library.add_book("Dune", "Frank Herbert", "0001")
library.add_book("The Hobbit", "J.R.R. Tolkien", "0002")
library.add_book("Foundation", "Isaac Asimov", "0003")
print(f"Loaded {len(library.all_books())} book(s) into the library.")

while True:
    print()
    print("1. Add a book")
    print("2. Check out a book")
    print("3. Return a book")
    print("4. Search by title")
    print("5. Search by author")
    print("6. List all books")
    print("7. Quit")
    choice = input("Choose an option (1-7): ").strip()

    if choice == "1":
        print()
        title = input("Title: ").strip()
        author = input("Author: ").strip()
        isbn = input("ISBN: ").strip()
        if not title or not author or not isbn:
            print("Title, author, and ISBN are all required.")
        elif library.find_by_isbn(isbn) is not None:
            print(f"A book with ISBN {isbn} already exists.")
        else:
            book = library.add_book(title, author, isbn)
            print(f"Added: {book}")

    elif choice == "2":
        print()
        isbn = input("ISBN of the book to check out: ").strip()
        book = library.find_by_isbn(isbn)
        if book is None:
            print(f"No book found with ISBN {isbn}.")
        elif book.check_out():
            print(f"Checked out: {book}")
        else:
            print(f'"{book.title}" is already checked out.')

    elif choice == "3":
        print()
        isbn = input("ISBN of the book to return: ").strip()
        book = library.find_by_isbn(isbn)
        if book is None:
            print(f"No book found with ISBN {isbn}.")
        elif book.return_book():
            print(f"Returned: {book}")
        else:
            print(f'"{book.title}" was not checked out.')

    elif choice == "4":
        print()
        keyword = input("Title keyword to search for: ").strip()
        if not keyword:
            print("Please enter a non-empty keyword.")
        else:
            matches = library.search_by_title(keyword)
            print(f"{len(matches)} match(es):")
            print_books(matches)

    elif choice == "5":
        print()
        keyword = input("Author keyword to search for: ").strip()
        if not keyword:
            print("Please enter a non-empty keyword.")
        else:
            matches = library.search_by_author(keyword)
            print(f"{len(matches)} match(es):")
            print_books(matches)

    elif choice == "6":
        print()
        print(f"All books ({len(library.all_books())}):")
        print_books(library.all_books())

    elif choice == "7":
        print()
        print("Goodbye!")
        break

    else:
        print("Please choose 1-7.")
