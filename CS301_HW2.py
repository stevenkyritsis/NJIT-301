import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

sns.distplot(np.random.poisson(100, 10), kde = False)
plt.show()