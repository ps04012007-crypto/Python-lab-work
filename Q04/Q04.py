# Q4: Student Course Enrolment Analysis

# Tuple to store student details
student1 = ("Rahul", 101, "CSE")
student2 = ("Priya", 102, "CSE")

# Sets to store courses
student1_courses = {"Python", "DSA", "DBMS", "Maths"}
student2_courses = {"Python", "DSA", "OS", "Computer Networks"}

print("Student 1 Details:", student1)
print("Student 1 Courses:", student1_courses)

print("\nStudent 2 Details:", student2)
print("Student 2 Courses:", student2_courses)

# Union - all unique courses
print("\nUnion of courses:")
print(student1_courses.union(student2_courses))

# Intersection - common courses
print("\nCommon courses:")
print(student1_courses.intersection(student2_courses))

# Difference - courses unique to each student
print("\nCourses only Student 1 is enrolled in:")
print(student1_courses.difference(student2_courses))

print("\nCourses only Student 2 is enrolled in:")
print(student2_courses.difference(student1_courses))
