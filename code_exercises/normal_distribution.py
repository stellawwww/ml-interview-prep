import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Set up parameters for a normal distribution
mu = 0
sigma = 1
x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
y = norm.pdf(x, mu, sigma)

# Create the plot
plt.plot(x, y, label="Normal Distribution")

# Shade 1σ
plt.fill_between(
    x, y, where=(x >= mu - sigma) & (x <= mu + sigma), alpha=0.3, label="68% (±1σ)"
)
# Shade 2σ
plt.fill_between(
    x,
    y,
    where=(x >= mu - 2 * sigma) & (x <= mu + 2 * sigma),
    alpha=0.2,
    label="95% (±2σ)",
)
# Shade 3σ
plt.fill_between(
    x,
    y,
    where=(x >= mu - 3 * sigma) & (x <= mu + 3 * sigma),
    alpha=0.1,
    label="99.7% (±3σ)",
)

plt.title("Empirical Rule Visualized with Density Plot")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.show()

##compute z score
mean = 143.5
std = 7.1
z = (157.7 - mean) / std  # 1.99 -> 2


##### Use Z-score to find proportion below a value
# Given a normal distribution with mean 150 and std 20, find the proportion of values
# user python to get proportion below z
z_score = (161.4 - 150) / 20  # 0.57

# get probablity use Z-table
from scipy.stats import norm

norm.cdf(z_score)  # the norm cdf gets P(x<=z)


# practice problem mean = 40 , std = 3 , value = 47.5
z_score = (47.5 - 40) / 3

print(
    f"The proportion of exampe scores are higher than Ludwig's score is {round(1 - norm.cdf(z_score), 4)}"
)

# standard normal table for porotion between two values
mean = 750
std = 60

z_score1 = (624 - mean) / std  # -2.1
z_score2 = (768 - mean) / std  # 0.3

norm.cdf(z_score2) - norm.cdf(z_score1)


##finding z score for a percentile
## given a probablity, calculate z score, and use mean and std to find out the value that corresponds to that z score
expected_z = norm.ppf(1 - 0.3)

x = expected_z * 9 + 80
print(f"the value that corresponds to the 70th percentile is {round(x, 2)}")

# getting the botton 10%
expected_z = norm.ppf(0.1)
x = expected_z * 11 + 185

# practice problem
mean = 80
std = 9

norm.ppf(0.4) * std + mean


### CDF and PDF
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x = np.linspace(-4, 4, 1000)
pdf = norm.pdf(x)  # PDF: bell-shaped - its just the curve's height. 感觉没啥用
cdf = norm.cdf(x)  # CDF: S-shaped

# Plot PDF
plt.subplot(1, 2, 1)
plt.plot(x, pdf, label="PDF")
plt.title("Probability Density Function")
plt.xlabel("x")
plt.ylabel("Density")
plt.grid(True)

# Plot CDF
plt.subplot(1, 2, 2)
plt.plot(x, cdf, label="CDF", color="green")
plt.title("Cumulative Distribution Function")
plt.xlabel("x")
plt.ylabel("Cumulative Probability")
plt.grid(True)

plt.tight_layout()
plt.show()
