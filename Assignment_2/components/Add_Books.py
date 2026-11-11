
from components.database import Save_Books, Books

def Add_Books():

    NumberOfBooks = int(input("Enter the number of books you want to add: "))

    for i in range(NumberOfBooks):

        print(f"Adding book {i + 1}...")

        Book_ID = input("Enter Book ID: ").strip().lower()

        while Book_ID in Books:
            print("Book ID already exists!")
            Book_ID = input("Enter unique Book ID: ").strip().lower()

        Book_Name = input("Enter Book Name: ").strip()
        Author_Name = input("Enter Author Name: ").strip()
        Category = input("Enter Category: ").strip()

        Number_of_Copies = int(input("Enter Number of Copies: "))
        while Number_of_Copies <= 0:
            print("Number of copies must be positive.")
            Number_of_Copies = int(input("Enter Number of Copies: "))

        Books[Book_ID] = {
            "Book_Name": Book_Name, 
            "Author_Name": Author_Name,
            "Category": Category,
            "Total_Copies": Number_of_Copies,
            "Issued_Copies": 0
        }

        print(f"---------- Book {i + 1} Added Successfully ----------\n")

    Save_Books(Books)
