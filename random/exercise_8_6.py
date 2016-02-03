# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 16:49:15 2015

@author: Georg
"""

import sys
import numpy as np

if len(sys.argv) >= 3:
    n = int(sys.argv[1])
    N = int(sys.argv[2])
else:
    raise ValueError('You provided not enough input values')

eyes = np.random.random_integers(1,6, size=(n,N))
M = 0
for i in range(N):
    if 6 in eyes[:,i]:
        M += 1
    else:
        M += 0
p = M/float(N)
print 'Probability of throwing one six with %d dies: %g' % (n, p)