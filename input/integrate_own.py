# -*- coding: utf-8 -*-
"""
Created on Thu Jul 09 12:00:58 2015

@author: Georg
"""

from math import *
import sys

def midpoint(f, a, b, n=200):
    h = (b-a)/float(n)
    I = 0
    for i in range(n):
        I += f(a + i*h + 0.5*h)
    return h*I

formula = sys.argv[1]
a = eval(sys.argv[2])
b = eval(sys.argv[3])
if len(sys.argv) >= 5:
    n = int(sys.argv[4])
else:
    n = 200
    
code = """
def g(x):
    return %s
""" % (formula)
exec(code)

result = midpoint(g, a, b, n=n)
print "Integral of %s in boundaries [%.3f, %.3f] approximated with n=%d rectangles is %.3f." % (formula, a, b, n, result)