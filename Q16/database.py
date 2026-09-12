import sqlite3

def connect_database():
    conn = sqlite3.connect("students.db")
    return conn


def create_table():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        roll_no INTEGER,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        cgpa REAL,
        PRIMARY KEY (roll_no, department)
    )
    """)

    conn.commit()
    conn.close()