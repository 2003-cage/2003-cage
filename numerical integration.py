import scipy.integrate as spi
import numpy as np

# Define the function
def f(x):
    return x**2 - x - 2

# Perform numerical integration over the interval [1, 3]
result, error = spi.quad(f, 1, 3)
print(f"Numerical integration of x^2 - x - 2 over [1, 3] is {result} with error {error}")
