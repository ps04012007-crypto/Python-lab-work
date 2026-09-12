import sqlite3


def connect_database():
    conn = sqlite3.connect("employees.db")
    return conn


def create_table():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        emp_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        designation TEXT NOT NULL,
        department TEXT NOT NULL,
        salary REAL
    )
    """)

    conn.commit()
    conn.close()