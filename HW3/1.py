import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics

# Plot between -10 and 10 with .001 steps.
x_axis = np.arange(10, 30, 0.01)

# Calculating mean and standard deviation
mean = 20
sd = math.sqrt(3)

plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
plt.show()