import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Given data
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([6, 17, 34, 57, 86, 121])

# Second-degree polynomial
def polynomial(x, a, b, c):
    return a*x**2 + b*x + c

# Fit the polynomial
coefficients, covariance = curve_fit(polynomial, x, y)

a, b, c = coefficients

print("Polynomial coefficients:")
print("a =", a)
print("b =", b)
print("c =", c)

# Calculate fitted values
y_fit = polynomial(x, a, b, c)

# Plot
plt.scatter(x, y, label="Original Data")
plt.plot(x, y_fit, label="Fitted Curve")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Second Degree Polynomial Fit")
plt.legend()
plt.show()


