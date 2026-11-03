pip install pandas matplotlib numpy

import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Create multiple plots
plt.figure(figsize=(10, 8))

# Plot 1 - Line plot
plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title("Line Plot")

# Plot 2 - Bar plot
plt.subplot(2, 2, 2)
plt.bar(x, y)
plt.title("Bar Plot")

# Plot 3 - Scatter plot
plt.subplot(2, 2, 3)
plt.scatter(x, y)
plt.title("Scatter Plot")

# Plot 4 - Histogram
plt.subplot(2, 2, 4)
plt.hist(y)
plt.title("Histogram")

# Display all plots
plt.tight_layout()
plt.show()