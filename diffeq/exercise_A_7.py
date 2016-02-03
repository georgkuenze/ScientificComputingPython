# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 16:56:29 2015

@author: Georg
"""
import numpy as np

x0 = 100                    ## initial amount
p = 5                       ## interest rate
N = 4                       ## number of years
index_set = range(N+1)
x = np.zeros(len(index_set))

# Compute solution
x[0] = x0
for i in index_set[:-1]:
    x[i+1] = x[i] + (p/100.0)*x[i]
print x