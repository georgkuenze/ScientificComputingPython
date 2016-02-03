# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 19:12:06 2015

@author: Georg
"""
import sys
from math import *

def Poisson(x, t, nu):
    x = float(x)
    return ((nu*t)**x)/factorial(x) * exp(-nu*t)

def get_input():
    if len(sys.argv) < 4:
        raise IndexError("Not enough values provided. Type in: 'x t nu'")
    elif len(sys.argv) > 4:
        raise IndexError("Too many values provided. Type in: 'x t nu'")
    try:
        x, t, nu = [eval(sys.argv[i]) for i in range(1, len(sys.argv))]
    except ValueError:
        raise ValueError("Value must be number not String")
    return x, t, nu

x, t, nu = get_input()
P = Poisson(x, t, nu)
print "Probability is %g." % (P)