from components.database import *
from datetime import datetime


def Return_Book():
        if not Issued_Book:
            print("No books have been issued yet.")
            return
    
        Student_Id = input("Enter Student ID: ").strip().lower()
        if Student_Id not in Student_Details:
            print("Student ID not found. Please register the student first.")
            return

        Book_ID = input("Enter Book ID: ").strip().lower()
        if Book_ID not in Books:
            print("Book ID not found in the library.")
            return

        for issued_book , Details in enumerate(Issued_Book):
            if Details['Book_ID'] == Book_ID and Details['Student_ID'] == Student_Id:
                if Details['Return_Date'] is not None:
                    print("This book has already been returned.")
                    return

                Return_Date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                Issued_Book[issued_book]['Return_Date'] = Return_Date
                Books[Book_ID]['Issued_Copies'] -= 1
                Save_Books(Books)
                Save_Issued_Books(Issued_Book)
                print("Book returned successfully.")
                print(f"Book: {Books[Book_ID]['Book_Name']}")
                print(f"Returned By: {Student_Details[Student_Id]['Student_Name']}")
                print(f"Return Date & Time: {Return_Date}")
                print("Status: Returned Successfully")
                return

        