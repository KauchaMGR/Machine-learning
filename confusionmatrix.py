import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt

actual=np.random.binomial(1,0.9,1000)
predicted=np.random.binomial(1,0.9,1000)

plt.plot(actual,predicted)
plt.show()