import numpy as np
import math


def factorial(i):
    return 0


for i in range(1, 10, 1):
    ff = 1
    for ii in range(1, i+1, 1):
        ff = ff*ii
    fff = np.exp(i*np.log(i)-i)
    j = i+1
    fffff = math.log2(0.5*(np.log(2*np.pi)-np.log(j)+j *
                 (2*np.log(j)+np.log(j*np.sinh(1/j)+1/810/j**6)-2)))
    print("{}  {} {}".format(i, math.log2(ff), np.exp(fffff)))
