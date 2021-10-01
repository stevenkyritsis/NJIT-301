import numpy as np
from matplotlib import pyplot as plt
'''
import seaborn as sns

#1
sns.distplot(np.random.poisson(100, 10), kde = False)
plt.show()
'''
from scipy.stats import poisson

# importing poisson fro scipy
from scipy.stats import poisson

# importing numpy as np
import numpy as np

# importing matplotlib as plt
import matplotlib.pyplot as plt


# creating a numpy array for x-axis
# using step size as 1
x = np.arange(0, 100, 1)

# poisson distribution data for y-axis
y = poisson.pmf(x, mu=10, loc=0)


# plotting the graph
plt.plot(x, y)

# showing the graph
plt.show()

'''

#2
def gradient_descent(x,y,theta,learning_rate=0.01,iterations=100):
 '''