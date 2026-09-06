#QUESTION NUMBER 3
#Develop a python program to manage student records using lists and 
#dictionaries, supporting, insertion, deletion and search operation.

students=[]

def insert_student():
    roll_no=input("Enter Roll Number: ")
    for student in students:
        if student["Roll No"]==roll_no:
            print("Student with this Roll Number already exists.\n")
            return
    name=input("Enter Name: ")
    age=input("Enter age: ")
    course=input("Enter Course: ")
    student={
            "Roll No":roll_no,
            "Name":name,
            "Age":age,
            "Course":course
            }
    students.append(student)
    print("Student record inserted successfully.\n")
def delete_student():
    roll_no=input("Enter Roll Number to delete: ")
    for student in students:
        if student["Roll No"]==roll_no:
            students.remove(student)
            print("Student record deleted successfully.\n")
            return
    print("Student record not found.\n")

def search_student():
    roll_no=input("Enter Roll Number to search: ")
    for student in students:
        if student["Roll No"]==roll_no:
            print("\nStudent Found: ")
            for key,value in student.items():
                print(f"{key}:{value}")
            print()
            return
    print("Student record not found.\n")
def display_students():
    if not students:
        print("No student records available.\n")
        return
    print("\n===All student Records===")
    for student in students:
        for key,value in student.items():
            print(f"{key}:{value}")

    print("----------------\n")
while True:
    print("===== Student Record Management====")
    print("1. Insert Student")
    print("2. Delete Student")
    print("3. Search Student")
    print("4. Display All Students")     
    print("5. Exit")
    choice=input("Enter your choice: ")
    if choice=="1":
        insert_student()
    elif choice=="2":
        delete_student()
    elif choice=="3":
        search_student()
    elif choice=="4":
        display_students()
    elif choice=="5":
        print("Existing program...")
        break
    else:
        print("Invalid choice! Please try again.\n")                                      
    