from database import connect_database


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