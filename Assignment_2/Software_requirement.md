
# Advanced Python Programming

## Assignment 01: Library Management System Using Python

| **Assignment Type** | Individual Project |
|---|---|
| **Difficulty** | Basic to Intermediate |
| **Technology** | Python and JSON |
| **Submission** | Source Code + Documentation |

## 1. Problem Statement

Develop a menu-driven Library Management System using Python. The library needs a computerized system to manage books, maintain student records, issue books, return books, and store all information permanently.

Your task is to develop a Python application that performs these operations using fundamental and intermediate Python programming concepts. The application must store its data in JSON files so that information remains available even after the program is closed.

## 2. Functional Requirements

### Module 1: Main Menu

Display the following menu:

1. Add New Book
2. Display All Books
3. Search for a Book
4. Register a Student
5. Issue a Book
6. Return a Book
7. Display Issued Books
8. Delete a Book
9. Exit

The application should continue running until the user selects Exit.

### Module 2: Add New Book

- Allow the librarian to enter Book ID, Book Name, Author Name, Category, and Number of Copies.
- Book ID must be unique.
- Number of copies must be greater than zero.
- Store book information using a Python dictionary and maintain all books in a list.

### Module 3: Display All Books

- Display Book ID, Book Name, Author, Category, and Available Copies in a readable format.
- Display an appropriate message if no books are available.

### Module 4: Search for a Book

- Allow users to search using Book ID, Book Name, or Author Name.
- Search should work regardless of uppercase or lowercase input.

### Module 5: Student Registration

- Register Student ID, Student Name, Department, and Contact Number.
- Student ID must be unique.
- Store student information using dictionaries and maintain student records in a JSON file.

### Module 6: Issue a Book

- Allow the librarian to issue a book to a registered student.
- Verify that the student and book exist and that copies are available.
- Reduce the available book count after issuing.
- Record Student ID, Book ID, and Issue Date.

### Module 7: Return a Book

- Verify the issue record.
- Update the available book count.
- Remove or update the corresponding issue record.

### Module 8: Delete a Book

- Allow the librarian to delete a book using its Book ID.
- Verify whether the book exists.
- Do not delete a book that is currently issued.
- Display an appropriate confirmation message.

## 3. Technical Requirements

Your application must demonstrate the following Python concepts:

| **Python Concept** | **Required Implementation** |
|---|---|
| Variables and Data Types | Store book and student details |
| Conditional Statements | Validate user choices and records |
| Loops | Build the menu-driven application |
| Functions | Create separate functions for each operation |
| Lists | Maintain collections of books and students |
| Dictionaries | Represent individual records |
| String Handling | Search and format book information |
| Modular Programming | Organize functionality into functions/modules |
| File Handling | Read and write data files |
| JSON | Store and retrieve persistent records |
| Input Validation | Prevent invalid entries and duplicate IDs |

## 4. JSON File Structure

Use three separate JSON files:

- `books.json` – stores all book information.
- `students.json` – stores registered student information.
- `issued_books.json` – stores book issue records.

Example structure for `books.json`:

```json
[
    {
        "book_id": "B101",
        "book_name": "Python Programming",
        "author": "John Smith",
        "category": "Programming",
        "available_copies": 5
    }
]
```

## 5. Additional Challenges (Intermediate Level)

- Display the total number of books in the library.
- Display the total number of registered students.
- Display the most frequently issued book.
- Sort books alphabetically by book name.
- Prevent a student from issuing more than three books simultaneously.
- Display a report of all currently issued books.

## 6. Submission Requirements

- Complete Python source code.
- Three JSON data files.
- Screenshots of the application running.
- A short project report explaining how the application works.

## 7. Evaluation Criteria

| **Evaluation Component** | **Marks** |
|---|---:|
| Menu and application structure | 10 |
| Functions and modular programming | 15 |
| Lists, dictionaries and string handling | 15 |
| File handling and JSON integration | 20 |
| Book and student management | 15 |
| Issue and return functionality | 15 |
| Additional features and code quality | 10 |
| **TOTAL** | **100** |

## 8. Important Instructions

- Do not use any database such as MySQL or SQLite.
- Do not use Django, Flask, or FastAPI.
- Do not use external libraries.
- Use Python's built-in `json` module.
- Organize the code using meaningful function names.
- Avoid writing the entire application inside a single function.
- Ensure that data remains stored after restarting the application.

## Learning Objective

Develop a functional Library Management System by integrating the Python programming concepts learned throughout the course.

---

*— End of Assignment —*
