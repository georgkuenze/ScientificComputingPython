# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 17:56:08 2015

@author: Georg
"""

import numpy as np
from math import sqrt, pi
import random, time
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(8,8))

# Functions to calculate Pi using a Monte Carlo integration method
def MCint_v1(radius, N, interval):
    r = radius
    a = -1*r
    b = 1*r
    s = 0
    k_values = []
    pi_values = []
    
    for k in xrange(1, N+1):
        x = random.uniform(a, b)
        s += 2*sqrt(1-x**2)
        if k % interval == 0:
            integral = ((b-a)/float(k))*s
            _pi = integral/float(r)**2
            pi_values.append(_pi)
            k_values.append(k)
    
    integral = ((b-a)/float(N))*s
    _pi= integral/float(r)**2
    
    return _pi, k_values, pi_values

def MCint_v2(radius, N, arraysize):
    r = radius
    a = -1*r
    b = 1*r
    s = 0
    rest = N % arraysize
    batch_sizes = [arraysize] * (N//arraysize) + [rest]
    k_values = np.linspace(arraysize, N, arraysize)
    pi_values = []
    
    for batch_size, k_value in zip(batch_sizes, k_values):
        x = np.random.uniform(a, b, batch_size)
        s += np.sum(2*np.sqrt(1-x**2))
        integral = ((b-a)/float(k_value))*s
        _pi = integral/float(r)**2
        pi_values.append(_pi)
    
    pi_values = np.asarray(pi_values)
    integral = ((b-a)/float(N))*s
    _pi= integral/float(r)**2
    
    return _pi, k_values, pi_values

# Initial parameter
radius = 1

# Call and time functions
start = time.clock()
approx_1, k_values_1, pi_values_1 = MCint_v1(radius, 10**6, interval=10**3)
for i in xrange(len(pi_values_1)):
    pi_values_1[i] = abs(pi_values_1[i] - pi)
intermediate = time.clock()
approx_2, k_values_2, pi_values_2 = MCint_v2(radius, 10**6, arraysize=10**3)
pi_values_2 = np.absolute(pi_values_2 - np.pi)
end = time.clock()

# Print result and make plot
print 'Method1: Integral: %.4f   Exact: %.4f   Diff.: %.4f   time: %5.1f ms' \
% (approx_1, pi, abs(approx_1-pi), (intermediate-start)*10**3)
print 'Method2: Integral: %.4f   Exact: %.4f   Diff.: %.4f   time: %5.1f ms' \
% (approx_2, pi, abs(approx_2-pi), (end-intermediate)*10**3)
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.plot(k_values_1, pi_values_1)
ax1.set_title('Monte Carlo Integration - Method 1')
ax2 = fig.add_subplot(212)
ax2.plot(k_values_2, pi_values_2)
ax2.set_title('Monte Carlo Integration - Method 2')
fig.subplots_adjust(hspace=0.2)