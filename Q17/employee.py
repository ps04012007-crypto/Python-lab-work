from database import connect_database


# CREATE
def add_employee(emp_id, name, designation, department, salary):
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO employees
    (emp_id, name, designation, department, salary)
    VALUES (?, ?, ?, ?, ?)
    """, (emp_id, name, designation, department, salary))

    conn.commit()
    conn.close()

    print("Employee added successfully.")


# READ
def display_employees():
    conn = connect_database()
    cursor = conn.cursor()

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

    conn.close()


# UPDATE
def update_employee(emp_id, name, designation, department, salary):
    conn = connect_database()
    cursor = conn.cursor()

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

    conn.close()


# DELETE
def delete_employee(emp_id):
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE emp_id = ?",
        (emp_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Employee deleted successfully.")
    else:
        print("Employee not found.")

    conn.close()