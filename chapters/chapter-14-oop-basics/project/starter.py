"""
Chapter 14 Project: Library Management System
See README.md in this folder for the full brief and example output.

This project is built AROUND general classes as its core organizing
principle. The Book class (__init__, instance attributes like title/author/
isbn/is_checked_out, an instance method or two, and a __str__ for readable
printing) is the real centerpiece -- every menu operation works with real
Book objects instead of a pile of separate dicts and functions. A Library
class holds the running list of Book objects and the operations that act on
that collection (add, check out, return, search, list all), matching Chapter
10's function-library-turned-class organizing pattern, just now built around
a class instead of loose functions. Fill in the numbered TODOs below.
"""


class Book:
    """One book in the library, with its own title, author, ISBN, and
    checked-out status."""

    def __init__(self, title, author, isbn, is_checked_out=False):
        # TODO 1: Set self.title, self.author, self.isbn, and
        # self.is_checked_out from the parameters above.
        pass

    def check_out(self):
        """Mark this book checked out. Returns True if it worked, False if
        the book was already checked out."""
        # TODO 2: If self.is_checked_out is already True, return False (it
        # can't be checked out again). Otherwise set self.is_checked_out to
        # True and return True.
        pass

    def return_book(self):
        """Mark this book returned. Returns True if it worked, False if the
        book wasn't checked out in the first place."""
        # TODO 3: If self.is_checked_out is already False, return False
        # (nothing to return). Otherwise set self.is_checked_out to False
        # and return True.
        pass

    def __str__(self):
        # TODO 4: Build a status string -- "checked out" if
        # self.is_checked_out else "available" -- then return an f-string
        # like: '"{title}" by {author} (ISBN {isbn}) -- {status}'.
        pass


class Library:
    """Holds the running collection of Book objects for one session and the
    operations that act on it."""

    def __init__(self):
        # TODO 5: Set self.books to an empty list. (This must live in
        # __init__, not as a class attribute -- otherwise every Library
        # instance would share the exact same list.)
        pass

    def add_book(self, title, author, isbn):
        # TODO 6: Create a new Book(title, author, isbn), append it to
        # self.books, and return it.
        pass

    def find_by_isbn(self, isbn):
        # TODO 7: Loop over self.books and return the first book whose
        # .isbn matches the isbn argument. If none match, return None.
        pass

    def search_by_title(self, keyword):
        # TODO 8: Return a list of every book in self.books where
        # keyword.lower() is found in book.title.lower().
        pass

    def search_by_author(self, keyword):
        # TODO 9: Return a list of every book in self.books where
        # keyword.lower() is found in book.author.lower().
        pass

    def all_books(self):
        # TODO 10: Return self.books.
        pass


def print_books(books):
    """Print a list of Book objects, one per line, using each book's
    __str__."""
    # TODO 11: If books is empty, print "No books to show." and return.
    # Otherwise loop over books and print f"  {book}" for each one (this
    # relies on Book.__str__ from TODO 4 to look right).
    pass


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
        # TODO 12: If title, author, or isbn is empty, print a message
        # saying all three are required. Otherwise, if
        # library.find_by_isbn(isbn) already returns a book (not None),
        # print that the ISBN already exists. Otherwise call
        # library.add_book(title, author, isbn) and print f"Added: {book}".
        pass

    elif choice == "2":
        print()
        isbn = input("ISBN of the book to check out: ").strip()
        # TODO 13: Look the book up with library.find_by_isbn(isbn). If it's
        # None, print that no book was found with that ISBN. Otherwise call
        # book.check_out() -- if it returns True, print f"Checked out:
        # {book}"; if False, print that the book is already checked out.
        pass

    elif choice == "3":
        print()
        isbn = input("ISBN of the book to return: ").strip()
        # TODO 14: Same lookup pattern as TODO 13, but call
        # book.return_book() instead -- True prints f"Returned: {book}",
        # False prints that the book wasn't checked out.
        pass

    elif choice == "4":
        print()
        keyword = input("Title keyword to search for: ").strip()
        # TODO 15: If keyword is empty, print a message asking for a
        # non-empty keyword. Otherwise call library.search_by_title(keyword),
        # print how many matches were found, and call print_books(...) on
        # the result.
        pass

    elif choice == "5":
        print()
        keyword = input("Author keyword to search for: ").strip()
        # TODO 16: Same as TODO 15, but call library.search_by_author(keyword)
        # instead.
        pass

    elif choice == "6":
        print()
        # TODO 17: Print f"All books ({len(library.all_books())}):" then
        # call print_books(library.all_books()).
        pass

    elif choice == "7":
        print()
        print("Goodbye!")
        break

    else:
        print("Please choose 1-7.")
