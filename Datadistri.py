import numpy 
x= numpy.random.uniform(0.0,0.5,250)#creating random 250  float values betn 0 to 0.5
print(x)

#for visualizing the data 
import matplotlib.pyplot as plt
plt.hist(x,5)
plt.show()