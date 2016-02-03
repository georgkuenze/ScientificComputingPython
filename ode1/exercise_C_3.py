# -*- coding: utf-8 -*-
"""
Created on Wed Oct 07 16:08:04 2015

@author: Georg
"""

import numpy as np
import matplotlib.pyplot as plt

dt = [1.00, 0.25, 0.01]
epsilon = 1.0E-03

def compute_ode(dt):
    n = int(4.0/dt)
    x = np.linspace(0.0,4.0,n+1)
    y = np.zeros(n+1)
    y[0] = 1+np.sqrt(epsilon)
    for k in range(n):
        y[k+1] = dt/(2*(y[k] - 1)) + y[k]
    return x, y

for value in dt:
    x, y = compute_ode(value)
    plt.plot(x, y, lw=5, label='dt = %.2f' % value)

x_coor = np.linspace(0,4,1001); y_exact = 1 + np.sqrt(x_coor + epsilon)
plt.hold('on')
plt.plot(x_coor, y_exact, 'b.', label='exact solution')
plt.legend(loc='best')