# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:08:33 2015

@author: Georg
"""
from numpy import allclose
from math import sqrt

class Vec2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vec2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return self.x*other.x + self.y*other.y
    
    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)
        
    def __eq__(self, other):
        return allclose(self.x, other.x) and allclose(self.y, other.y)
    
    def __ne__(self, other):
        return not self.__eq__(other)
        
    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)
    
    def __repr__(self):
        return 'Vec2D(x=%s, y=%s)' % (self.x, self.y)