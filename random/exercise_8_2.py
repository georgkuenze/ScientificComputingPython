# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 09:50:31 2015

@author: Georg
"""

from numpy import random
from numpy import where, logical_and, sum

for i in [1,2,3,6]:
    N = 10**i
    values = random.random(N)
    result = sum(where(logical_and(0.5 <= values, values <= 0.6), 1, 0))
    probability = result/float(N)
    print 'N = 10**%d random numbers between [0,1]; %.5f of values in interval [0.5, 0.6]' % (i, probability)