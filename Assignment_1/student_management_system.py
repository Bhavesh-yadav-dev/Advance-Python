from student_module import *

def main():
    create_db() 
    user = load_user()
    while True:
        print("\nStudent Management System")
        print("1. Register User")
        print("2. Display Users")
        print("3. Search User")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            register_users(user)

        elif choice == 2:
            display_users(user)

        elif choice == 3:
            roll_no = int(input("Enter the roll number to search: "))
            search_user(user, roll_no)

        elif choice == 4:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


main()
