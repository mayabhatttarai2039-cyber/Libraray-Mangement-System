class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
    def display_info(self):
        print(f"Title: {self.title} | Author: {self.author} | ISBN: {self.isbn} | Status: {self.is_available}")
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library shelf.")
    def list_books(self):
        if self.books == []:
            print("The library has no books right now.")
        else:
            for book in self.books:
                book.display_info()

my_library = Library()

while True:
    print("\n---Library Menu ---")
    print("1. Add a New Book")
    print("2. List all books")
    print("3. Exit system")
    choice = input("Enter your choice(1-3): ")
    if choice == "1":
        title = input("Enter book title:")
        author = input("Enter name of the author: ")
        isbn = input("Enter book ISBN: ")
        new_book = Book(title, author, isbn)
        my_library.add_book(new_book)
    elif choice == "2":
        print("\n---Current Inventory -----")
        my_library.list_books()
    elif choice == "3":
        print("Thank you for using the library system. Adieu!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

