# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 00:00:51 2015

@author: Georg
"""

import sys, random

np = 1
xp = int(sys.argv[1])   # point to reach
p  = float(sys.argv[2]) # probability to drift to the right
N  = int(sys.argv[3])   # no of experiment to average over

s = 0
for i in range(N):
    position = 0
    counter = 0
    while position < xp:
        r = random.random()
        if r <= p:
            position += 1
        else:
            position -= 1
        counter += 1
    s += counter

average = s/float(N)

print 'Particle with probability to drift right of %.2f walks from 0 to %d in %d steps on average.' \
% (p, xp, average)