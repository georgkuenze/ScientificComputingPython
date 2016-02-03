# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 10:28:12 2015

@author: Georg
"""
from numpy import *
import matplotlib.pyplot as plt

xp = array([-1, 1, 2], dtype='float64')
yp = array([0, 3, 1], dtype='float64')

# Define Lagrange's polynomial interpolation formula
def p_L(x, xp, yp):
    Ls = zeros(xp.size, dtype='float64')
    p = 0
    
    for index, k in enumerate(xp):
        i = xp[where(xp!=k)]
        L = 1
        for j in xrange(len(i)):
            L *= ((x - i[j])/(float(k) - i[j]))
        Ls[index] = L
            
    for j,l in zip(yp, Ls):
        p += j*l
    
    return p

# Define test function i.e. test yp identity
def test_p_L(xp, yp, eps=1.0e-16):
    if all([abs(yp[i] - p_L(xp[i], xp, yp)) < eps for i in range(len(xp))]):
        print "Lagrange's interpolation at knot points correct."
    else:
        print "Lagrange's interpolation at knot points not correct."


x = linspace(-5,5,100)
y = zeros(x.size, dtype='float64')
for ix in xrange(len(x)):
    y[ix] = p_L(x[ix], xp, yp)

plt.plot(x,y)
plt.hold('on')
plt.plot(xp,yp,'ro')
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(x.min(), x.max())

test_p_L(xp, yp, eps=1.0e-16)