# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 13:12:32 2015

@author: Georg
"""

import sympy

class Derivative:
    def __init__(self, arg, h=1E-5):
        if callable(arg) and isinstance(h, (float, int)):
            self.f = arg
            self.h = float(h)
        elif str(type(arg)).startswith('sympy', 8):
            self.f_expr    = arg
            x = sympy.Symbol('x')
            self.dxdy_expr = sympy.diff(self.f_expr, x)
            self.dxdy      = sympy.lambdify([x], self.dxdy_expr)
        else:
            raise TypeError('Argument 1 must be either a function or a symbolic expression')
    
    def __call__(self, x):
        if hasattr(self, 'f') and hasattr(self, 'h'):
            return (self.f(x+self.h) - self.f(x))/self.h
        elif hasattr(self, 'dxdy'):
            return self.dxdy(x)
    
    def __str__(self):
        if hasattr(self, 'dxdy'):    
            return 'Symbolic derivative of %s is %s.' % (self.f_expr, self.dxdy_expr)
        else:
            raise TypeError('Instance has to be created with function as sympy expression.')