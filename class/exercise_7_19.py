# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 15:36:52 2015

@author: Georg
"""

from numpy import *
import matplotlib.pyplot as plt

class Heaviside:
    def __init__(self, eps=None):
        if isinstance(eps, (float, int)):        
            self.eps = float(eps)
    
    def __call__(self, x):
        if hasattr(self, 'eps') is False:
            condition1 = x < 0
            condition2 = x >= 0
            r = where(condition1, 0.0, 0.0)
            r = where(condition2, 1.0, 0.0)
            return r
        
        elif hasattr(self, 'eps') is True:
            condition1 = x < -self.eps
            condition2 = logical_and(-self.eps <= x, x <= self.eps)
            condition3 = x > self.eps
            r = where(condition1, 0.0, 0.0)
            r = where(condition2, 0.5+(x/(2.0*self.eps))+(1.0/(2*pi))*sin((pi*x)/self.eps), r)
            r = where(condition3, 1.0, r)
            return r
    
    def plot(self, xmin, xmax):
        if hasattr(self, 'eps') is False:
            plt.plot([xmin, 0, 0, xmax], [0, 0, 1, 1])
            plt.ylim(-0.1, 1.1)
            plt.xlabel('x')
            plt.ylabel('f(x)')
        elif hasattr(self, 'eps') is True:
            x_left = linspace(xmin, -self.eps, 10)
            x_dense = linspace(-self.eps, self.eps, 201/self.eps)
            x_right = linspace(self.eps, xmax, 10)
            x = concatenate((x_left, x_dense, x_right), axis=1)
            y = self.__call__(x)
            plt.plot(x, y)
            plt.ylim(-0.1, 1.1)
            plt.xlabel('x')
            plt.ylabel('f(x)')