# import numpy

# speed = [99,99,86,87,88,111,86,103,87,94,78,73,47,5,23,85,86]

# x = numpy.mean(speed)
# y= numpy.median(speed)

# print("the mean speed is",x)
# print("the median speed is",y)

from scipy import stats

sped = [99,86,87,88,111,86,103,87,94,54,78,74,37,85,86]

y = stats.mode(sped)

print(y)