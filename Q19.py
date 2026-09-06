import tkinter as tk
import sqlite3
from tkinter import messagebox

# Connect to SQLite database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    status TEXT
)
""")

conn.commit()


# Add Book
def add_book():
    book_id = entry_id.get()
    title = entry_title.get()
    author = entry_author.get()

    if book_id == "" or title == "" or author == "":
        messagebox.showinfo("Error", "Please enter all details")
    else:
        cursor.execute(
            "INSERT INTO books VALUES (?, ?, ?, ?)",
            (book_id, title, author, "Available")
        )
        conn.commit()

        messagebox.showinfo("Success", "Book added successfully")

        entry_id.delete(0, tk.END)
        entry_title.delete(0, tk.END)
        entry_author.delete(0, tk.END)


# Issue Book
def issue_book():
    book_id = entry_id.get()

    cursor.execute(
        "SELECT status FROM books WHERE id = ?", (book_id,)
    )

    result = cursor.fetchone()

    if result is None:
        messagebox.showinfo("Error", "Book not found")

    elif result[0] == "Issued":
        messagebox.showinfo("Message", "Book is already issued")

    else:
        cursor.execute(
            "UPDATE books SET status = 'Issued' WHERE id = ?",
            (book_id,)
        )

        conn.commit()

        messagebox.showinfo("Success", "Book issued successfully")


# Return Book
def return_book():
    book_id = entry_id.get()

    cursor.execute(
        "SELECT status FROM books WHERE id = ?", (book_id,)
    )

    result = cursor.fetchone()

    if result is None:
        messagebox.showinfo("Error", "Book not found")

    elif result[0] == "Available":
        messagebox.showinfo("Message", "Book is already available")

    else:
        cursor.execute(
            "UPDATE books SET status = 'Available' WHERE id = ?",
            (book_id,)
        )

        conn.commit()

        messagebox.showinfo("Success", "Book returned successfully")


# Search Book
def search_book():
    book_id = entry_id.get()

    cursor.execute(
        "SELECT * FROM books WHERE id = ?", (book_id,)
    )

    result = cursor.fetchone()

    if result is None:
        messagebox.showinfo("Error", "Book not found")
    else:
        messagebox.showinfo(
            "Book Details",
            "ID: " + str(result[0]) +
            "\nTitle: " + result[1] +
            "\nAuthor: " + result[2] +
            "\nStatus: " + result[3]
        )


# Create window
window = tk.Tk()
window.title("Library Management System")
window.geometry("400x400")


# Heading
tk.Label(
    window,
    text="Library Management System",
    font=("Arial", 16)
).pack(pady=10)


# Book ID
tk.Label(window, text="Book ID").pack()
entry_id = tk.Entry(window)
entry_id.pack()


# Book Title
tk.Label(window, text="Book Title").pack()
entry_title = tk.Entry(window)
entry_title.pack()


# Author
tk.Label(window, text="Author").pack()
entry_author = tk.Entry(window)
entry_author.pack()


# Buttons
tk.Button(window, text="Add Book",
          command=add_book).pack(pady=5)

tk.Button(window, text="Issue Book",
          command=issue_book).pack(pady=5)

tk.Button(window, text="Return Book",
          command=return_book).pack(pady=5)

tk.Button(window, text="Search Book",
          command=search_book).pack(pady=5)


window.mainloop()

conn.close()