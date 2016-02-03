# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 22:59:31 2015

@author: Georg
"""

from math import sqrt

class Complex():
    counter = 0
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag
        Complex.counter += 1
    
    def __add__(self, other):
        if isinstance(other, (float, int)):
            other = Complex(other)
        elif not (hasattr(other, 'real') and hasattr(other, 'imag')):
            raise TypeError('other must have real and imaginary attributes')
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __radd__(self, other):
        if isinstance(other, (float, int)):
            other = Complex(other)
        return other.__add__(self)
        
    def __sub__(self, other):
        if isinstance(other, (float, int)):
            other = Complex(other)
        elif not (hasattr(other, 'real') and hasattr(other, 'imag')):
            raise TypeError('other must have real and imaginary attributes')
        return Complex(self.real - other.real, self.imag - other.imag)
    
    def __rsub__(self, other):
        if isinstance(other, (float, int)):
            other = Complex(other)
        return other.__sub__(self)
        
    def __mul__(self, other):
        if isinstance(other, (float, int)):
            other = Complex(other)
        elif not (hasattr(other, 'real') and hasattr(other, 'imag')):
            raise TypeError('other must have real and imaginary attributes')
        return Complex(self.real*other.real - self.imag*other.imag,
                       self.imag*other.real + self.real*other.imag)
    
    def __rmul__(self, other):
        if isinstance(other, (float, int)):
            other = Complex(other)
        return other.__mul__(self)
    
    def __div__(self, other):
        if isinstance(other, (float, int)):
            other = Complex(other)
        elif not (hasattr(other, 'real') and hasattr(other, 'imag')):
            raise TypeError('other must have real and imaginary attributes')
        return Complex((self.real*other.real + self.imag*other.imag)/float(other.real**2 + other.imag**2),
                       (self.real*other.imag - self.imag*other.real)/float(other.real**2 + other.imag**2))
    
    def __rdiv__(self, other):
        if isinstance(other, (float, int)):
            other = Complex(other)
        return other.__div__(self)
    
    def __abs__(self):
        return sqrt(self.real**2 + self.imag**2)
        
    def __neg__(self):
        return Complex(-self.real, -self.imag)
    
    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __str__(self):
        return '(%g, %g)' % (self.real, self.imag)
    
    def __repr__(self):
        return 'Complex(%s, %s)' % (self.real, self.imag)
    
    def __pow__(self, power):
        raise NotImplementedError('self**power is not yet implemented for Complex')