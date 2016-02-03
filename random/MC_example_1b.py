# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 15:54:05 2015

@author: Georg
"""

# Program to compute the probability that when throwing two dies
# black and green, the black one shows the larger number

import sys
N = int(sys.argv[1])

import numpy as np

numbers = np.random.random_integers(1,6, size=(2,N))
black = numbers[0,:]
green = numbers[1,:]

money = 10 - N   # Start capital is 10, -1 for every throw
success = black > green
M = np.sum(success)
p = M/float(N)
money += 2.4*M
print 'Probability: %g' % p
print 'Capital after %d throws: %g' % (N, money)