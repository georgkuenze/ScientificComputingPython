# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 19:02:27 2015

@author: Georg
"""

from math import *

def binomials(x, n, p):
    x = float(x)
    return (factorial(n)/(factorial(x)*factorial(n-x)) * p**x * (1-p)**(n-x))

print 1-binomials(0, 5, 1/120.)