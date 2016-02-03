# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 09:42:39 2015

@author: Georg
"""

import random

def flip_coin(N):
    head = 0
    for n in xrange(N):
        result = random.randint(0,1)
        if result == 0:
            head += 1
            print '%4d. flip: %s' % (n+1, 'head')
        else:
            print '%4d. flip: %s' % (n+1, 'tail')
    print '\nResult: %g x head, %g x tail' % (head, N-head)

flip_coin(50)