# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 23:45:45 2015

@author: Georg
"""

import numpy as np
from math import factorial

def exact_binomial(p, n, x):
    B = factorial(float(n))/(factorial(x)*factorial(n-x)) * p**x * (1-p)**(n-x)
    return B

def simulate_binomial(N, p, n, x):
    M = 0   # number of experiments with successful outcome
    for i in xrange(N):
        experiments = np.random.random(n)
        m = np.sum(np.where(experiments < p, 1, 0))
        if m == x:
            M += 1
        else:
            pass
    B = M/float(N)
    return B


# First Experiment: Throwing a coin 5 times.
# Success is when head is two times.

n = 5   # number of experiments
p = 0.5   # probability of a single event
x = 2   # number of successful events

exact = exact_binomial(p, n, x)
approx = simulate_binomial(10**6, p, n, x)

print 'First Experiment: Throwing a coin.'
print 'Exact = %.5f; Approximation = %.5f; Error = %.5f' % (exact, approx, abs(exact-approx))

# Second Experiment: Throwing a die 4 times.
# Success is when number one occurs 4 times.

n = 4   # number of experiments
p = 1/6.0   # probability of a single event
x = 4   # number of successful events

exact = exact_binomial(p, n, x)
approx = simulate_binomial(10**6, p, n, x)

print '\nSecond Experiment: Throwing a die.'
print 'Exact = %.5f; Approximation = %.5f; Error = %.5f' % (exact, approx, abs(exact-approx))

# Third Experiment: Ski break.

n = 5   # number of experiments
p = 1/120.   # probability of a single event
x = 0   # number of successful events

exact = exact_binomial(p, n, x)
approx = simulate_binomial(10**6, p, n, x)

print '\nThird Experiment: Ski break.'
print 'Exact = %.5f; Approximation = %.5f; Error = %.5f' % (1 - exact, 1 - approx, abs(exact-approx))