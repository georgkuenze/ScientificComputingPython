# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 21:52:41 2015

@author: Georg
"""

import random

N = 10**6
m = []

for n in xrange(N):
    Success = True
    previous = random.randint(1,6)
    counter = 1
    while Success == True:
        actual = random.randint(1,6)
        if actual > previous:
            counter += 1
            previous = actual
        else:
            Success = False
    m.append(counter)

p = {}
r = {}
for i in range(2,7):
    exec('p_%d = m.count(%d)/float(N)' % (i,i))
    exec('p[%d] = p_%d' % (i,i))
    exec('r_%d = 1/p_%d' % (i,i))
    exec('r[%d] = r_%d' % (i,i))

print 'm   probability   fair winning award\n%s' % (36*'-')
for i in range(2,7):
    print '%d     %.5f    %12.2f Euro' % (i, p[i], r[i])