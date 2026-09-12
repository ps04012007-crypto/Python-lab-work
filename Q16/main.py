from database import create_table
from student import add_student, display_students


# Create student table
create_table()

# Enter number of students
n = int(input("Enter number of students: "))

# Add students
for i in range(n):
    print("\nEnter details of student", i + 1)

    roll_no = int(input("Roll Number: "))
    name = input("Name: ")
    department = input("Department: ")
    cgpa = float(input("CGPA: "))

    add_student(roll_no, name, department, cgpa)


# Display all students
display_students()