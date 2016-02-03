# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 09:42:51 2015

@author: Georg
"""
import numpy as np
import matplotlib.pyplot as plt

def compute_price(p0, A, a, B, b, N):
    p = np.zeros(N+1)
    index_set = range(len(p))
    p[0] = p0
    for t in index_set[1:]:
        p[t] = (A*p[t-1] + np.log(1+p[t-1]) + B - b)/float(a)
    return p

def compute_supply(p, A, B):
    S = np.zeros_like(p)
    S = A*p + B + np.log(1+p)
    return S

p0 = 4.5
A  = 1.0
B  = 0
a  = -3.0
b  = 5.0
N  = 20

p = compute_price(p0, A, a, B, b, N)
S = compute_supply(p, A, B)

plt.plot(range(N+1), p, 'k-', label='price')
plt.hold('on')
plt.plot(range(1, N+1), S[:-1], 'b-', label='supply')
plt.legend(loc=1)

print "Stable price after N = %d steps: %g" % (N, np.mean(p[:-5]))
print "Stable supply after N = %d steps: %g" % (N, np.mean(S[:-5]))