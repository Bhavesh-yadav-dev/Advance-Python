from components.database import Save_Issued_Books , Save_Books , Issued_Book , Student_Details , Books
from datetime import datetime


def Issue_Book():
    if not Books:
        print("No books available in the library.")
        return

    Student_Id = input("Enter Student ID: ").strip().lower()
    if Student_Id not in Student_Details:
        print("Student ID not found. Please register the student first.")
        return
    
    Book_ID = input("Enter Book ID: ").strip().lower()
    if Book_ID not in Books:
        print("Book ID not found in the library.")
        return

    Details = Books[Book_ID]

    if Details['Issued_Copies'] >= Details['Total_Copies']:
        print("No available copies of the book to issue.")
        return

    if Details['Issued_Copies'] < Details['Total_Copies']:
        Books[Book_ID]['Issued_Copies'] += 1
        Issued_Date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Issued_Book.append({
            "Book_ID": Book_ID,
            "Student_ID": Student_Id,
            "Issued_Date": Issued_Date,
            "Return_Date": None,
        })
    Save_Books(Books)
    Save_Issued_Books(Issued_Book)
    print("Book issued successfully.")
    print(f"Book: {Details['Book_Name']}")
    print(f"Issued To: {Student_Details[Student_Id]['Student_Name']}")
    print(f"Issued Date & Time: {Issued_Date}")
    print("Status: Issued Successfully")