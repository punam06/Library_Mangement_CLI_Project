import json
from datetime import datetime

def return_book(all_books):
    book_title = input("Enter Book Title to Return: ")
    borrower_name = input("Enter Borrower's Name: ")

    # Load lend info
    lend_info = []
    try:
        with open("lend_info.json", "r") as lend_file:
            for line in lend_file:
                lend_info.append(json.loads(line.strip()))
    except FileNotFoundError:
        print("No lend information found.")
        return all_books

    for book in all_books:
        if book["title"] == book_title:
            for lend in lend_info:
                if lend["book_title"] == book_title and lend["borrower_name"] == borrower_name:
                    # Increase the quantity of the book
                    book["quantity"] += 1

                    # Remove the lend info
                    lend_info.remove(lend)

                    # Save updated lend info back to the file
                    with open("lend_info.json", "w") as lend_file:
                        for lend in lend_info:
                            json.dump(lend, lend_file)
                            lend_file.write("\n")  # New line for each entry

                    print("Book returned successfully.")
                    # Save the updated book list
                    save_all_books(all_books)
                    return all_books

            print("Lend information not found for this borrower.")
            return all_books

    print("Book Not Found")
    return all_books