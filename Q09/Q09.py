#QUESTION NUMBER 9TH
#Develop a python program to compute statical measures(mean,median,
#standard deviation, minimum and maximum) using numpy and without using 
#numpy. marks=[78,85,92,67,88,73,95,81,76,89]
#temperatures=[28.5,30.2,29.8,31.4,27.9,32.1,27.9,32.1,30.5]
#sales=[12500,13800,14200,11900,15100,14750,16000]

import numpy as np

marks = [78, 85, 92, 67, 88, 73, 95, 81, 76, 89]
temperatures = [28.5, 30.2, 29.8, 31.4, 27.9, 32.1, 30.5]
sales = [12500, 13800, 14200, 11900, 15100, 14750, 16000]


# Without NumPy
def without_numpy(data):
    n = len(data)

    mean = sum(data) / n

    sorted_data = sorted(data)

    if n % 2 == 0:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        median = sorted_data[n // 2]

    variance = sum((x - mean) ** 2 for x in data) / n
    standard_deviation = variance ** 0.5

    minimum = min(data)
    maximum = max(data)

    return mean, median, standard_deviation, minimum, maximum


# Using NumPy
def with_numpy(data):
    arr = np.array(data)

    mean = np.mean(arr)
    median = np.median(arr)
    standard_deviation = np.std(arr)
    minimum = np.min(arr)
    maximum = np.max(arr)

    return mean, median, standard_deviation, minimum, maximum


# Ask user for choice
print("1. Calculate using NumPy")
print("2. Calculate without NumPy")

choice = int(input("Enter your choice: "))


datasets = {
    "Marks": marks,
    "Temperatures": temperatures,
    "Sales": sales
}


if choice == 1:

    print("\n--- Using NumPy ---")

    for name, data in datasets.items():

        mean, median, sd, minimum, maximum = with_numpy(data)

        print("\n", name)
        print("Mean =", mean)
        print("Median =", median)
        print("Standard Deviation =", sd)
        print("Minimum =", minimum)
        print("Maximum =", maximum)


elif choice == 2:

    print("\n--- Without NumPy ---")

    for name, data in datasets.items():

        mean, median, sd, minimum, maximum = without_numpy(data)

        print("\n", name)
        print("Mean =", mean)
        print("Median =", median)
        print("Standard Deviation =", sd)
        print("Minimum =", minimum)
        print("Maximum =", maximum)


else:
    print("Invalid choice!")
