# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 09:18:01 2015

@author: Georg
"""

import numpy as np
import matplotlib.pyplot as plt

# Define smoothed heaviside function
def H_eps(x, eps):
    if x < -eps:
        return 0
    elif -eps <= x <= eps:
        return 0.5 + x/(2.*eps) + 1/(2*np.pi)*np.sin((np.pi*x)/eps)
    else:
        return 1
    
# Define smoothed heaviside test function
def test_H_eps():
    eps = 0.01
    a = -2.*eps
    b =  2.*eps
    n = 100
    y = []
    x = [((b-a)/float(n))*i + a for i in range(0, n+1)]
    for i in range(len(x)):
        y.append(H_eps(x[i], eps))
    return x, y

# Run test
test_result_x, test_result_y = test_H_eps()

# Make plot of smoothed heaviside function
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(test_result_x, test_result_y, 'r-')
ax.set_xlim(-0.02, 0.02)
ax.set_ylim(-0.2, 1.2)