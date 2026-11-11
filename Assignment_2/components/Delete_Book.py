from components.database import Save_Books, Books, Issued_Book


def Delete_Book():
    if not Books:
        print("No books available in the library.")
        return

    Book_ID = input("Enter Book ID to delete: ").strip().lower()

    if Book_ID not in Books:
        print("Book ID not found in the library.")
        return

    # Check if the book has any copies currently issued
    issued_count = Books[Book_ID]['Issued_Copies']
    if issued_count > 0:
        print(f"Cannot delete '{Books[Book_ID]['Book_Name']}'. It has {issued_count} copy/copies currently issued.")
        return

    book_name = Books[Book_ID]['Book_Name']

    confirm = input(f"Are you sure you want to delete '{book_name}'? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Deletion cancelled.")
        return

    del Books[Book_ID]
    Save_Books(Books)

    print(f"Book '{book_name}' deleted successfully.")
