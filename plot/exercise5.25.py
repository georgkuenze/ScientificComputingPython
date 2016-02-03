# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 22:11:02 2015

@author: Georg
"""

from numpy import *
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(6, 9))
from scitools.StringFunction import StringFunction

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

# Define plotting function
def graph(f, n, xmin, xmax, resolution=1001):
    f.vectorize(globals())    
    xp = linspace(xmin, xmax, n)
    yp = f(xp)
    
    x = linspace(xmin, xmax, resolution)
    y = zeros(x.size, dtype='float64')
    for ix in xrange(len(x)):
        y[ix] = p_L(x[ix], xp, yp)
    
    return x, y, xp, yp

f = StringFunction('abs(x)', independent_variable='x')
xmin = -2
xmax = 2
n = [2, 4, 6, 10, 13, 20]

fig, axarr = plt.subplots(2, 3, sharex='col', sharey='row')
counter = 0
for i in range(2):
    for j, k in zip(range(3), n[counter:counter+3]):
        x, y, xp, yp = graph(f, k, xmin, xmax, resolution=1001)
        axarr[i, j].plot(x, y, 'b-', xp, yp, 'ro')
        axarr[i, j].set_title('n = %d' % (k))

    counter += 3
    
fig.text(0.5, 0.08, 'x', ha='center')
fig.text(0.06, 0.5, 'f(x)', ha='center', rotation='vertical')