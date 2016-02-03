# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:34:54 2015

@author: Georg
"""

class Line:
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1
    
    def __call__(self, x):
        return self.c0 + self.c1*x
    
    def table(self, L, R, n):
        """Return a table with n points in interval [L,R]"""
        s = ''
        import numpy as np
        for x in np.linspace(L,R,n):
            y = self(x)
            s += '%12.3f %12.3f\n' % (x, y)
        print s

class Parabola(Line):
    def __init__(self, c0, c1, c2):
        Line.__init__(self, c0, c1)
        self.c2 = c2
    
    def __call__(self, x):
        return Line.__call__(self, x) + self.c2*x**2

class Cubic(Parabola):
    def __init__(self, c0, c1, c2, c3):
        Parabola.__init__(self, c0, c1, c2)
        self.c3 = c3
    
    def __call__(self, x):
        return Parabola.__call__(self, x) + self.c3*x**3

class Poly4(Cubic):
    def __init__(self, c0, c1, c2, c3, c4):
        Cubic.__init__(self, c0, c1, c2, c3)
        self.c4 = c4
    
    def __call__(self, x):
        return Cubic.__call__(self, x) + self.c4*x**4

class Sine(Parabola):
    def __init__(self, c, b, a, w, A):
        Parabola.__init__(self, c, b, a)
        self.w = w
        self.A = A
    
    def __call__(self, x):
        from math import sin        
        return Parabola.__call__(self, x) + self.A*sin(self.w*x)

__all__ = ['Line', 'Parabola', 'Cubic', 'Poly4', 'Sine']