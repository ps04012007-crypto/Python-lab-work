import sqlite3

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    status TEXT
)
""")

conn.commit()


def add_book(book_id, title, author):
    cursor.execute(
        "INSERT INTO books VALUES (?, ?, ?, ?)",
        (book_id, title, author, "Available")
    )
    conn.commit()


def issue_book(book_id):
    cursor.execute(
        "SELECT status FROM books WHERE id = ?",
        (book_id,)
    )

    result = cursor.fetchone()

    if result is None:
        return "Book not found"

    if result[0] == "Issued":
        return "Book is already issued"

    cursor.execute(
        "UPDATE books SET status = 'Issued' WHERE id = ?",
        (book_id,)
    )
    conn.commit()

    return "Book issued successfully"


def return_book(book_id):
    cursor.execute(
        "SELECT status FROM books WHERE id = ?",
        (book_id,)
    )

    result = cursor.fetchone()

    if result is None:
        return "Book not found"

    if result[0] == "Available":
        return "Book is already available"

    cursor.execute(
        "UPDATE books SET status = 'Available' WHERE id = ?",
        (book_id,)
    )
    conn.commit()

    return "Book returned successfully"


def search_book(book_id):
    cursor.execute(
        "SELECT * FROM books WHERE id = ?",
        (book_id,)
    )

    return cursor.fetchone()