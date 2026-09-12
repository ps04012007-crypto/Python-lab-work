#QUESTION NUMBER 15TH
#Develop a Python program using Scipy optimisation techniques 
#to determine the minimum value of the function. 
# f(x,y)=(x-2)^2 + (y-2)^2

from scipy.optimize import minimize

# Define the function
def f(variables):
    x, y = variables
    return (x - 2)**2 + (y - 2)**2

# Initial guess
initial_guess = [0, 0]

# Minimize the function
result = minimize(f, initial_guess)

# Get minimum point
x_min, y_min = result.x

print("Minimum point:")
print("x =", x_min)
print("y =", y_min)

print("Minimum value =",round( result.fun,2))
