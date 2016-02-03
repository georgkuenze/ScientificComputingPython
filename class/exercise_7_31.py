# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 22:07:27 2015

@author: Georg
"""

from numpy import *

class Vec:
    def __init__(self, *args):
        if len(args) == 1:
            self.v = asarray(args[0], dtype='float64')
        elif len(args) > 1:
            self.v = array(args, dtype='float64')
    
    def __add__(self, other):
        if isinstance(other, (list, tuple, ndarray)):
            other = Vec(other)
        return Vec(self.v + other.v)
    
    def __radd__(self, other):
        if isinstance(other, (list, tuple, ndarray)):
            other = Vec(other)
        return other.__add__(self)
    
    def __sub__(self, other):
        if isinstance(other, (list, tuple, ndarray)):
            other = Vec(other)
        return Vec(self.v - other.v)
    
    def __rsub__(self, other):
        if isinstance(other, (list, tuple, ndarray)):
            other = Vec(other)
        return other.__sub__(self)
        
    def __mul__(self, other):
        if isinstance(other, (list, tuple, ndarray)):
            other = Vec(other)
        return Vec(self.v*other.v)
    
    def __rmul__(self, other):
        if isinstance(other, (list, tuple, ndarray)):
            other = Vec(other)
        return other.__mul__(self)
    
    def __div__(self, other):
        if isinstance(other, (list, tuple, ndarray)):
            other = Vec(other)
        return Vec(self.v/other.v)
    
    def __rdiv__(self, other):
        if isinstance(other, (list, tuple, ndarray)):
            other = Vec(other)
        return other.__div__(self)
        
    def __abs__(self):
        return sqrt(sum(dot(self.v, self.v)))
    
    def __eq__(self, other):
        if isinstance(other, (list, tuple, ndarray)):
            other = Vec(other)
        return allclose(self.v, other.v)
    
    def __ne__(self, other):
        if isinstance(other, (list, tuple, ndarray)):
            other = Vec(other)
        return not allclose(self.v, other.v)

    def __str__(self):
        s = '['
        for i in range(len(self.v)):
            s += str(self.v[i]) + ', '
        s += ']'
        s = s.replace(', ]', ']')
        return s
    
    def __repr__(self):
        return 'Vec(%s)' % self.__str__()