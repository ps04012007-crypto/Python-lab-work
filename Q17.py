#QUESTION NUMBER 17TH
# Develop a Python application to perform Create, Read, Update,
# and Delete (CRUD) operations on employee records containing 
# employee ID, name, designation, department, and salary in an SQLite
# database.

import sqlite3

# Connect to database
conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    designation TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL
)
""")

# CREATE
def create_employee():
    emp_id = int(input("Employee ID: "))
    name = input("Name: ")
    designation = input("Designation: ")
    department = input("Department: ")
    salary = float(input("Salary: "))

    cursor.execute("""
    INSERT INTO employees
    (emp_id, name, designation, department, salary)
    VALUES (?, ?, ?, ?, ?)
    """, (emp_id, name, designation, department, salary))

    conn.commit()
    print("Employee added successfully.")


# READ
def read_employees():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    print("\n----- Employee Records -----")

    if not employees:
        print("No employee records found.")
    else:
        for emp in employees:
            print("Employee ID:", emp[0])
            print("Name:", emp[1])
            print("Designation:", emp[2])
            print("Department:", emp[3])
            print("Salary:", emp[4])
            print("----------------------------")


# UPDATE
def update_employee():
    emp_id = int(input("Enter Employee ID to update: "))

    name = input("New Name: ")
    designation = input("New Designation: ")
    department = input("New Department: ")
    salary = float(input("New Salary: "))

    cursor.execute("""
    UPDATE employees
    SET name = ?, designation = ?, department = ?, salary = ?
    WHERE emp_id = ?
    """, (name, designation, department, salary, emp_id))

    conn.commit()

    if cursor.rowcount > 0:
        print("Employee updated successfully.")
    else:
        print("Employee not found.")


# DELETE
def delete_employee():
    emp_id = int(input("Enter Employee ID to delete: "))

    cursor.execute(
        "DELETE FROM employees WHERE emp_id = ?",
        (emp_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Employee deleted successfully.")
    else:
        print("Employee not found.")


# Menu
while True:
    print("\n===== Employee Management System =====")
    print("1. Create Employee")
    print("2. Read Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_employee()

    elif choice == 2:
        read_employees()

    elif choice == 3:
        update_employee()

    elif choice == 4:
        delete_employee()

    elif choice == 5:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")

# Close database
conn.close()