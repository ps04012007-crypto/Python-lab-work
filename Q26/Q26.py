import matplotlib.pyplot as plt

# Data
students = ["S1", "S2", "S3", "S4", "S5",
            "S6", "S7", "S8", "S9", "S10"]

study_hours = [8, 10, 12, 15, 18, 20, 7, 14, 16, 22]

exam_scores = [65, 72, 75, 82, 88, 90, 60, 80, 85, 95]


# -------- HISTOGRAM OF STUDY HOURS --------

plt.figure()

plt.hist(study_hours, bins=5,edgecolor="white")

plt.xlabel("Study Hours per Week")
plt.ylabel("Number of Students")
plt.title("Distribution of Study Hours")

plt.show()


# -------- HISTOGRAM OF EXAM SCORES --------

plt.figure()

plt.hist(exam_scores, bins=5,edgecolor="white")

plt.xlabel("Exam Score")
plt.ylabel("Number of Students")
plt.title("Distribution of Exam Scores")

plt.show()


# -------- SCATTER PLOT --------

plt.figure()

plt.scatter(study_hours, exam_scores)

plt.xlabel("Study Hours per Week")
plt.ylabel("Exam Score")
plt.title("Study Hours vs Exam Scores")

plt.grid()
plt.show()
