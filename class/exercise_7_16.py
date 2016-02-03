# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 14:30:40 2015

@author: Georg
"""

import sympy
import numpy as np

class Central:
    def __init__(self, arg, h=1E-5):
        if callable(arg) and isinstance(h, (float, int)):
            self.f = arg
            self.h = float(h)
        else:
            raise TypeError('Argument 1 must be a python function.')
    
    def __call__(self, x):
        return (self.f(x+self.h) - self.f(x-self.h))/(2*self.h)
        

def table(f, xp, h=1E-5):
    x = sympy.Symbol('x')
    f_expr = f
    df_expr = sympy.diff(f_expr)
    df_exact = sympy.lambdify([x], df_expr)
    
    f_plain = sympy.lambdify([x], f_expr)
    df_appr = Central(f_plain, h)
    
    return df_exact(xp), df_appr(xp)


f = x*sympy.sin(2*x)             # Sympy expression
xp = np.linspace(0, 2*np.pi, 50) # Numpy array of x values

print "Exact vs. numerical differentiation"
print "exact value  approx. value  difference\n%s" % (38*'-')
for ix in xrange(len(xp)):
    exact, appr = table(f, xp[ix])
    diff = abs(exact - appr)
    print '%8.3f %13.3f %15.3e' % (exact, appr, diff)