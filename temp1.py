# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 19:14:39 2017

@author: ganesh
"""
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
plt.axis([0,10,0,10])

i=0
x=list()
y=list()

while i <50:
    temp_y=np.random.random()*10
    x.append(i)
    y.append(temp_y)
    plt.scatter(i,temp_y)
    i+=1
    plt.draw()
    plt.pause(0.01)