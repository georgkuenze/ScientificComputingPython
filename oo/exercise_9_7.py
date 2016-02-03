# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 23:35:30 2015

@author: Georg
"""

class F:
    def __init__(self, a, b):
        self.a, self.b = a, b
    
    def __call__(self, t):
        from math import exp, sin
        return exp(-self.a*t)*sin(self.b*t)

class Fs(F):
    def __init__(self, t, a):
        F.__init__(self, a, b=1)
        self.t = t
    
    def __call__(self, b):
        F.__init__(self, self.a, b)
        return F.__call__(self, self.t)

f = Fs(t=2, a=4.5)
print f(3)
print f.__dict__
