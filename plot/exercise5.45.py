# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:00:33 2015

@author: Georg
"""

import numpy as np
import matplotlib.pyplot as plt
from itertools import chain

def plot_piecewise(data, xmax):
    x = list(chain.from_iterable((data[i][0], data[i][0]) for i in range(1, len(data))))
    x.insert(0, data[0][0])
    x.append(xmax)
    y = list(chain.from_iterable((data[i][1], data[i][1]) for i in range(len(data))))
    plt.plot(x,y)
    plt.axis([min(x), max(x), min(y)-1, max(y)+1])

data = [(0,-1), (1,1), (2.5,4)]
#plot_piecewise(data, 3)

def piecewise_constant_vec(x, data, xmax):
    conditions = []
    for i in range(len(data)-1):
        conditions.append(np.logical_and(data[i][0] <= x, x < data[i+1][0]))
    conditions.append(np.logical_and(data[-1][0] <= x, x <= xmax))
    
    r = np.where(conditions[0], data[0][1], data[0][1])
    for i in range(1, len(conditions)):
        r = np.where(conditions[i], data[i][1], r)
    return r

xmax = 5
x = np.linspace(-2, xmax, 1000)
y = piecewise_constant_vec(x, data, xmax)
plt.plot(x,y)
plt.axis([x.min(), x.max(), y.min()-1, y.max()+1])