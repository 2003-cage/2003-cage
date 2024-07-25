import numpy as np


# Define the function to integrate
def f(x):
    return np.sin(x)  # Example function: sin(x)


# Implement the trapezoidal rule
def trapezoidal_rule(func, a, b, n):
    h = (b - a) / n  # Calculate the width of each trapezoid
    integral = 0.5 * (func(a) + func(b))  # Add the first and last terms

    for i in range(1, n):
        x = a + i * h
        integral += func(x)

    integral *= h  # Multiply by the width of the trapezoids
    return integral


# Set the integration limits and number of trapezoids
a = 0  # Lower limit
b = np.pi  # Upper limit
n = 100  # Number of subintervals (trapezoids)

# Calculate the integral
result = trapezoidal_rule(f, a, b, n)

print(f'The integral of sin(x) from {a} to {b} is approximately {result}')
