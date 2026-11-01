import json
import os

if not os.path.exists("Books.json"):
    with open("Books.json", "w") as file:
        json.dump({}, file)

if not os.path.exists("Issued_Books.json"):
    with open("Issued_Books.json", "w") as file:
        json.dump([], file)

def load_Books_data():
    with open("Books.json", "r") as file:
        data = json.load(file)
    return data
def save_Books_data(data):
    with open("Books.json", "w") as file:
        json.dump(data, file, indent=4)

def load_Issued_Books_data():
    with open("Issued_Books.json", "r") as file:
        data = json.load(file)
    return data

def save_Issued_Books_data(data):
    with open("Issued_Books.json", "w") as file:
        json.dump(data, file, indent=4)


Books = load_Books_data()
Issued_Books = load_Issued_Books_data()

def Add_NewBook():
    book_id = int(input("Enter Book ID: "))
    while book_id in Books:
        print("Book ID already exists. Please enter a unique Book ID.")
        book_id = int(input("Enter Book ID: "))
    book_title = input("Enter Book Title: ")
    book_author = input("Enter Book Author: ")
    total = int(input("Enter Total Copies: "))
    while total < 0:
        print("Total copies cannot be negative. Please enter a valid number.")
        total = int(input("Enter Total Copies: "))
    issued = 0
    available = total - issued


    Books[book_id] = {
        
        "title": book_title,
        "author": book_author,
        "total": total,
        "issued": issued,
        "available": total
    }

    save_Books_data(Books)

    print("Book added successfully.")


def Display_Books():
    if not Books:
        print("No books available.")
        return

    for books_id in Books.items():
        print(f"Book ID: {books_id[0]}")
        print(f"Title: {books_id[1]['title']}")
        print(f"Author: {books_id[1]['author']}")
        print(f"Total Copies: {books_id[1]['total']}")
        print(f"Issued Copies: {books_id[1]['issued']}")
        print(f"Available Copies: {books_id[1]['available']}")
        print("------------------------")

def Search_Book():
    search = str(input("Enter Book ID to Title: "))
    
    for book_id, details in Books.items():
        if str(book_id) == search or details['title'].lower() == search.lower():
            print(f"Book ID: {book_id}")
            print(f"Title: {details['title']}")
            print(f"Author: {details['author']}")
            print(f"Total Copies: {details['total']}")
            print(f"Issued Copies: {details['issued']}")
            print(f"Available Copies: {details['available']}")
            return

    print("Book not found.")

def Issue_Book():
    student_ID = int(input("Enter Student ID: "))
    student_name = input("Enter Student Name: ")
    book_ID = int(input("Enter Book ID: "))

    for books_id , details in Books.items():
       if books_id == book_ID and details['available'] > 0:
            details['issued'] += 1
            details['available'] -= 1
            Issued_Books.append({
                'student_ID': student_ID,
                'student_name': student_name,
                'book_ID': book_ID,
                'book_title': details['title']
            })
            save_Books_data(Books)
            save_Issued_Books_data(Issued_Books)
            print("Book issued successfully.")
            return

    print("Book not found or no available copies.")


def Return_Book():
    student_ID = int(input("Enter Student ID: "))
    book_ID = int(input("Enter Book ID: "))

    for issued_book in Issued_Books:
        if issued_book['student_ID'] == student_ID and issued_book['book_ID'] == book_ID:
            Issued_Books.remove(issued_book)
            Books[book_ID]['issued'] -= 1
            Books[book_ID]['available'] += 1
            save_Books_data(Books)
            save_Issued_Books_data(Issued_Books)
            print("Book returned successfully.")
            return

    print("No record found for the given Student ID and Book ID.")

def Display_All_Available_Books():
    
    if not Books:
        print("No books available.")
        return

    for book_id, details in Books.items():
        if details['available'] > 0:
            print(f"Book ID: {book_id}")
            print(f"Title: {details['title']}")
            print(f"Author: {details['author']}")
            print(f"Total Copies: {details['total']}")
            print(f"Issued Copies: {details['issued']}")
            print(f"Available Copies: {details['available']}")
            print("------------------------")
        else:
            print(f"No available copies for Book ID: {book_id}")

def Display_Issued_Books():
    if not Issued_Books:
        print("No books have been issued.")
        return

    for issued_book in Issued_Books:
        print(f"Student ID: {issued_book['student_ID']}")
        print(f"Student Name: {issued_book['student_name']}")
        print(f"Book ID: {issued_book['book_ID']}")
        print(f"Book Title: {issued_book['book_title']}")
        print("------------------------")


def main():
    while True:
        print("\nLibrary Management System\n")
        
        print("1. Add New Book\n2. Display All Books\n3. Search Book\n4. Issue Book\n5. Return Book\n6. Display All Available Books\n7. Display Issued Books\n8. Exit\n\n")

        choice = int(input("enter your choice: "))

        if choice == 1:
            Add_NewBook()   
        elif choice == 2:
            Display_Books()
        elif choice == 3:
            Search_Book()
        elif choice == 4:
            Issue_Book()
        elif choice == 5:
            Return_Book()   
        elif choice == 6:
            Display_All_Available_Books()
        elif choice == 7:
            Display_Issued_Books()
        elif choice == 8:
            print("Exiting the program.")
            break
        
main()