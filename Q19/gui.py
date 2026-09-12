import tkinter as tk
from tkinter import messagebox

import database


def add_book():
    book_id = entry_id.get()
    title = entry_title.get()
    author = entry_author.get()

    if book_id == "" or title == "" or author == "":
        messagebox.showinfo("Error", "Please enter all details")
        return

    try:
        database.add_book(book_id, title, author)
        messagebox.showinfo("Success", "Book added successfully")

        entry_id.delete(0, tk.END)
        entry_title.delete(0, tk.END)
        entry_author.delete(0, tk.END)

    except sqlite3.IntegrityError:
        messagebox.showinfo("Error", "Book ID already exists")


def issue_book():
    book_id = entry_id.get()

    if book_id == "":
        messagebox.showinfo("Error", "Please enter Book ID")
        return

    result = database.issue_book(book_id)
    messagebox.showinfo("Result", result)


def return_book():
    book_id = entry_id.get()

    if book_id == "":
        messagebox.showinfo("Error", "Please enter Book ID")
        return

    result = database.return_book(book_id)
    messagebox.showinfo("Result", result)


def search_book():
    book_id = entry_id.get()

    if book_id == "":
        messagebox.showinfo("Error", "Please enter Book ID")
        return

    result = database.search_book(book_id)

    if result is None:
        messagebox.showinfo("Error", "Book not found")
    else:
        messagebox.showinfo(
            "Book Details",
            "Book ID: " + str(result[0]) +
            "\nTitle: " + result[1] +
            "\nAuthor: " + result[2] +
            "\nStatus: " + result[3]
        )


def create_gui():
    global entry_id
    global entry_title
    global entry_author

    window = tk.Tk()
    window.title("Library Management System")
    window.geometry("400x400")

    tk.Label(
        window,
        text="Library Management System",
        font=("Arial", 16)
    ).pack(pady=10)

    tk.Label(window, text="Book ID").pack()
    entry_id = tk.Entry(window)
    entry_id.pack()

    tk.Label(window, text="Book Title").pack()
    entry_title = tk.Entry(window)
    entry_title.pack()

    tk.Label(window, text="Author").pack()
    entry_author = tk.Entry(window)
    entry_author.pack()

    tk.Button(
        window,
        text="Add Book",
        command=add_book
    ).pack(pady=5)

    tk.Button(
        window,
        text="Issue Book",
        command=issue_book
    ).pack(pady=5)

    tk.Button(
        window,
        text="Return Book",
        command=return_book
    ).pack(pady=5)

    tk.Button(
        window,
        text="Search Book",
        command=search_book
    ).pack(pady=5)

    window.mainloop()