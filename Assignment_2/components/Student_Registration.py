from components.database import Student_Details, Save_Student_Details

def Student_Registration():
    NumberOfStudents = int(input("Enter the number of students you want to register: "))

    for i in range(NumberOfStudents):
        print(f"Registering student {i + 1}...")
        Student_ID = input("Enter Student ID: ").strip().lower()
        while Student_ID in Student_Details:
            print("Student ID already exists!")
            Student_ID = input("Enter unique Student ID: ").strip().lower()
        Student_Name = input("Enter Student Name: ").strip().lower()
        Department = input("Enter Department: ").strip().lower()

        Contact_Number = input("Enter Contact Number: ").strip()
        while not Contact_Number.isdigit() or len(Contact_Number) != 10:
            print("Invalid contact number! Please enter a 10-digit number.")
            Contact_Number = input("Enter Contact Number: ").strip()


        Student_Details[Student_ID] = {
            "Student_Name": Student_Name,       
            "Department": Department,
            "Contact_Number": Contact_Number,
            "Issued_Count": 0    
        }
        Save_Student_Details(Student_Details)
        print(f"---------- Student {i + 1} Registered Successfully ----------\n")   