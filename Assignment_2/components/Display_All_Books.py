from components.database import Books

def Display_All_Books():
    if not Books:
        print("No books available in the library.")
        return

    for Book_ID, Details in Books.items():
        print(f"Book ID: {Book_ID}")
        print(f"Book Name: {Details['Book_Name']}")
        print(f"Author Name: {Details['Author_Name']}")
        print(f"Category: {Details['Category']}")
        print(f"Total Copies: {Details['Total_Copies']}")
        print(f"Issued Copies: {Details['Issued_Copies']}")
        print(f"Available Copies: {Details['Total_Copies'] - Details['Issued_Copies']}")
        print("-----------------------------\n")