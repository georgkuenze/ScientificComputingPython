# -*- coding: utf-8 -*-
"""
Created on Wed Sep 02 10:24:29 2015

@author: Georg
"""

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

__all__ = ['Diff', 'Forward1', 'Forward3', 'Backward1', 'Central2', 'Central4', 'Central6']