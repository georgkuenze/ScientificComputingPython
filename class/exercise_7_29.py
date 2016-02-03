# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 21:14:39 2015

@author: Georg
"""
from numpy import allclose
from math import sqrt

class Vec2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        if isinstance(other, (list, tuple)):
            other = Vec2D(other[0], other[1])
        elif not hasattr(other, 'x') and hasattr(other, 'y'):
            raise TypeError('Instance vector must have x and y value.')
        return Vec2D(self.x + other.x, self.y + other.y)
    
    def __radd__(self, other):
        if isinstance(other, (list, tuple)):
            other = Vec2D(other[0], other[1])
        elif not hasattr(other, 'x') and hasattr(other, 'y'):
            raise TypeError('Instance vector must have x and y value.')
        return other.__add__(self)
    
    def __sub__(self, other):
        if isinstance(other, (list, tuple)):
            other = Vec2D(other[0], other[1])
        elif not hasattr(other, 'x') and hasattr(other, 'y'):
            raise TypeError('Instance vector must have x and y value.')
        return Vec2D(self.x - other.x, self.y - other.y)
    
    def __rsub__(self, other):
        if isinstance(other, (list, tuple)):
            other = Vec2D(other[0], other[1])
        elif not hasattr(other, 'x') and hasattr(other, 'y'):
            raise TypeError('Instance vector must have x and y value.')
        return other.__sub__(self)
        
    def __mul__(self, other): # Scalar product
        if isinstance(other, (list, tuple)):
            other = Vec2D(other[0], other[1])
        elif not hasattr(other, 'x') and hasattr(other, 'y'):
            raise TypeError('Instance vector must have x and y value.')
        return self.x*other.x + self.y*other.y
    
    def __rmul__(self, other):
        if isinstance(other, (list, tuple)):
            other = Vec2D(other[0], other[1])
        elif not hasattr(other, 'x') and hasattr(other, 'y'):
            raise TypeError('Instance vector must have x and y value.')
        return other.__mul__(self)
        
    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)
        
    def __eq__(self, other):
        if isinstance(other, (list, tuple)):
            other = Vec2D(other[0], other[1])
        elif not hasattr(other, 'x') and hasattr(other, 'y'):
            raise TypeError('Instance vector must have x and y value.')
        return allclose(self.x, other.x) and allclose(self.y, other.y)
    
    def __ne__(self, other):
        if isinstance(other, (list, tuple)):
            other = Vec2D(other[0], other[1])
        elif not hasattr(other, 'x') and hasattr(other, 'y'):
            raise TypeError('Instance vector must have x and y value.')
        return not self.__eq__(other)
    
    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)
    
    def __repr__(self):
        return 'Vec2D(x=%s, y=%s)' % (self.x, self.y)