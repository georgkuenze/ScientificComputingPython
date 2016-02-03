# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 23:51:05 2015

@author: Georg
"""
import numpy as np
import matplotlib.pyplot as plt

class Diff:
    def __init__(self, f, h=1E-05, dfdx_exact=None):
        if callable(f) and isinstance(h, (float, int)) and dfdx_exact is None:
            self.f, self.h, self.exact = f, float(h), None
        elif callable(f) and isinstance(h, (float, int)) and callable(dfdx_exact):
            self.f, self.h, self.exact = f, float(h), dfdx_exact
        else:
            raise ValueError('Function and exact derivative must be callable; h must be provided as float.')
    
    def error(self, x):
        if self.exact is not None:
            df_numerical = self(x)
            df_exact = self.exact(x)
            return abs(df_numerical - df_exact)

class Forward1(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(h+x) - f(x))/h
        
class Forward3(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (-(1./6)*f(x+2*h) + f(x+h) - 0.5*f(x) - (1./3)*f(x-h))/h
        
class Backward1(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x) - f(x-h))/h

class Central2(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x-h))/(2*h)

class Central4(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (4./3)*(f(x+h) - f(x-h))/(2*h) - (1./3)*(f(x+2*h) - f(x-2*h))/(4*h)

class Central6(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (3./2)*(f(x+h) - f(x-h))/(2*h) - (3./5)*(f(x+2*h) - f(x-2*h))/(4*h) \
        + (1./10)*(f(x+3*h) - f(x-3*h))/(6*h)

def function(x, mu=0.01):
    return (1-np.exp(x/float(mu)))/(1-np.exp(1.0/float(mu)))

def dfdx_exact(x, mu=0.01):
    return -1.*np.exp(x/float(mu))/(-1.*np.exp(1/float(mu))+1)

def table(f, x, h_values, methods, dfdx=None):
    print '      h      ',
    for method in methods:
        print '%-15s' % method.__name__,
    print
    for h in h_values:
        print '%10.2E' % h,
        for method in methods:
            if dfdx is not None:
                d = method(f, h, dfdx)
                output = d.error(x)
            else:
                d = method(f, h)
                output = d(x)
            print '%15.8E' % output,
        print

table(function, 0.0, [2**(-k) for k in range(20)], [Forward1, Forward3, Central2, Central4, Central6], dfdx=dfdx_exact)

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.plot(np.linspace(0,10,100), function(np.linspace(0,10,100), 1), label='mu=1.00')
ax1.legend(loc=1)
ax2 = fig.add_subplot(122)
ax2.plot(np.linspace(0,10,100), function(np.linspace(0,10,100), 0.1), label='mu=0.10')
ax2.legend(loc=1)