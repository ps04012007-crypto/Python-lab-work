#QUESTION NUMBER 8TH
#Develop a python program using Numpy array to compute the total marks 
#average marks,and percentage improvement of students across multiple
#subject using vectorized arthimatic operations.

import numpy as np

# Mid-Semester Examination Marks
mid_sem = np.array([
    [65, 70, 68, 72],
    [78, 75, 80, 77],
    [55, 60, 58, 62],
    [82, 85, 80, 88],
    [70, 68, 72, 74]
])

# End-Semester Examination Marks
end_sem = np.array([
    [72, 78, 75, 80],
    [84, 82, 86, 83],
    [65, 68, 66, 70],
    [88, 90, 85, 92],
    [78, 75, 80, 82]
])

students = ["S1", "S2", "S3", "S4", "S5"]

# Total marks in Mid-Semester
mid_total = np.sum(mid_sem, axis=1)

# Total marks in End-Semester
end_total = np.sum(end_sem, axis=1)

# Average marks in End-Semester
average = np.mean(end_sem, axis=1)

# Percentage improvement from Mid-Semester to End-Semester
percentage_improvement = ((end_total - mid_total) / mid_total) * 100

# Display results
print("Student\tMid Total\tEnd Total\tAverage\tImprovement (%)")
print("-" * 65)

for i in range(len(students)):
    print(f"{students[i]}\t{mid_total[i]}\t\t{end_total[i]}\t\t"
          f"{average[i]:.2f}\t{percentage_improvement[i]:.2f}%")
