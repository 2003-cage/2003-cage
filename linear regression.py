import numpy as np
from sklearn.linear_model import LinearRegression
import numpy as np
# Generate some data points (x, y)
x_data = np.linspace(1, 3, 10)
y_data = x_data**2 - x_data - 2 + np.random.normal(0, 1, x_data.shape)

# Reshape x_data for sklearn
x_data = x_data.reshape(-1, 1)

# Perform linear regression
model = LinearRegression()
model.fit(x_data, y_data)

# Print the coefficients
print(f"Slope: {model.coef_[0]}, Intercept: {model.intercept_}")
