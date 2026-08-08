import mysql.connector as mysql
import random

# Establishing connection to MySQL
con = mysql.connect(host="localhost", user="root", password="123456")
cursor = con.cursor()

print('''
**************************************************************************************
                            LIBRARY MANAGEMENT SYSTEM                               
**************************************************************************************
''')

# Check existing databases and create 'LibraryPlus' if it does not exist
cursor.execute("create database if not exists LibraryPlus")
cursor.execute("USE LibraryPlus")

# Creating necessary tables if they don't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS books(
               id INT PRIMARY KEY,
               title VARCHAR(50),
               author VARCHAR(50),
               quantity INT,
               INDEX(title) )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS issued_books(
               id INT,
               title VARCHAR(50),
               student_name VARCHAR(50),
               issue_date DATE )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS returned_books(
               id INT,
               title VARCHAR(50),
               student_name VARCHAR(50),
               issue_date DATE,
               return_date DATE )''')

con.commit()


def generate_unique_id(): # Function to generate a unique 3-digit ID for a new book
    cursor.execute("SELECT id FROM books")
    existing_ids = cursor.fetchall()

    # Create a set to store existing IDs for efficient lookup
    existing_id_set = set()
    for id in existing_ids:
        existing_id_set.add(id[0])

    # Generate a random 3-digit ID within the range (100, 999)
    while True:
        new_id = random.randint(100, 999)
        # Check if the generated ID is not in the set of existing IDs
        if new_id not in existing_id_set:
            # If it's unique, return the new ID
            return new_id


def add_book():
    title = input("Enter Book Title: ")
    author = input("Enter Author's Name: ")
    quantity = int(input("Enter Quantity: "))

    # Generating a unique ID for the new book using the generate_unique_id function
    book_id = generate_unique_id()

    cursor.execute("INSERT INTO books VALUES (%s, %s, %s, %s)", (book_id, title, author, quantity))
    con.commit()
    print("Book Added Successfully!")


def display_books():
    try:
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        if not books:
            print("No books available")
        else:
            print("List of Books: ")
            for book in books:
                print("ID: ", book[0], 
                      "Title: ", book[1], 
                      "Author: ", book[2], 
                      "Quantity: ", book[3]
                      )
    except Exception as e:
        print("An error occurred while fetching books:", e)


def search_book():
    search_title = input("Enter the book title to search:  ")
    cursor.execute("SELECT * FROM books WHERE title LIKE %s", ('%' + search_title + '%',))
    found_books = cursor.fetchall()
    if not found_books: 
        print("No matching books found.")
    else: 
        print("Matching Books:  ")
        for book in found_books: 
            print("ID: ", book[0], "Title: ", book[1], "Author: ", book[2], "Quantity: ", book[3])


def issue_book(): 
    title = input("Enter Book Title: ")
    try:
        # Check if the book is available and in stock
        cursor.execute("SELECT id, quantity FROM books WHERE title = %s", (title,))
        book_data = cursor.fetchone()

        if not book_data or book_data[1] == 0:
            print("Book not available or out of stock. Choose any other book")
            return
        
        student_name = input("Enter Student's Name: ")
        issue_date = input("Enter Issue Date (YYYY-MM-DD): ")

        # Check if the book has already been issued to the same student
        cursor.execute("SELECT title, student_name FROM issued_books WHERE title = %s AND student_name = %s", (title, student_name))
        existing_issue = cursor.fetchone()
        
        # If the book has already been issued to the same student, display an error message
        if existing_issue:
            print("The requested book has already been issued to the same student.")
            return

        # Proceed with issuing the book
        book_id = book_data[0]
        cursor.execute("UPDATE books SET quantity = quantity - 1 WHERE id = %s", (book_id,))
        cursor.execute("INSERT INTO issued_books VALUES (%s, %s, %s, %s)", (book_id, title, student_name, issue_date))
        con.commit()
        print("Book issued successfully")

    except Exception as e:
        print("Error occurred:", e)
        con.rollback()       # Rollback the transaction to revert any changes made before the error occurred


def Display_issued_books(): 
    # Display issued books
    cursor.execute("SELECT id, title, student_name, issue_date FROM issued_books")
    issued = cursor.fetchall()
    if issued: 
        print("List of Currently Issued Books: ")
        for book in issued: 
            print("ID: ", book[0], "Title: ", book[1], "Student: ", book[2], "Issue Date: ", book[3])
    else:
        print("No books currently issued")


def return_book(): 
    sname = input("Enter Student's Name:  ")
    title = input("Enter Book Title:  ")
    return_date = input("Enter Return Date (YYYY-MM-DD):  ")
    
    # Retrieve the book's ID and issue date from the issued_books table based on student name and book title
    cursor.execute("SELECT id, issue_date FROM issued_books WHERE student_name = %s AND title = %s", (sname, title))
    book = cursor.fetchone()

    if book: 
        book_id = book[0]
        issue_date = book[1]
        # Move the book to the returned_books table with the issue date
        cursor.execute("INSERT INTO returned_books VALUES(%s, %s, %s, %s, %s)", (book_id, title, sname, issue_date, return_date))
        
        # Increase the quantity of the book in the books table
        cursor.execute("UPDATE books SET quantity = quantity + 1 WHERE title = %s", (title,))
        
        # Remove the book from the issued_books table
        cursor.execute("DELETE FROM issued_books WHERE id = %s AND title = %s AND student_name = %s", (book_id, title, sname))
        con.commit()
        print("Book Returned Successfully")

    else: 
        print("No such book issued")


def Display_returned_books(): 
    # Display returned books
    cursor.execute("SELECT id, title, student_name, issue_date, return_date FROM returned_books")
    returned = cursor.fetchall()
    if returned:
        print("List of All Returned Books: ")
        for book in returned: 
            print("ID: ", book[0], "Title: ", book[1], "Student: ", book[2], "Issue Date: ", book[3], "Return Date: ", book[4])
    else:
        print("No books have been returned yet.")


def delete_book(): 
    try:
        book_id = int(input("Enter Book ID to delete:  "))
        # Check if the book is currently issued but not returned
        cursor.execute("SELECT id FROM issued_books WHERE id = %s", (book_id,))
        issued_book = cursor.fetchone()

        if issued_book:
            print("Cannot delete the book because it is currently issued to a student.")
        else:
            # Delete the book from the books table
            cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
            con.commit()
            print("Book Deleted Successfully")
    except Exception as e:
        print("An error occurred while deleting the book:", e)


def add_default_books():  # This function is created to add some default books for testing purposes!
    try:
        books = [
            ("Computer Science", "Sumita Arora", 50),
            ("Maths class 12", "RS Aggarwal", 15),
            ("English Grammar", "David Miller", 25),
            ("Concepts of Physics", "H.C Verma", 20)
        ]

        # Iterate through each default book
        for book in books:
            # Extracting title, author, and quantity from the current book tuple
            title = book[0]
            author = book[1]
            quantity = book[2]
            # Check if the book already exists in the database
            cursor.execute("SELECT id FROM books WHERE title = %s AND author = %s", (title, author))
            existing_book = cursor.fetchone()
            
            # If the book does not exist in the database then insert it
            if not existing_book:
                book_id = generate_unique_id() # Generate a unique ID for the new book
                cursor.execute("INSERT INTO books VALUES (%s, %s, %s, %s)", (book_id, title, author, quantity))

        con.commit()
        
    except Exception as e:
        print(e)



def main():
    add_default_books()
    while True: 
        print('''
LIBRARY MANAGEMENT SYSTEM
1. ADD BOOK
2. DISPLAY BOOKS
3. SEARCH BOOK
4. ISSUE OF BOOK
5. DISPLAY ISSUED BOOKS
6. RETURN BOOK
7. DISPLAY RETURNED BOOKS    
8. DELETE BOOK
9. EXIT PROGRAM
              ''')
    
        choice = input("Enter your choice:  ")
        if choice == '1':
            add_book()
        elif choice == '2': 
            display_books() 
        elif choice == '3': 
            search_book()
        elif choice == '4': 
            issue_book()
        elif choice == '5': 
            Display_issued_books()
        elif choice == '6':
            return_book()
        elif choice == '7':
            Display_returned_books()
        elif choice == '8':
            delete_book()
        elif choice == '9': 
            print("Exiting...")
            break
        else: 
            print("Invalid choice. Please try again.")

if __name__ == "__main__": 
    main()

if con.is_connected():
    cursor.close()
    con.close()