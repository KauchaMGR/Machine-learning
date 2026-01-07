# import numpy 
# x= numpy.random.uniform(0.0,0.5,20000)#creating random 250  float values betn 0 to 0.5
# print(x)

# #for visualizing the data 
# import matplotlib.pyplot as plt
# plt.hist(x,100)
# plt.show()

# for normal data distribution
import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()