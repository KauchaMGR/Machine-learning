# # import numpy 
# # x= numpy.random.uniform(0.0,0.5,20000)#creating random 250  float values betn 0 to 0.5
# # print(x)

# # #for visualizing the data 
# # import matplotlib.pyplot as plt
# # plt.hist(x,100)
# # plt.show()

# # for normal data distribution
# import numpy
# import matplotlib.pyplot as plt

# x = numpy.random.normal(5.0, 1.0, 100000)

# plt.hist(x, 100)
# plt.show()


# #Sactter plot using scattter() function
# import numpy
# import matplotlib.pyplot as plt

# x = numpy.random.normal(5.0, 1.0, 100000)
# y = numpy.random.normal(5.0, 1.0, 100000)

# plt.scatter(x,y)
# plt.show()

import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# slope,intercept,r,p ,std_Err=stats.linregress(x,y)

# def myfunc(x):
#     return slope*x+intercept

# y_value=list(map(myfunc,x))
# plt.scatter(x,y)
# plt.plot(x,y_value)

# plt.show()

#for polynomial equation line regression

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]


mymodel=np.poly1d(np.polyfit(x,y,3))
myline=np.linspace(1,22,100)

plt.scatter(x,y)
plt.plot(myline,mymodel(myline))
plt.show()