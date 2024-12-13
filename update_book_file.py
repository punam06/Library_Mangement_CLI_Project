import add_books
import view_all_books
import restore_books_file
import update_book_file
import delete_book_file
import lend_book_file  # Import the new lend book file
from datetime import datetime

all_books = []

while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Book Update")
    print("4. Book Remove/Delete")
    print("5. Lend Book")  # New option for lending books

    all_books = restore_books_file.restore_all_books(all_books)
    
    menu = input("Select any number: ")
    
    if menu == "0":
        print("Thanks for using Library Management System ")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    elif menu == "3":
        update_book_file.update_books(all_books)
    elif menu == "4":
        delete_book_file.delete_books(all_books)
    elif menu == "5":
        lend_book_file.lend_book(all_books)  # Call the lend book function
    else:
        print("Choose a valid number")