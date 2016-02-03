# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 21:45:03 2015

@author: Georg
"""

from numpy import allclose
from math import sqrt

class Vec3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self, other):
        if isinstance(other, (list, tuple)):
            other = Vec3D(other[0], other[1], other[2])
        elif not hasattr(other, 'x') and hasattr(other, 'y') and hasattr(other, 'z'):
            raise TypeError('Instance vector must have x, y and z value.')
        return Vec3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __radd__(self, other):
        if isinstance(other, (list, tuple)):
            other = Vec3D(other[0], other[1], other[2])
        elif not hasattr(other, 'x') and hasattr(other, 'y') and hasattr(other, 'z'):
            raise TypeError('Instance vector must have x, y and z value.')
        return other.__add__(self)
    
    def __sub__(self, other):
        if isinstance(other, (list, tuple)):
            other = Vec3D(other[0], other[1], other[2])
        elif not hasattr(other, 'x') and hasattr(other, 'y') and hasattr(other, 'z'):
            raise TypeError('Instance vector must have x, y and z value.')
        return Vec3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __rsub__(self, other):
        if isinstance(other, (list, tuple)):
            other = Vec3D(other[0], other[1], other[2])
        elif not hasattr(other, 'x') and hasattr(other, 'y') and hasattr(other, 'z'):
            raise TypeError('Instance vector must have x, y and z value.')
        return other.__sub__(self)
        
    def __mul__(self, other): # Scalar product
        if isinstance(other, (list, tuple)):
            other = Vec3D(other[0], other[1], other[2])
        elif not hasattr(other, 'x') and hasattr(other, 'y') and hasattr(other, 'z'):
            raise TypeError('Instance vector must have x, y and z value.')
        return self.x*other.x + self.y*other.y + self.z*other.z
    
    def __rmul__(self, other):
        if isinstance(other, (list, tuple)):
            other = Vec3D(other[0], other[1], other[2])
        elif not hasattr(other, 'x') and hasattr(other, 'y') and hasattr(other, 'z'):
            raise TypeError('Instance vector must have x, y and z value.')
        return other.__mul__(self)
    
    def cross(self, other): # Cross product
        if isinstance(other, (list, tuple)):
            other = Vec3D(other[0], other[1], other[2])
        elif not hasattr(other, 'x') and hasattr(other, 'y') and hasattr(other, 'z'):
            raise TypeError('Instance vector must have x, y and z value.')
        return Vec3D(self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z, self.x*other.y - self.y*other.x)
    
    def __abs__(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)
        
    def __eq__(self, other):
        if isinstance(other, (list, tuple)):
            other = Vec3D(other[0], other[1], other[2])
        elif not hasattr(other, 'x') and hasattr(other, 'y') and hasattr(other, 'z'):
            raise TypeError('Instance vector must have x, y and z value.')
        return allclose(self.x, other.x) and allclose(self.y, other.y) and allclose(self.z, other.z)
    
    def __ne__(self, other):
        if isinstance(other, (list, tuple)):
            other = Vec3D(other[0], other[1], other[2])
        elif not hasattr(other, 'x') and hasattr(other, 'y') and hasattr(other, 'z'):
            raise TypeError('Instance vector must have x, y and z value.')
        return not self.__eq__(other)
    
    def __str__(self):
        return '(%g, %g, %g)' % (self.x, self.y, self.z)
    
    def __repr__(self):
        return 'Vec3D(x=%s, y=%s, z=%s)' % (self.x, self.y, self.z)