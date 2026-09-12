from database import create_table
from employee import add_employee, display_employees
from employee import update_employee, delete_employee


# Create employee table
create_table()


while True:

    print("\n===== Employee Management System =====")
    print("1. Create Employee")
    print("2. Read Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # CREATE
    if choice == 1:

        emp_id = int(input("Employee ID: "))
        name = input("Name: ")
        designation = input("Designation: ")
        department = input("Department: ")
        salary = float(input("Salary: "))

        add_employee(
            emp_id,
            name,
            designation,
            department,
            salary
        )

    # READ
    elif choice == 2:

        display_employees()

    # UPDATE
    elif choice == 3:

        emp_id = int(input("Enter Employee ID to update: "))
        name = input("New Name: ")
        designation = input("New Designation: ")
        department = input("New Department: ")
        salary = float(input("New Salary: "))

        update_employee(
            emp_id,
            name,
            designation,
            department,
            salary
        )

    # DELETE
    elif choice == 4:

        emp_id = int(input("Enter Employee ID to delete: "))

        delete_employee(emp_id)

    # EXIT
    elif choice == 5:

        print("Program ended.")
        break

    else:

        print("Invalid choice.")