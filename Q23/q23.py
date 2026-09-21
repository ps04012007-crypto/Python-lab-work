import xml.etree.ElementTree as ET

# Read XML file
tree = ET.parse("students.xml")
root = tree.getroot()

print("===== Student Information Management =====")
print("1. Modify Student")
print("2. Add Student")

choice = input("Enter your choice: ")

# ---------------- MODIFY STUDENT ----------------

if choice == "1":

    student_id = input("Enter Student ID: ")

    student = None

    for s in root.findall("student"):
        if s.get("id") == student_id:
            student = s
            break

    if student is None:
        print("Student not found.")

    else:
        print("\n1. Name")
        print("2. Department")
        print("3. Year")
        print("4. Email")
        print("5. CGPA")

        option = input("What do you want to modify? ")

        if option == "1":
            value = input("Enter new name: ")
            student.find("name").text = value

        elif option == "2":
            value = input("Enter new department: ")
            student.find("department").text = value

        elif option == "3":
            value = input("Enter new year: ")
            student.find("year").text = value

        elif option == "4":
            value = input("Enter new email: ")
            student.find("email").text = value

        elif option == "5":
            value = input("Enter new CGPA: ")
            student.find("cgpa").text = value

        else:
            print("Invalid choice.")
            exit()

        print("Student information modified successfully.")


# ---------------- ADD STUDENT ----------------

elif choice == "2":

    student_id = input("Enter Student ID: ")

    # Check duplicate ID
    exists = False

    for s in root.findall("student"):
        if s.get("id") == student_id:
            exists = True
            break

    if exists:
        print("Student ID already exists.")

    else:
        name = input("Enter name: ")
        department = input("Enter department: ")
        year = input("Enter year: ")
        email = input("Enter email: ")
        cgpa = input("Enter CGPA: ")

        student = ET.SubElement(root, "student")
        student.set("id", student_id)

        ET.SubElement(student, "name").text = name
        ET.SubElement(student, "department").text = department
        ET.SubElement(student, "year").text = year
        ET.SubElement(student, "email").text = email
        ET.SubElement(student, "cgpa").text = cgpa

        print("New student added successfully.")

else:
    print("Invalid choice.")

# Save XML file
tree.write("modified_students.xml",
           encoding="utf-8",
           xml_declaration=True)

print("XML file saved successfully.")