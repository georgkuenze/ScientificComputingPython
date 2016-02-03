# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 17:50:00 2015

@author: Georg
"""
from numpy import *
import matplotlib.pyplot as plt

class LagrangeInterpolation:
    # Constructor method
    def __init__(self, xp, yp):
        if isinstance(xp, (tuple, list, ndarray)) and isinstance(yp, (tuple, list, ndarray)):
            self.xp = array(list(xp))
            self.yp = array(list(yp))
        else:
            raise TypeError('Points must be provided as tuple or list')
        
    # Define Lagrange's polynomial interpolation formula
    def __call__(self, x):
        Ls = zeros(self.xp.size, dtype='float64')
        p = 0
        
        for index, k in enumerate(self.xp):
            i = self.xp[where(self.xp!=k)]
            L = 1
            for j in xrange(len(i)):
                L *= ((x - i[j])/(float(k) - i[j]))
            Ls[index] = L
                
        for j,l in zip(self.yp, Ls):
            p += j*l
                
        return p
    
    # Method to plot graph of Lagrange polynomial
    def plot(self, left, right, n=100):
        x = linspace(left, right, n)
        y = zeros(x.size, dtype='float64')
        for ix in xrange(len(x)):
            y[ix] = self.__call__(x[ix])
        plt.plot(x, y)
        plt.hold('on')
        plt.plot(self.xp, self.yp, 'ro')
        plt.grid()
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.xlim(x.min(), x.max())
    
    # Define test function i.e. test yp identity
    def test(self, eps=1.0e-16):
        if all([abs(self.yp[i] - self.__call__(self.xp[i])) < eps for i in range(len(self.xp))]):
            print "Lagrange's interpolation at knot points correct."
        else:
            print "Lagrange's interpolation at knot points not correct."