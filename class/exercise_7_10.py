# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 22:49:00 2015

@author: Georg
"""
from numpy import *
import matplotlib.pyplot as plt

class Sum:
    def __init__(self, arg1, arg2, arg3):
        if callable(arg1) and isinstance(arg2, (float, int)) and isinstance(arg3, (float, int)):
            self.term = arg1
            self.M    = int(arg2)
            self.N    = int(arg3)
        else:
            raise TypeError('Arg1 must be function; Arg2 and Arg3 must be float or integer numbers')
    
    def __call__(self, x):      
        Summe = 0
        for k in range(self.M, self.N+1):
            Summe += self.term(x, k)
        return Summe
    
    def plot(self, left, right, n=100):
        self.L = left
        self.R = right
        xp = linspace(self.L, self.R, n)
        yp = zeros(n, dtype='float64')
        for i in xrange(len(xp)):
            yp[i] = self.__call__(xp[i])
        
        plt.plot(xp, yp)
        plt.xlim(self.L, self.R)
        plt.grid()
        plt.xlabel('x')
        plt.ylabel('f(x)')