# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 21:23:19 2015

@author: Georg
"""

import sys
N = int(sys.argv[1])
r = int(sys.argv[2])

import numpy as np

eyes = np.random.random_integers(1,6, size=(4,N))
summe = np.sum(eyes, axis=0)
M = np.sum(np.where(summe < 9, 1, 0))
p = M/float(N)
capital = -1*N + r*M - 1*(N-M)
fair = 2/p -1

print 'Probability: %g' % p
print 'Capital with r = %d Euro: %g Euro' % (r, capital)
print 'Fair winning award is: %g Euro' % (fair)
print 'Capital with %g Euro: %g Euro' % (fair, -1*N + fair*M - 1*(N-M))