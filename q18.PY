#QUESTION NUMBER 18TH
# Develop a Python application to generate department-wise employee
# salary reports by executing parameterized SQL queries on an SQLite 
# database.

import sqlite3

# Connect to database
conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

# Create table if it does not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    designation TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL
)
""")

# Insert sample data only if table is empty
cursor.execute("SELECT COUNT(*) FROM employees")
count = cursor.fetchone()[0]

if count == 0:
    employees = [
        (101, "Rahul", "Manager", "CSE", 60000),
        (102, "Priya", "Developer", "CSE", 50000),
        (103, "Amit", "Engineer", "ECE", 45000),
        (104, "Neha", "Developer", "ECE", 48000),
        (105, "Rohan", "Manager", "Civil", 55000)
    ]

    cursor.executemany("""
    INSERT INTO employees
    (emp_id, name, designation, department, salary)
    VALUES (?, ?, ?, ?, ?)
    """, employees)

    conn.commit()


# Generate department-wise salary report
department = input("Enter department: ")

cursor.execute("""
SELECT emp_id, name, designation, salary
FROM employees
WHERE department = ?
""", (department,))

employees = cursor.fetchall()

print("\n===== Department-wise Salary Report =====")
print("Department:", department)

if not employees:
    print("No employees found in this department.")
else:
    total_salary = 0

    for emp in employees:
        print("\nEmployee ID:", emp[0])
        print("Name:", emp[1])
        print("Designation:", emp[2])
        print("Salary:", emp[3])

        total_salary += emp[3]

    print("\nTotal Salary:", total_salary)
    print("Number of Employees:", len(employees))
    print("Average Salary:", total_salary / len(employees))

# Close connection
conn.close()
