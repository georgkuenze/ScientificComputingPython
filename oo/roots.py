# -*- coding: utf-8 -*-
"""
Created on Wed Sep 02 14:50:59 2015

@author: Georg
"""

class Diff:
    def __init__(self, f, h=1E-08):
        if callable(f) and isinstance(h, (float, int)):
            self.f, self.h = f, float(h)
        else:
            raise ValueError('Function must be callable; h must be provided as float.')

    def central(self, x):
        # differentiation with central method
        f, h = self.f, self.h
        return (f(x+h) - f(x-h))/(2*h)

class Root:
    def __init__(self, f, dfdx='Numeric'):
        self.f = f
        if callable(dfdx):
            self.dfdx = dfdx
        elif dfdx == 'Numeric':
            self.dfdx = Diff(f)
    
    def solve(self, epsilon=1.0E-7, N=100, store=False):
        raise NotImplementedError('No root finding rule in class %s' 
        % self.__class__.__name__)


class Newton(Root):    
    def solve(self, x, epsilon=1.0E-7, max_iter=100, store=False):
        f, dfdx = self.f, self.dfdx
        f_value = f(x)
        n = 0
        
        if store is True: 
            info = [(x, f_value)]
        
        while abs(f_value) > epsilon and n <= max_iter:
            dfdx_value = dfdx.central(x) if isinstance(dfdx, Diff) else float(dfdx(x))
            if abs(dfdx_value) < 1E-14:
                raise ValueError("f'(%g)=%g is very small and leads to zero divison error" \
                % (x, dfdx_value))
            
            x = x - f_value/dfdx_value
            
            n += 1
            f_value = f(x)
            if store is True:
                info.append((x, f_value))
        
        expression = 'x0 found' if abs(f_value) < epsilon else 'x0 not found'
        
        if store is True:
            return x, info, expression
        else:
            return x, f_value, expression, n
            
            
class Secant(Root):
    def solve(self, a, b, epsilon=1.0E-7, max_iter=100, store=False):
        f = self.f
        fa = f(a)
                
        if fa*f(b) > 0:
            raise ValueError('No or more than one root in interval [%g, %g]' % (a, b))
    
        n = 0
        
        if store is True: 
            info = []
        
        f_value = fa
        while abs(f_value) > epsilon and n <= max_iter:
            x = a - fa*(float(b-a)/(f(b)-fa))
            f_value = f(x)
            n += 1
            if store is True:
                info.append((x, f_value))
            
            if fa*f_value <= 0:
                b = x   # root is on the left part of secant
            else:
                a = x   # root in on the right part of secant
                fa = f_value
                
        expression = 'x0 found' if abs(f_value) < epsilon else 'x0 not found'
        
        if store is True:
            return x, info, expression
        else:
            return x, f_value, expression, n
            
class Bisection(Root):
    def solve(self, a, b, epsilon=1.0E-7, max_iter=100, store=False):
        f = self.f
        fa = f(a)
        
        if fa*f(b) > 0:
            raise ValueError('No or more than one root in interval [%g, %g]' % (a, b))
        
        n = 0

        if store is True: 
            info = []
        
        while b-a > epsilon and n <= max_iter:
            m = (a + b)/2.0
            fm = f(m)
            n += 1
            if store is True:
                info.append((m, fm))
                
            if fa*fm <= 0:
                b = m   # root is in the left half of [a,b]
            else:
                a = m   # root is in the right half of [a,b]
                fa = fm
        
        expression = 'x0 found' if b-a < epsilon else 'x0 not found'
        
        if store is True:
            return m, info, expression
        else:
            return m, fm, expression, n

__all__ = ['Diff', 'Root', 'Newton', 'Secant', 'Bisection']