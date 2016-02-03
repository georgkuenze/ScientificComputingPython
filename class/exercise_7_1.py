# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 23:06:02 2015

@author: Georg
"""

from math import sin, exp

class F:
    def __init__(self, alpha, omega):
        self.a = alpha
        self.o = omega
    
    def __call__(self, x):
        self.x = x
        return exp(-self.a*self.x)*sin(self.o*self.x)
    
    def __str__(self):
        return 'exp(-%g*x)*sin(%g*x)' % (self.a, self.o)
    
    def __repr__(self):
        return '%s(a=%g, w=%g)' % (self.__class__.__name__, self.a, self.o)        