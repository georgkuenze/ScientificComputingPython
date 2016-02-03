# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 23:31:33 2015

@author: Georg
"""

# import newly made module and others
from example_module import *
from math import *
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(15,15))

# Read in input from cml
f, a, b, eps = get_input()

# Calulate root with bysection function
root, i, liste = bisection(f, a, b, eps)

# Calculate x and y values to plot function
x, y = calc_vals(f, a, b)

x0 = root   # this is the approximate root
print "The root is %g, found in %d iterations" % (x0, i)

# Make plot
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax1.plot(x, y, 'k-', label='f(x)')
ax1.plot([min(x), max(x)], [0, 0], 'r--', label='y=0')
ax1.plot([liste[0][1], liste[0][1]], [max(y), min(y)], 'b-.', label='a')
ax1.plot([liste[0][2], liste[0][2]], [max(y), min(y)], 'b:', label='b')
ax1.set_ylim(min(y), max(y))
ax1.legend(loc=1)
ax1.set_title('The Bisection method, iteration %d, interval [%.2f, %.2f]' % (liste[0][0], liste[0][1], liste[0][2]))

ax2 = fig.add_subplot(222)
ax2.plot(x, y, 'k-', label='f(x)')
ax2.plot([min(x), max(x)], [0, 0], 'r--', label='y=0')
ax2.plot([liste[1][1], liste[1][1]], [max(y), min(y)], 'b-.', label='a')
ax2.plot([liste[1][2], liste[1][2]], [max(y), min(y)], 'b:', label='b')
ax2.set_ylim(min(y), max(y))
ax2.legend(loc=1)
ax2.set_title('The Bisection method, iteration %d, interval [%.2f, %.2f]' % (liste[1][0], liste[1][1], liste[1][2]))

ax3 = fig.add_subplot(223)
ax3.plot(x, y, 'k-', label='f(x)')
ax3.plot([min(x), max(x)], [0, 0], 'r--', label='y=0')
ax3.plot([liste[2][1], liste[2][1]], [max(y), min(y)], 'b-.', label='a')
ax3.plot([liste[2][2], liste[2][2]], [max(y), min(y)], 'b:', label='b')
ax3.set_ylim(min(y), max(y))
ax3.legend(loc=1)
ax3.set_title('The Bisection method, iteration %d, interval [%.2f, %.2f]' % (liste[2][0], liste[2][1], liste[2][2]))

ax4 = fig.add_subplot(224)
ax4.plot(x, y, 'k-', label='f(x)')
ax4.plot([min(x), max(x)], [0, 0], 'r--', label='y=0')
ax4.plot([liste[3][1], liste[3][1]], [max(y), min(y)], 'b-.', label='a')
ax4.plot([liste[3][2], liste[3][2]], [max(y), min(y)], 'b:', label='b')
ax4.set_ylim(min(y), max(y))
ax4.legend(loc=1)
ax4.set_title('The Bisection method, iteration %d, interval [%.2f, %.2f]' % (liste[3][0], liste[3][1], liste[3][2]))

plt.show()