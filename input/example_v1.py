# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 17:44:44 2015

@author: Georg
"""

import argparse
import sys
from scitools.StringFunction import StringFunction
from math import *
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(15,15))


parser = argparse.ArgumentParser()
parser.add_argument('--a', type=float, default=0.0, help='left limit', metavar='a')
parser.add_argument('--b', type=float, default=1.0, help='right limit', metavar='b')
parser.add_argument('--e', type=str, default='0.0', help='epsilon', metavar='e')
parser.add_argument('--f', type=str, default='0.0', help='function', metavar='f')

args = parser.parse_args()
a = args.a; b = args.b
f = StringFunction(args.f)
eps = eval(args.e)

fa = f(a)
if fa*f(b) > 0:
    print "f(x) does not change sign in [%g, %g]." % (a, b)
    sys.exit(1)

x = [((b-a)/1000.0)*x + a for x in range(1000)]
y = [f(k) for k in x]

i = 0   # iteration counter
analysis = []
while (b - a) > eps:
    i += 1
    m = (a + b)/2.0
    fm = f(m)
    if fa*fm <= 0:
        b = m   # root is in the left half of [a,b]
    else:
        a = m   # root is in the right half of [a,b]
        fa = fm
    print 'Iteration %d: interval=[%g, %g]' % (i, a, b)
    analysis.append([i, a, b])

x0 = m   # this is the approximate root
print "The root is %g, found in %d iterations" % (x0, i)

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax1.plot(x, y, 'k-', label='f(x)')
ax1.plot([min(x), max(x)], [0, 0], 'r--', label='y=0')
ax1.plot([analysis[0][1], analysis[0][1]], [max(y), min(y)], 'b-.', label='a')
ax1.plot([analysis[0][2], analysis[0][2]], [max(y), min(y)], 'b:', label='b')
ax1.set_ylim(min(y), max(y))
ax1.legend(loc=1)
ax1.set_title('The Bisection method, iteration %d, interval [%.2f, %.2f]' % (analysis[0][0], analysis[0][1], analysis[0][2]))

ax2 = fig.add_subplot(222)
ax2.plot(x, y, 'k-', label='f(x)')
ax2.plot([min(x), max(x)], [0, 0], 'r--', label='y=0')
ax2.plot([analysis[1][1], analysis[1][1]], [max(y), min(y)], 'b-.', label='a')
ax2.plot([analysis[1][2], analysis[1][2]], [max(y), min(y)], 'b:', label='b')
ax2.set_ylim(min(y), max(y))
ax2.legend(loc=1)
ax2.set_title('The Bisection method, iteration %d, interval [%.2f, %.2f]' % (analysis[1][0], analysis[1][1], analysis[1][2]))

ax3 = fig.add_subplot(223)
ax3.plot(x, y, 'k-', label='f(x)')
ax3.plot([min(x), max(x)], [0, 0], 'r--', label='y=0')
ax3.plot([analysis[2][1], analysis[2][1]], [max(y), min(y)], 'b-.', label='a')
ax3.plot([analysis[2][2], analysis[2][2]], [max(y), min(y)], 'b:', label='b')
ax3.set_ylim(min(y), max(y))
ax3.legend(loc=1)
ax3.set_title('The Bisection method, iteration %d, interval [%.2f, %.2f]' % (analysis[2][0], analysis[2][1], analysis[2][2]))

ax4 = fig.add_subplot(224)
ax4.plot(x, y, 'k-', label='f(x)')
ax4.plot([min(x), max(x)], [0, 0], 'r--', label='y=0')
ax4.plot([analysis[3][1], analysis[3][1]], [max(y), min(y)], 'b-.', label='a')
ax4.plot([analysis[3][2], analysis[3][2]], [max(y), min(y)], 'b:', label='b')
ax4.set_ylim(min(y), max(y))
ax4.legend(loc=1)
ax4.set_title('The Bisection method, iteration %d, interval [%.2f, %.2f]' % (analysis[3][0], analysis[3][1], analysis[3][2]))

plt.show()