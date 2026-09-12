from database import connect_database


def department_report(department):
    conn = connect_database()
    cursor = conn.cursor()

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

    conn.close()