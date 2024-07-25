import scipy.interpolate as spi
import matplotlib.pyplot as plt
import numpy as np
# Generate some data points (x, y)
x_data = np.linspace(1, 3, 10)
y_data = x_data**2 - x_data - 2 + np.random.normal(0, 1, x_data.shape)

# Perform spline interpolation
spl = spi.splrep(x_data, y_data)
x_smooth = np.linspace(1, 3, 100)
y_smooth = spi.splev(x_smooth, spl)

# Plot the results
plt.scatter(x_data, y_data, label='Data Points')
plt.plot(x_smooth, y_smooth, label='Spline Interpolation')
plt.legend()
plt.show()
