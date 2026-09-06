#QUESTION NUMBER 16TH
# Develop a SQLite-based Student Information Management System 
# using Python to store, retrieve, and display student details
# such as roll number, name, department, and CGPA.

import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    cgpa REAL
)
""")

# Insert student details
n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student", i + 1)

    roll_no = int(input("Roll Number: "))
    name = input("Name: ")
    department = input("Department: ")
    cgpa = float(input("CGPA: "))

    cursor.execute("""
    INSERT INTO students (roll_no, name, department, cgpa)
    VALUES (?, ?, ?, ?)
    """, (roll_no, name, department, cgpa))

conn.commit()

# Retrieve and display student details
print("\n----- Student Information -----")

cursor.execute("SELECT * FROM students")
students = cursor.fetchall()

for student in students:
    print("Roll Number:", student[0])
    print("Name:", student[1])
    print("Department:", student[2])
    print("CGPA:", student[3])
    print("------------------------------")

# Close connection
conn.close()