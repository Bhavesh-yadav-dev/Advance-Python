from components.library_record import Library_Record
from components.Add_Books import Add_Books
from components.Display_All_Books import Display_All_Books
from components.Search_Books import Search_Books
from components.Student_Registration import Student_Registration
from components.Issue_Book import Issue_Book
from components.Delete_Book import Delete_Book


def menu():
    while True:
        print("\n========== Library Management System ==========")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Delete Book")
        print("6. Student Registration")
        print("0. Exit")
        print("================================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            Add_Books()
        elif choice == "2":
            Display_All_Books()
        elif choice == "3":
            Search_Books()
        elif choice == "4":
            Issue_Book()
        elif choice == "5":
            Delete_Book()
        elif choice == "6":
            Student_Registration()
        elif choice == "7":
            Library_Record()
        elif choice == "0":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


menu()
