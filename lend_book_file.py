import json
from datetime import datetime, timedelta

def lend_book(all_books):
    borrower_name = input("Enter Borrower's Name: ")
    borrower_phone = input("Enter Borrower's Phone Number: ")
    book_title = input("Enter Book Title to Lend: ")

    for book in all_books:
        if book["title"] == book_title:
            if book["quantity"] > 0:
                # Decrease the quantity of the book
                book["quantity"] -= 1

                # Set the return due date (e.g., 14 days from now)
                return_due_date = datetime.now() + timedelta(days=14)

                # Create lend info
                lend_info = {
                    "borrower_name": borrower_name,
                    "borrower_phone": borrower_phone,
                    "book_title": book_title,
                    "return_due_date": return_due_date.strftime("%d-%m-%Y %H:%M:%S")
                }

                # Save lend info to a file
                with open("lend_info.json", "a") as lend_file:
                    json.dump(lend_info, lend_file)
                    lend_file.write("\n")  # New line for each entry

                print("Book lent successfully. Return due date is:", lend_info["return_due_date"])
                # Save the updated book list
                save_all_books(all_books)
                return all_books
            else:
                print("There are not enough books available to lend.")
                return all_books

    print("Book Not Found")