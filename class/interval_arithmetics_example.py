# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 18:01:28 2015

@author: Georg
"""

class IntervalMath:
    def __init__(self, lower, upper):
        self.lo = float(lower)
        self.up = float(upper)
        
    def __add__(self, other):
        if isinstance(other, (float, int)):
            other = IntervalMath(other, other)
        a, b, c, d = self.lo, self.up, other.lo, other.up
        return IntervalMath(a+c, b+d)

    def __radd__(self, other):
        if isinstance(other, (float, int)):
            other = IntervalMath(other, other)
        return other.__add__(self)

    def __sub__(self, other):
        if isinstance(other, (float, int)):
            other = IntervalMath(other, other)
        a, b, c, d = self.lo, self.up, other.lo, other.up
        return IntervalMath(a-d, b-c)

    def __rsub__(self, other):
        if isinstance(other, (float, int)):
            other = IntervalMath(other, other)
        return other.__sub__(self)

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            other = IntervalMath(other, other)
        a, b, c, d = self.lo, self.up, other.lo, other.up
        return IntervalMath(min(a*c, a*d, b*c, b*d), max(a*c, a*d, b*c, b*d))

    def __rmul__(self, other):
        if isinstance(other, (float, int)):
            other = IntervalMath(other, other)
        return other.__mul__(self)

    def __div__(self, other):
        if isinstance(other, (float, int)):
            other = IntervalMath(other, other)
        a, b, c, d = self.lo, self.up, other.lo, other.up
        if (c or d) <= 0:
            raise ValueError('interval cannot be denominator because it contains zero')
        return IntervalMath(min(a/c, a/d, b/c, b/d), max(a/c, a/d, b/c, b/d))

    def __rdiv__(self, other):
        if isinstance(other, (float, int)):
            other = IntervalMath(other, other)
        return other.__div__(self)

    def __pow__(self, exponent):
        if isinstance(exponent, int):
            p = 1
            if exponent > 0:
                for i in range(exponent):
                    p = p*self
            elif exponent < 0:
                for i in range(-exponent):
                    p = p*self
                p = 1/p
            else:
                p = IntervalMath(1, 1)
            return p
        else:
            raise TypeError('exponent must be an integer')
    
    def __float__(self):
        return (self.lo + self.up)/2.0
        
    def __repr__(self):
        return '%s(%g, %g)' % (self.__class__.__name__, self.lo, self.up)

    def __str__(self):
        return '[%g, %g]' % (self.lo, self.up)