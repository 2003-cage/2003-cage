import scipy.optimize as opt
import numpy as np
# Define the function we want to fit to
def model(x, a, b, c):
    return a * x**2 + b * x + c

# Generate some data points (x, y) to fit to
x_data = np.linspace(1, 3, 10)
y_data = model(x_data, 1, -1, -2) + np.random.normal(0, 1, x_data.shape)

# Fit the model to the data
params, covariance = opt.curve_fit(model, x_data, y_data)
print(f"Fitted parameters: {params}")
