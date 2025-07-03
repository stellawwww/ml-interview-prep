import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Your data
data = np.array(
    [0.5, 0.7, 2.1, 2.2, 2.9, 3.2, 3.2, 3.3, 3.7, 4.5, 4.6, 4.8, 5.2, 5.3, 6.7, 8.1]
)
n = len(data)

# Silverman's rule of thumb for bandwidth
std_dev = np.std(data)
h = 1.06 * std_dev * n ** (-1 / 5)

# KDE estimate at x = 3.0
x = 3.0
kde_estimate = np.sum(norm.pdf((x - data) / h)) / (n * h)
print(f"KDE at x = {x}: {kde_estimate:.4f}")

# Plotting the full KDE curve manually
x_grid = np.linspace(min(data) - 1, max(data) + 1, 200)
kde_curve = np.array([np.sum(norm.pdf((x - data) / h)) / (n * h) for x in x_grid])

plt.hist(data, bins=10, density=True, alpha=0.5, label="Histogram")
plt.plot(x_grid, kde_curve, label="Density Curve (KDE)", linewidth=2)
plt.title("Manual KDE from Histogram")
plt.legend()
plt.show()


###density plot: area =1
import seaborn as sns
import matplotlib.pyplot as plt

data = [10, 12, 12, 14, 15, 15, 15, 16, 17, 18, 20, 22]

sns.histplot(data, kde=True, stat="density")  # kde=True adds the density curve
plt.title("Histogram with Density Curve")
plt.show()
