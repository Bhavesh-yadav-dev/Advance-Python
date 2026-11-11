import os
import json

def initialize_database():
    if not os.path.exists("Books.json"):
        with open("Books.json", "w") as file:
            json.dump({}, file)

    if not os.path.exists("Issued_Books.json"):
        with open("Issued_Books.json", "w") as file:
            json.dump([], file)

    if not os.path.exists("Student_Details.json"):
        with open("Student_Details.json", "w") as file:
            json.dump({}, file)


def Save_Books(book_data):
    with open("Books.json", "w") as file:
        json.dump(book_data, file, indent=4)

def Load_Books():
    with open("Books.json", "r") as file:
        return json.load(file)

def Save_Issued_Books(issued_books):
    with open("Issued_Books.json", "w") as file:
        json.dump(issued_books, file, indent=4)

def Load_Issued_Books():
    with open("Issued_Books.json", "r") as file:
        return json.load(file)

def Save_Student_Details(student_details):
    with open("Student_Details.json", "w") as file:
        json.dump(student_details, file, indent=4)

def Load_Student_Details():
    with open("Student_Details.json", "r") as file:
        return json.load(file)


initialize_database()

Books = Load_Books()
Issued_Book = Load_Issued_Books()
Student_Details = Load_Student_Details()