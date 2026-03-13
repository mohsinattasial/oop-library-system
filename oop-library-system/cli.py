from datetime import date
from src.library import Library
from src.models import SimpleFinePolicy

library = Library(SimpleFinePolicy())

while True:

    print("\n1 Add Book")
    print("2 Add Member")
    print("3 Borrow Book")
    print("4 Return Book")
    print("5 Exit")

    choice = input("Choose: ")

    if choice == "1":

        book_id = input("Book ID: ")
        title = input("Title: ")
        author = input("Author: ")

        library.add_book(book_id, title, author)
        print("Book added")

    elif choice == "2":

        member_id = input("Member ID: ")
        name = input("Name: ")

        library.add_member(member_id, name)
        print("Member added")

    elif choice == "3":

        member_id = input("Member ID: ")
        book_id = input("Book ID: ")

        library.borrow_book(member_id, book_id, date.today())
        print("Book borrowed")

    elif choice == "4":

        member_id = input("Member ID: ")
        book_id = input("Book ID: ")

        fine = library.return_book(member_id, book_id, date.today())
        print("Book returned")
        print("Fine:", fine)

    elif choice == "5":
        break