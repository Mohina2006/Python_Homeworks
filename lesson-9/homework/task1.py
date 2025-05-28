class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"Title: {self.title} | Author: {self.author} | Status: {status}"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        if not self.borrowed_books:
            return f"Member name: {self.name} | Borrowed: 0 books [None]"
        book_titles = ", ".join(book.title for book in self.borrowed_books)
        return f"Member name: {self.name} | Borrowed: {len(self.borrowed_books)} books [{book_titles}]"

class BookNotFoundException(Exception):
    """Raised when the book requested is not in the library."""
    pass

class BookAlreadyBorrowedException(Exception):
    """Raised when the book is already borrowed."""
    pass

class MemberLimitExceededException(Exception):
    """Raised when a member tries to borrow more than 3 books."""
    pass

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, book_title, member_name):
        book = next((b for b in self.books if b.title == book_title), None)
        if not book:
            raise BookNotFoundException(f"Book '{book_title}' not found in the library")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"Book '{book_title}' is already borrowed.")
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            raise Exception(f"Member '{member_name}' not found in the system.")
        if len(member.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{member.name} can't borrow more than 3 books.")
        book.is_borrowed = True
        member.borrowed_books.append(book)
        print(f"{member.name} successfully borrowed '{book.title}'.")

    def return_book(self, book_title, member_name):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            raise Exception(f"Member '{member_name}' not found.")
        book = next((b for b in member.borrowed_books if b.title == book_title), None)
        if not book:
            raise Exception(f"Book '{book_title}' is not borrowed by {member_name}.")
        book.is_borrowed = False
        member.borrowed_books.remove(book)
        print(f"{member.name} successfully returned '{book.title}'.")

def main():
    lib = Library()

    # Add books
    b1 = Book("1984", "George Orwell")
    b2 = Book("Kite Runner", "Khalid Hosseini")
    b3 = Book("As long as the Lemon trees grow", "Zoulfa Katouh")
    lib.add_book(b1)
    lib.add_book(b2)
    lib.add_book(b3)

    # Add member
    m1 = Member("Mohina")
    lib.add_member(m1)

    # Borrow books
    try:
        lib.borrow_book("1984", "Mohina")
        lib.borrow_book("Kite Runner", "Mohina")
        lib.borrow_book("As long as the Lemon trees grow", "Mohina")
        lib.borrow_book("Idiot", "Mohina")  # This will raise BookNotFoundException
    except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException, Exception) as e:
        print(f"Error: {e}")

    print(m1)
    print(b1)
    print(b2)
    print(b3)

    # Return a book and borrow it again
    lib.return_book("1984", "Mohina")
    try:
        lib.borrow_book("1984", "Mohina")
    except Exception as e:
        print(f"Error: {e}")

    print(m1)

if __name__ == "__main__":
    main()
