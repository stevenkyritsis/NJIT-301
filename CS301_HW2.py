import numpy as np
from matplotlib import pyplot as plt
'''
import seaborn as sns

#1
sns.distplot(np.random.poisson(100, 10), kde = False)
plt.show()
'''

# poisson distribution data for y-axis
s = np.random.poisson(10, 100)

# showing the graph
plt.show()

'''

#2
def gradient_descent(x,y,theta,learning_rate=0.01,iterations=100):
 '''