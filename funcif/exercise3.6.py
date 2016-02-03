# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 13:48:21 2015

@author: Georg
"""

import numpy as np
from scipy.integrate import quad

# Approximation of integral with one trapezoid
def trapezint1(f, a, b):
    integral = ((b-a)/2.)*(f(a) + f(b))
    return integral

exact_int = []
trapezint1_int = []
functions = [np.sin, np.cos]

for f in functions:
    exact_int.append(quad(f, 0, np.pi)[0])
    trapezint1_int.append(trapezint1(f, 0, np.pi))

print "Approximation of integral with one trapezoid" 
for f, i, j in zip(functions, exact_int, trapezint1_int):
    print "Function: %s; exact integral: %.5e; trapez integral: %.5e, Error: %.5e" % (f.__name__, i, j, abs(i-j))

# Approximation of integral with two trapezoids
def trapezint2(f, a, b):
    n = 2
    integral = 0
    x = [(b-a)/float(n)*i + a for i in range(0, n+1)]
    for i in range(len(x)-1):
        integral += 0.5*((b-a)/float(n))*(f(x[i]) + f(x[i+1]))
    return integral

trapezint2_int = []

for f in functions:
    trapezint2_int.append(trapezint2(f, 0, np.pi))

print "\nApproximation of integral with two trapezoids" 
for f, i, j in zip(functions, exact_int, trapezint2_int):
    print "Function: %s; exact integral: %.5e; trapez integral: %.5e, Error: %.5e" % (f.__name__, i, j, abs(i-j))
    
# Approximation of integral with n-times trapezoids
def trapezintn(f, a, b, n):
    integral = 0
    x = [(b-a)/float(n)*i + a for i in range(0, n+1)]
    for i in range(len(x)-1):
        integral += 0.5*((b-a)/float(n))*(f(x[i]) + f(x[i+1]))
    return integral

trapezintn_int = []
n = 1000

for f in functions:
    trapezintn_int.append(trapezintn(f, 0, np.pi, n))

print "\nApproximation of integral with %s-times trapezoids" % (n)
for f, i, j in zip(functions, exact_int, trapezintn_int):
    print "Function: %s; exact integral: %.5e; trapez integral: %.5e, Error: %.5e" % (f.__name__, i, j, abs(i-j))

# Approximation with mid point rule
def midpoint(f, a, b, n):
    integral = 0
    x = [(b-a)/float(n)*i + a for i in range(0, n+1)]
    for i in range(len(x)-1):
        integral += (b-a)/float(n)*f(a + x[i] + 0.5*((b-a)/float(n)))
    return integral
    
midpoint_int = []
n = 1000

for f in functions:
    midpoint_int.append(midpoint(f, 0, np.pi, n))

print "\nApproximation of integral with %s-times rectangles" % (n)
for f, i, j in zip(functions, exact_int, midpoint_int):
    print "Function: %s; exact integral: %.5e; trapez integral: %.5e, Error: %.5e" % (f.__name__, i, j, abs(i-j))

# Define an adaptive trapezoid
def adaptive_trapezint(f, a, b, eps):
    c = 10000    
    x = [(b-a)/float(c)*i + a for i in range(0, c+1)]
    f_two_prime = []
    for i in range(1, len(x)-1):
        f_two_prime.append((f(x[i+1]) - 2*f(x[i]) + f(x[i-1]))/((b-a)/float(c))**2)     
    h = np.sqrt(12*eps)*((b-a)*max(abs(j) for j in f_two_prime))**(-0.5)
    n = (b-a)/h
    return n

no_intervals = []
eps = 1e-16

for f in functions:
    no_intervals.append(adaptive_trapezint(f, 0, np.pi, eps))
    
print "\nNumer of trapezoids needed for approximation with error < %.e" % (eps)
for f, i in zip(functions, no_intervals):
    print "Function: %s; no of trapezoids: %.f" % (f.__name__, i)
