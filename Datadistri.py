import numpy 
x= numpy.random.uniform(0.0,0.5,20000)#creating random 250  float values betn 0 to 0.5
print(x)

#for visualizing the data 
import matplotlib.pyplot as plt
plt.hist(x,100)
plt.show()