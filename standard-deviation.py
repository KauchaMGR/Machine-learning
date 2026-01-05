import numpy

seed = [86,87,88,86,87,83,56]

x = numpy.std(seed)

print("standard deviation of given data ",x)

ages = [5,31,43,48,50,41,7,11,15,39,80,82,45,32,2,8,6,25,36,27,51,33]

y= numpy.percentile(ages, 75)

print("THe percentile of given  age",x)
