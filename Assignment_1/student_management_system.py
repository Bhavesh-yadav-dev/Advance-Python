# user = []

# def register_user():
#     n = int(input("Enter the number of users to register: "))
#     for i in range(n):
#         name = input(f"Enter the name of user {i+1}: ")
#         roll_no = int(input(f"Enter the roll number of user {i+1}: "))
#         while any(u["roll_no"] == roll_no for u in user):
#             print(f"Roll number {roll_no} already exists.")
#             roll_no = int(input(f"Enter the roll number of user {i+1}: "))

#         marks1 = int(input(f"Enter the marks of user {i+1}: "))
#         marks2 = int(input(f"Enter the marks of user {i+1}: "))
#         marks3 = int(input(f"Enter the marks of user {i+1}: "))

      
#         total = marks1 + marks2 + marks3
#         average = total / 3

#         grade = (
#             "A" if average >= 90 else
#             "B" if average >= 75 else
#             "C" if average >= 60 else
#             "D" if average >= 40 else
#             "F"
#         )

#         user.append({
#             "name": name,
#             "roll_no": roll_no,
#             "marks1": marks1,
#             "marks2": marks2,
#             "marks3": marks3,
#             "total": total,
#             "average": average,
#             "grade": grade
#         })

#         print(f"User {i+1} registered successfully!\n")


# def display_users():
#     if not user:
#         print("No users registered.")
#         return

#     print("\nRegistered Users:")
#     for i, u in enumerate(user):
#         print(f"User {i+1}:")
#         print(f"Name: {u['name']}")
#         print(f"Roll Number: {u['roll_no']}")
#         print(f"Marks 1: {u['marks1']}")
#         print(f"Marks 2: {u['marks2']}")
#         print(f"Marks 3: {u['marks3']}")
#         print(f"Total Marks: {u['total']}")
#         print(f"Average Marks: {u['average']}") 
#         print(f"Grade: {u['grade']}")
#         print()


# def search_user(roll_no):
#     for u in user:
#         if not u["roll_no"] == roll_no:
#             print(f"No user found with roll number {roll_no}.")
#         else:
#             print(f"Name: {u['name']}")
#             print(f"Roll Number: {u['roll_no']}")
#             print(f"Marks 1: {u['marks1']}")
#             print(f"Marks 2: {u['marks2']}")
#             print(f"Marks 3: {u['marks3']}")
#             print(f"Total Marks: {u['total']}")
#             print(f"Average Marks: {u['average']}") 
#             print(f"Grade: {u['grade']}")
#             print()
        
            



# while True:
#     print("student management system\n")
#     print("1. Register User")
#     print("2. Display Users")   
#     print("3. Search User")
#     print("4. Exit")

#     n = int(input("Enter your choice: "))
#     if n == 1:
#         register_user()
#     elif n == 2:
#         display_users()
#     elif n == 3:
#         roll_no = int(input("Enter the roll number to search: "))
#         search_user(roll_no)
#     elif n == 4:
#         print("Exiting...")
#         break
#     else:
#         print("Invalid choice. Please try again.")
4
    

    
user = []


def register_users(user):
    n = int(input("Enter the number of users to register: "))

    for i in range(n):
        username = input("Enter the student name: ")
        roll_no = int(input("Enter the student roll number: "))

        while any(u["Roll_no"] == roll_no for u in user):
            print(f"Roll number {roll_no} already exists!")
            roll_no = int(input("Enter a different roll number: "))

        marks1 = int(input("Enter marks of subject 1: "))
        while marks1 < 0 or marks1 > 100:
            print("Invalid marks. Enter marks between 0 and 100.")
            marks1 = int(input("Enter marks of subject 1: "))

        marks2 = int(input("Enter marks of subject 2: "))
        while marks2 < 0 or marks2 > 100:
            print("Invalid marks. Enter marks between 0 and 100.")
            marks2 = int(input("Enter marks of subject 2: "))

        marks3 = int(input("Enter marks of subject 3: "))
        while marks3 < 0 or marks3 > 100:
            print("Invalid marks. Enter marks between 0 and 100.")
            marks3 = int(input("Enter marks of subject 3: "))

        total = marks1 + marks2 + marks3
        average = total / 3

        grade = (
            "A" if average >= 90 else
            "B" if average >= 75 else
            "C" if average >= 60 else
            "D" if average >= 40 else
            "F"
        )

        user.append({
            "username": username,
            "Roll_no": roll_no,
            "marks1": marks1,
            "marks2": marks2,
            "marks3": marks3,
            "total": total,
            "average": average,
            "grade": grade
        })

        print(f"User {i + 1} registered successfully!\n")


def display_users(user):
    if not user:
        print("No users registered.")
        return

    for i, u in enumerate(user, start=1):
        print(f"\nUser {i}:")
        print(f"Name: {u['username']}")
        print(f"Roll Number: {u['Roll_no']}")
        print(f"Marks 1: {u['marks1']}")
        print(f"Marks 2: {u['marks2']}")
        print(f"Marks 3: {u['marks3']}")
        print(f"Total Marks: {u['total']}")
        print(f"Average Marks: {u['average']:.2f}")
        print(f"Grade: {u['grade']}")
        print("-" * 30)


def search_user(user, roll_no):
    for i, u in enumerate(user, start=1):
        if u["Roll_no"] == roll_no:
            print(f"\nUser {i}:")
            print(f"Name: {u['username']}")
            print(f"Roll Number: {u['Roll_no']}")
            print(f"Marks 1: {u['marks1']}")
            print(f"Marks 2: {u['marks2']}")
            print(f"Marks 3: {u['marks3']}")
            print(f"Total Marks: {u['total']}")
            print(f"Average Marks: {u['average']:.2f}")
            print(f"Grade: {u['grade']}")
            return

    print(f"No student found with roll number {roll_no}.")

def main():
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