students = {}

def add_student():
    roll_no = input("Enter roll number: ")

    if roll_no in students:
        print(f"Student with roll number {roll_no} already exists.")
        return
    
    name = input("Enter name: ")

    marks = []
    for i in range(1,4):
        mark = float(input(f"Enter marks for subject {i}: "))
        while mark < 0 or mark > 100:
            print("Invalid marks. Please enter a value between 0 and 100.")
            mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)


    students[roll_no] = {
        "name": name, 
        "marks": marks
    }

    print("student added successfully.")


def display_students():
    if not students:
        print("No students registered.")
        return

    for roll_no, details in students.items():
        print(f"Roll Number: {roll_no}")
        print(f"Name: {details['name']}")
        print(f"Marks: {details['marks']}")

def calculate_results():
    if not students:
        print("No students registered.")
        return

    for roll_no, details in students.items():
        marks = details['marks']
        total = sum(marks)
        average = total / len(marks)
        grade = (
            "A" if average >= 90 else
            "B" if average >= 75 else
            "C" if average >= 60 else
            "D" if average >= 40 else
            "F"
        )
        print(f"\nResults for Roll Number: {roll_no}")
        print(f"Name: {details['name']}")
        print(f"\nRoll Number: {roll_no}")
        print(f"Name: {details['name']}")
        print(f"Total Marks: {total}")
        print(f"Average Marks: {average}")
        print(f"Grade: {grade}")


def search_student():
    roll_no =  input("Enter roll number to search: ")

    if roll_no in students:
        details = students[roll_no]
        print(f"Roll Number: {roll_no}")
        print(f"Name: {details['name']}")
        print(f"Marks: {details['marks']}")
    else:
        print(f"No student found with roll number {roll_no}.")

def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Calculate Results")
        print("4. Search Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            calculate_results()
        elif choice == '4':
            search_student()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")



main()