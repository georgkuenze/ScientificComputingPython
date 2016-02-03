# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 12:09:37 2015

@author: Georg
"""

import random
from exercise_8_19 import *

hat = Hat(blue=6, brown=8, green=3)

N = 10**6

counter = 0
for n in xrange(N):
    balls = hat.draw(6)
    if balls.count('brown') == 2 and balls.count('blue') == 2:
        counter += 1
    else:
        pass
    hat.putback(balls)
M = counter
p = M/float(N)

print 'Probability of drawing 2 brown and 2 blue from hat: %g' % (p)