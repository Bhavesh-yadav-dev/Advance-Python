from components.database import  Books

def Search_Books():
    if not Books:
        print("No books available in the library.")
        return
    
    ID = input("Enter Book ID: ").strip()
    Book_Name = input("Enter Book Name: ").strip() 
    Author_Name = input("Enter Author Name: ").strip()
    found = False

    print("\nSearching for the book...\n")

    for Book_ID , details in Books.items():
        if ID == Book_ID or details['Book_Name'].lower() == Book_Name.lower() or details['Author_Name'].lower() == Author_Name.lower():
            found = True
            print("---------Book found:---------\n")
            print(f"Book ID: {Book_ID}")
            print(f"Book Name: {details['Book_Name']}")
            print(f"Author Name: {details['Author_Name']}")
            print(f"Category: {details['Category']}")
            print(f"Total Copies: {details['Total_Copies']}")
            print(f"Issued Copies: {details['Issued_Copies']}")
            print(f"Available Copies: {details['Total_Copies'] - details['Issued_Copies']}")
            print("-----------------------------\n")
    if not found:
        print("Book not found in the library.")