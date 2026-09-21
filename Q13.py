import numpy as np
from scipy.integrate import quad
from scipy.misc import derivative

def f(x):
    return x**2

# Numerical differentiation at x = 2
d = derivative(f, 2, dx=0.0001)

print("Derivative at x = 2:", d)

# Numerical integration from 0 to 2
result, error = quad(f, 0, 2)

print("Integration from 0 to 2:", result)

