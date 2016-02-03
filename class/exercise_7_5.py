# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 10:08:35 2015

@author: Georg
"""
from math import sqrt

class Quadratic:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
    
    def __call__(self, x):
        self.x = x
        return self.a*self.x**2 + self.b*self.x + self.c
    
    def table(self, left, right, n=100):
        self.L = float(left)
        self.R = float(right)
        print '    x         y    \n--------- ---------'
        for x in [((self.R-self.L)/float(n))*i + self.L for i in range(n+1)]:
            y = self.__call__(x)
            print '%9.2f %9.2f' % (x, y)
            
    def roots(self):
        if (self.b**2) <= (4*self.a*self.c):
            raise ValueError('Function has no roots.')
        else:
            y_1 = (-self.b - sqrt(self.b**2 - 4*self.a*self.c))/(2*self.a)
            y_2 = (-self.b + sqrt(self.b**2 - 4*self.a*self.c))/(2*self.a)
        return (y_1, y_2)