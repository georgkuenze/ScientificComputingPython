# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 23:00:33 2015

@author: Georg
"""

import numpy as np
import matplotlib.pyplot as plt

def func(t):
    return 1.0/np.sqrt(2*np.pi)*np.exp(-t**2)
    
a = -3.0
b =  3.0
n = 1000
h = (b-a)/float(n+1)

x = np.linspace(a,b,n+1)
index_set = range(len(x))
f = np.zeros(len(index_set))
I = np.zeros(len(index_set))
f[0] = func(a)
I[0] = 0
for i in index_set[1:]:
    f[i] = func(x[i])
    I[i] = I[i-1] + func(0.5*h + x[i])
    ## I[i] = I[i-1] + func(a + 0.5*h + i*h)
I *= h

plt.plot(x, f, 'k-', label='function')
plt.hold('on')
plt.plot(x, I, 'b.', label='integral')
plt.legend(loc='best')