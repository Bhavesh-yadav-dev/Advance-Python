# developed.md — Assignment 2: Library Management System

## Project Overview

| **Field** | **Detail** |
|---|---|
| Assignment | Library Management System |
| Technology | Python, JSON |
| Structure | Modular (separate file per feature) |
| Data Storage | Books.json, Student_Details.json, Issued_Books.json |

---

## Requirement vs Development Comparison

### Module 1: Main Menu

| Requirement | Status | Notes |
|---|---|---|
| Menu-driven application | Done | `main.py` has a `while True` loop with numbered options |
| Runs until user selects Exit | Done | Option `0` breaks the loop |
| All menu options wired correctly | Done | All 8 options mapped, no duplicates, no dead code |

---

### Module 2: Add New Book

| Requirement | Status | Notes |
|---|---|---|
| Enter Book ID, Name, Author, Category, Copies | Done | `Add_Books.py` collects all fields |
| Book ID must be unique | Done | `while Book_ID in Books` loop re-prompts |
| Number of copies must be > 0 | Done | Validated with a while loop |
| Store using dictionary | Done | Each book stored as a dict inside `Books` |

---

### Module 3: Display All Books

| Requirement | Status | Notes |
|---|---|---|
| Show Book ID, Name, Author, Category, Available Copies | Done | `Display_All_Books.py` prints all fields |
| Message if no books available | Done | Prints "No books available in the library." |

---

### Module 4: Search for a Book

| Requirement | Status | Notes |
|---|---|---|
| Search by Book ID | Done | Compared directly |
| Search by Book Name | Done | Case-insensitive with `.lower()` |
| Search by Author Name | Done | Case-insensitive with `.lower()` |
| Message if not found | Done | Prints after the loop if `found` is still False |

---

### Module 5: Student Registration

| Requirement | Status | Notes |
|---|---|---|
| Register Student ID, Name, Department, Contact | Done | `Student_Registration.py` collects all fields |
| Student ID must be unique | Done | `while Student_ID in Student_Details` loop |
| Validate Contact Number | Done | 10-digit check with `.isdigit()` and `len()` |
| Store in JSON file | Done | Saved to `Student_Details.json` |

---

### Module 6: Issue a Book

| Requirement | Status | Notes |
|---|---|---|
| Verify student exists | Done | Checked against `Student_Details` |
| Verify book exists | Done | Checked against `Books` |
| Verify copies are available | Done | `Issued_Copies < Total_Copies` |
| Reduce available count after issuing | Done | `Issued_Copies += 1` saved to `Books.json` |
| Record Student ID, Book ID, Issue Date | Done | Appended to `Issued_Books.json` with timestamp |
| Limit: max 3 books per student | Done | Extra challenge implemented |

---

### Module 7: Return a Book

| Requirement | Status | Notes |
|---|---|---|
| Verify the issue record exists | Done | Loops through `Issued_Book` to find matching record |
| Check if already returned | Done | Checks `Return_Date is not None` |
| Update available book count | Done | `Issued_Copies -= 1` saved to `Books.json` |
| Update student issued count | Done | `Issued_Count -= 1` saved to `Student_Details.json` |
| Record return date | Done | Sets `Return_Date` with current timestamp |
| Update issue record | Done | Updates record in-place and saves to `Issued_Books.json` |

---

### Module 8: Delete a Book

| Requirement | Status | Notes |
|---|---|---|
| Delete by Book ID | Done | `Delete_Book.py` removes from `Books` dict |
| Verify book exists | Done | Checked before deletion |
| Block deletion if book is currently issued | Done | Checks `Issued_Copies > 0` |
| Confirmation message | Done | Asks `yes/no` before deleting |

---

## Additional / Extra Features

| Feature | Requirement | Status |
|---|---|---|
| Total unique book titles | Additional challenge | Done — `library_record.py` |
| Total registered students | Additional challenge | Done — `library_record.py` |
| Prevent issuing > 3 books per student | Additional challenge | Done — `Issue_Book.py` |
| Most frequently issued book | Additional challenge | Not implemented |
| Sort books alphabetically | Additional challenge | Not implemented |
| Display all issued books | Additional challenge | Not implemented |

---

## Technical Requirements Coverage

| Python Concept | Requirement | Status |
|---|---|---|
| Variables and Data Types | Store book/student details | Done |
| Conditional Statements | Validate choices and records | Done |
| Loops | Menu-driven application | Done |
| Functions | Separate function per operation | Done |
| Lists | Collections (`Issued_Book` is a list) | Done |
| Dictionaries | Individual records | Done |
| String Handling | Search, format, `.lower()`, `.strip()` | Done |
| Modular Programming | One file per feature inside `components/` | Done |
| File Handling | Read/write JSON files | Done |
| JSON | `json.load` / `json.dump` via `database.py` | Done |
| Input Validation | Duplicate IDs, copy count, contact number | Done |

---

## File Structure

```
Assignment_2/
│
├── main.py                          # Menu loop, entry point
├── Books.json                       # Persistent book data
├── Issued_Books.json                # Persistent issued records
├── Student_Details.json             # Persistent student data
├── Software_requirement.md          # Original requirements
├── developed.md                     # This file
│
└── components/
    ├── database.py                  # Load/Save functions + shared dicts
    ├── Add_Books.py                 # Module 2
    ├── Display_All_Books.py         # Module 3
    ├── Search_Books.py              # Module 4
    ├── Student_Registration.py      # Module 5
    ├── Issue_Book.py                # Module 6
    ├── Return_Book.py               # Module 7
    ├── Delete_Book.py               # Module 8
    └── library_record.py            # Extra: summary stats
```

---


---

## What is Pending

| Item | Priority |
|---|---|
| Display all issued books (menu option) | Medium — required in assignment |
| Most frequently issued book | Low — optional challenge |
| Sort books alphabetically | Low — optional challenge |

---


