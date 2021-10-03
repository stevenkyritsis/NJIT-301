import numpy as np
from matplotlib import pyplot as plt
'''
import seaborn as sns

#1
sns.distplot(np.random.poisson(100, 10), kde = False)
plt.show()
'''

# creating a numpy array for x-axis
# using step size as 1
x = np.arange(0, 100, 1)

# poisson distribution data for y-axis
y = np.random.poisson(x, 10)

# showing the graph
plt.show()

'''

#2
def gradient_descent(x,y,theta,learning_rate=0.01,iterations=100):
 '''