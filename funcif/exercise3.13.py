# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 22:21:41 2015

@author: Georg
"""

import numpy as np

# define function for approximation of pi with polygon
def pathlength(n):
    x = [0.5*np.cos(2*np.pi*i/float(n)) for i in range(0, n+1)]
    y = [0.5*np.sin(2*np.pi*i/float(n)) for i in range(0, n+1)]
    L = 0
    for i, j in zip(range(len(x)-1), range(len(y)-1)):
        L += np.sqrt((x[i+1] - x[i])**2 + (y[j+1] - y[j])**2)
    return L

n = [2**i for i in range(2,11)]
exact_circumference = np.pi

print "Approximation of pi with polygon n-1 lines"
for i in range(len(n)):
    approx_pi = pathlength(n[i])
    error = abs(approx_pi - exact_circumference)
    print "n = %4d; approx. circumference: %.6e; error: %.6e" % (n[i], approx_pi, error)