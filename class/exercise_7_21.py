# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 16:53:07 2015

@author: Georg
"""

from numpy import *
import matplotlib.pyplot as plt

class Piecewise:
    def __init__(self, arg, xmax):
        if isinstance(arg, list) and isinstance(xmax, (float, int)):
            self.bounds = arg
            self.xmax   = float(xmax)
        else:
            raise TypeError('Bounds must be given as list and xmax as float or integer number')
        
    def __call__(self, x):
        condition1 = logical_and(self.bounds[0][0] <= x, x < self.bounds[1][0])
        r = where(condition1, self.bounds[0][1], self.bounds[0][1])
        
        for ix in range(1, len(self.bounds)-1):
            condition2 = logical_and(self.bounds[ix][0] <= x, x < self.bounds[ix+1][0])
            r = where(condition2, self.bounds[ix][1], r)
        
        condition3 = logical_and(self.bounds[-1][0] <= x, x <= self.xmax)
        r = where(condition3, self.bounds[-1][1], r)
        
        return r
    
    def plot(self):
        x_v = [self.bounds[0][0]]
        for ix in range(1, len(self.bounds)):
            x_v += 2*[self.bounds[ix][0]]
        x_v += [self.xmax]
        
        y_v = []
        for ix in range(len(self.bounds)):
            y_v += 2*[self.bounds[ix][1]]
        
        plt.plot(x_v,y_v)
        plt.ylim(min(y_v)-0.1, max(y_v)+0.1)
        plt.xlabel('x')
        plt.ylabel('f(x)')