
x1, y1 = 2.00, 7.2
x2, y2 = 4.25, 7.1

# The x value at which we want to find the interpolated y value
x = 4.0

# Calculate the interpolated y value using the linear interpolation formula
y = y1 + (y2 - y1) / (x2 - x1) * (x - x1)

print(f"The value of y at x = {x} is {y:.6f}")
