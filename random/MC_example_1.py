# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 15:44:40 2015

@author: Georg
"""
# Program to compute the probability that when throwing two dies
# black and green, the black one shows the larger number

import sys
N = int(sys.argv[1])

import random
M = 0   # Number of successful events
money = 10   # Start capital
for i in range(N):
    money -= 1
    black = random.randint(1,6)
    green = random.randint(1,6)
    if black > green:
        M += 1
        money += 2.5
p = M/float(N)
print 'Probability: %g' % p
print 'Capital after %d throws: %g' % (N, money)