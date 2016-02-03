# -*- coding: utf-8 -*-
"""
Created on Wed Sep 02 14:49:50 2015

@author: Georg
"""

import numpy as np
import matplotlib.pyplot as plt
from roots import *
from MinMax import *

def f(x):
    #return x**2*np.exp(-0.2*x)*np.sin(2*np.pi*x)
    return x**2 - 1   
    
def make_inverse(f, intervals, n_points=100):
    F = lambda gamma: f(gamma) - xi    
    g = []
    x_all = []
    for k in range(0, len(intervals), 2):
        a, b = intervals[k], intervals[k+1]
        x = [(b-a)/float(n_points)*i + a for i in range(n_points+1)]
    
        for i in range(len(x)):
            xi = x[i]
        
            if i == 0:
                gamma0 = x[0]
            else:
                gamma0 = g[i-1]
        
            n = Newton(F, dfdx='Numeric')
            gamma, F_value, expression, n = n.solve(gamma0, epsilon=1.0E-7, max_iter=100, store=False)
            g.append(gamma)
        x_all += x
    return g, x_all

m  = MinMax_v1(f, 0.01, 2, 1000)
mi = np.asarray(m.get_all_minima())
mi = list(mi[:,0])
ma = np.asarray(m.get_all_maxima())
ma = list(ma[:,0])
intervals = sorted(mi+ma)
intervals = sorted(intervals+intervals[1:-1])

for i in range(1, len(intervals)-1):
    if i % 2 != 0:
        intervals[i] -= 0.01
    else:
        intervals[i] += 0.01

g, x = make_inverse(f, intervals)
y = []
for i in x:
    y.append(f(i))
plt.rc('figure', figsize=(6,5))
plt.plot(x, y, 'b-', label='initial function')
plt.hold('on')
plt.plot(x, g, 'r-', label='inverse function')
plt.legend(loc='best')