# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 22:58:47 2015

@author: Georg
"""

class FuncWithDerivative:
    def __init__(self, h=1.0E-5):
        self.h = h
    
    def __call__(self, x):
        raise NotImplementedError('__call__ missing in class %s') % self.__class__.__name__
    
    def df(self, x):
        h = self.h
        return (self(x+h) - self(x-h))/(2.0*h)
    
    def ddf(self, x):
        h = self.h
        return (self(x+h) - 2*self(x) + self(x-h))/(float(h)**2)

class Sine1(FuncWithDerivative):
    def __call__(self, x):
        from math import sin        
        return sin(x)

class Sine2:
    def __call__(self, x):
        from math import sin        
        return sin(x)
    
    def df(self, x):
        from math import cos
        return cos(x)
    
    def ddf(self, x):
        from math import sin
        return -sin(x)

def table_d(x_values, h_values, methods):
    print '      x         h      ',
    for method in methods:
        print '%-14s' % method.__name__,
    print
    for x in x_values:
        for h in h_values:
            print '%10.2E' % x, '%10.2E' % h,
            for method in methods:
                if issubclass(method, FuncWithDerivative):
                    s = method(h)
                    df = s.df(x)
                else:
                    s = method()
                    df = s.df(x)
                print '%13.6E' % df,
            print
        print
from math import pi
table_d([0,0.5*pi, pi, 1.5*pi, 2.0*pi], [2**(-k) for k in range(10)], [Sine1, Sine2])