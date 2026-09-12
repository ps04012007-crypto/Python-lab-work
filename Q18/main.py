from database import create_table
from employee import add_employee
from report import department_report


# Create employee table
create_table()


# Enter number of employees
n = int(input("Enter number of employees: "))


# Add employee details
for i in range(n):
    print("\nEnter details of employee", i + 1)

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


# Generate department-wise salary report
department = input("\nEnter department for salary report: ")

department_report(department)