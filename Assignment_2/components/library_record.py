from components.database import Books, Student_Details

def Library_Record():
    if not Books:
        print("No books available in the library.")
        return
    
    total_book = len(Books)
    
    total_students = len(Student_Details)
    
    print("\n--- Library Record ---")
    print(f"Total Unique Book Titles : {total_book}")
    print(f"Total Registered Students : {total_students}")
    print("-----------------------")