import json
import os

# Create JSON database if it doesn't exist
DB_FILE = "user_db.json"

def create_db():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as file:
            json.dump([], file)

def save_user(user):
    with open(DB_FILE, "w") as file:
        json.dump(user, file, indent=4)

def load_user():
    with open(DB_FILE, "r") as file:
        return json.load(file)


# Initialize database
create_db()
user = load_user()


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

        
        # Load the latest user data before saving

     
        save_user(user)

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