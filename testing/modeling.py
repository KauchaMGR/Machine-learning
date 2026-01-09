import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2)

x=np.random.normal(3,1,100)

y=np.random.normal(150,40,100)/x
train_x=x[:80]
train_y=y[:80]
plt.scatter(train_x,train_y)
plt.show()
