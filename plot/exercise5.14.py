# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 18:32:48 2015

@author: Georg
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('xy.dat', dtype='float64')

x = data[:,0]
y = data[:,1]

plt.plot(x,y,'k.')
plt.xlabel('x')
plt.ylabel('y')

print "Mean = %.2f; Maximum = %.2f; Minimum = %.2f" % (np.mean(y), np.min(y), np.max(y))