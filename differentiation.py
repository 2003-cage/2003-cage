import sympy as sp

# Define the variable and the function
x = sp.symbols('x')
f = x**2 - x - 2

# Differentiate the function
f_prime = sp.diff(f, x)
print(f"Derivative of {f} with respect to {x} is {f_prime}")
