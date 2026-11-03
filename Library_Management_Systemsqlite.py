
import sqlite3

# 1. Establish database connection
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

print("Database connected successfully!")


# 2. Create Books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    Book_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title VARCHAR(100) NOT NULL,
    Author VARCHAR(100) NOT NULL,
    Category VARCHAR(50) NOT NULL,
    Copies INTEGER NOT NULL
)
""")

conn.commit()
print("Books table created successfully!")


# 3. Insert a single book
def insert_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    category = input("Enter category: ")
    copies = int(input("Enter number of copies: "))

    cursor.execute("""
    INSERT INTO Books (Title, Author, Category, Copies)
    VALUES (?, ?, ?, ?)
    """, (title, author, category, copies))

    conn.commit()
    print("Book inserted successfully!")


# 4. Insert multiple books using executemany()
def insert_multiple_books():
    n = int(input("How many books do you want to insert? "))

    books = []

    for i in range(n):
        print("\nEnter details of book", i + 1)

        title = input("Enter title: ")
        author = input("Enter author: ")
        category = input("Enter category: ")
        copies = int(input("Enter copies: "))

        books.append((title, author, category, copies))

    cursor.executemany("""
    INSERT INTO Books (Title, Author, Category, Copies)
    VALUES (?, ?, ?, ?)
    """, books)

    conn.commit()
    print("Multiple books inserted successfully!")


# 5. Display all books
def display_books():
    cursor.execute("SELECT * FROM Books")
    records = cursor.fetchall()

    if records:
        print("\n===== ALL BOOK DETAILS =====")

        for row in records:
            print(row)
    else:
        print("No books available!")


# 6. Search book using Book_ID
def search_book():
    book_id = int(input("Enter Book ID: "))

    cursor.execute(
        "SELECT * FROM Books WHERE Book_ID = ?",
        (book_id,)
    )

    record = cursor.fetchone()

    if record:
        print("Book found:", record)
    else:
        print("Book not found!")


# 7. Update number of copies
def update_book():
    book_id = int(input("Enter Book ID: "))
    copies = int(input("Enter new number of copies: "))

    cursor.execute("""
    UPDATE Books
    SET Copies = ?
    WHERE Book_ID = ?
    """, (copies, book_id))

    conn.commit()

    if cursor.rowcount > 0:
        print("Book copies updated successfully!")
    else:
        print("Book not found!")


# 8. Delete a book using Book_ID
def delete_book():
    book_id = int(input("Enter Book ID to delete: "))

    cursor.execute(
        "DELETE FROM Books WHERE Book_ID = ?",
        (book_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Book deleted successfully!")
    else:
        print("Book not found!")


# 9. Display books by category
def search_category():
    category = input("Enter category: ")

    cursor.execute(
        "SELECT * FROM Books WHERE Category = ?",
        (category,)
    )

    records = cursor.fetchall()

    if records:
        print("\nBooks in", category, "category:")

        for row in records:
            print(row)
    else:
        print("No books found in this category!")


# 10. Menu-driven application
while True:

    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Insert a Book")
    print("2. Insert Multiple Books")
    print("3. Display All Books")
    print("4. Search Book by ID")
    print("5. Update Book Copies")
    print("6. Delete Book")
    print("7. Search Books by Category")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        insert_book()

    elif choice == '2':
        insert_multiple_books()

    elif choice == '3':
        display_books()

    elif choice == '4':
        search_book()

    elif choice == '5':
        update_book()

    elif choice == '6':
        delete_book()

    elif choice == '7':
        search_category()

    elif choice == '8':
        print("Exiting Library Management System...")
        break

    else:
        print("Invalid choice! Please try again.")


# Close database connection
conn.close()

print("Database connection closed.")
