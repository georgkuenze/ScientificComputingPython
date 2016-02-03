# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 18:06:42 2015

@author: Georg
"""

import numpy as np
from collections import OrderedDict
import time

def compute_probability_v1(r, n):
    P = OrderedDict()
    for element in n.tolist():
        m = 0
        for i in range(int(element)):
            if r[i] == 0: # head
                m += 1
        P[int(element)] = m/float(element)
    return P

def compute_probability_v2(r, n):
    head = np.where(r == 0, 1, 0)
    N = len(r)
    p = np.zeros(N)
    for i in range(N):
        p[i] = np.sum(head[:i+1])/float(i+1)
    
    P = OrderedDict()
    for element in n.tolist():
        P[int(element)] = p[element]
    return P

def compute_probability_v3(r, n):
    head = np.where(r == 0, 1, 0)
    N = len(r)
    p = np.zeros(N)
    q = np.cumsum(head)
    I = np.arange(1,N+1)
    p = np.true_divide(q,I)

    P = OrderedDict()
    for element in n.tolist():
        P[int(element)] = p[element]
    return P
    
def format_p_table(P):
    print '     N   p_N\n%s' % (13*'-')
    for k, v in P.items():
        print '%6d %.4f' % (k, v)

# Parameter and N times throws of coin
N = 10**5
N_1 = np.asarray([N*10**(-1*i) for i in range(4,0,-1)])
coins = np.random.randint(0,2,size=N)

# Method 1
start = time.time()
P = compute_probability_v1(coins, N_1)
stop = time.time()
print 'Probability array: '
format_p_table(P)
print 'Method1 - Elabsed time for computation: %g microsec' % ((stop-start)*10**6)

# Method 2
start = time.time()
P = compute_probability_v2(coins, N_1)
stop = time.time()
print 'Probability array: '
format_p_table(P)
print 'Method2 - Elabsed time for computation: %g microsec' % ((stop-start)*10**6)

# Method 3
start = time.time()
P = compute_probability_v3(coins, N_1)
stop = time.time()
print 'Probability array: '
format_p_table(P)
print 'Method3 - Elabsed time for computation: %g microsec' % ((stop-start)*10**6)