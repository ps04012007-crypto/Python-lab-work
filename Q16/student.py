from database import connect_database


def add_student(roll_no, name, department, cgpa):
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO students (roll_no, name, department, cgpa)
    VALUES (?, ?, ?, ?)
    """, (roll_no, name, department, cgpa))

    conn.commit()
    conn.close()

    print("Student added successfully.")


def display_students():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    print("\n----- Student Information -----")

    if not students:
        print("No student records found.")
    else:
        for student in students:
            print("Roll Number:", student[0])
            print("Name:", student[1])
            print("Department:", student[2])
            print("CGPA:", student[3])
            print("------------------------------")

    conn.close()