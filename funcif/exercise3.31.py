# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 12:52:45 2015

@author: Georg
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

# Define function for approximation of cosine
def cos_sum(x, n):
    term = 1
    s = term
    for j in range(n):
        j += 1
        term = -term * (x**2/(2.0*j*(2.0*j - 1)))
        s += term
    return s

# Test approximation function by calculating test data
x = np.linspace(0*np.pi, 10*np.pi, 100)
no_iter = [5,25,50,100,200] # number of sum terms
labels = ["n = " + str(a) for a in no_iter]
elist = [np.zeros(100, dtype='float') for i in xrange(len(no_iter))]
y_list = np.rec.array(elist, names=labels)

# Loop over number of sum terms and calculate y
for i, name in zip(range(len(no_iter)), labels):
    y_list[name] = cos_sum(x, no_iter[i])

# Make plots
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, np.cos(x), 'k.', lw=1)
color = iter(cm.rainbow(np.linspace(0,1,len(no_iter))))
for name in (labels):
    c=next(color)
    ax.plot(x, y_list[name], color=c, ls='-', lw=2, label=name)
ax.legend(loc='best')
ax.set_ylim(-1.4, 1.4)

# Define function for error calculation
def error_sum(x, n):
    # Prepare arrays to write in data
    exact = np.zeros((len(x), len(n)))
    approx = np.zeros((len(x), len(n)))
    error = np.zeros((len(x), len(n)))
    
    # Loop over input values to calc data
    for i in range(len(x)):     
        exact[i] = np.cos(x[i])
    for i in range(len(x)):
        for j in range(len(n)):
            approx[i][j] = cos_sum(x[i], n[j])
    
    # Calculate error
    error = abs(exact - approx)

    # Print result
    table = []
    table.append(["x"] + [str(a) for a in n])
    for i in range(len(x)):
        table.append([x[i]] + [a for a in error[i]])
    for j in range(len(n)+1):
        print "  %8s" % (table[0][j]),
    print
    for k in range(1, len(x)+1):
        print "%10.4f" % (table[k][0]),
        for j in range(1, len(n)+1):
            print  "%10.4e" % (table[k][j]),
        print

print "Error compared to exact value for increasing number of iterations:\n"
error_sum([a*np.pi for a in range(4,12,2)], [5, 25, 50, 100, 200])