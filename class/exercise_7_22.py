# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:12:53 2015

@author: Georg
"""
from numpy import *
import matplotlib.pyplot as plt

class Integral:
    def __init__(self, f, a, n):
        if callable(f) and isinstance(a, (float, int)) and isinstance(n, (float, int)):
            self.f = f
            self.a = float(a)
            self.n = float(n)
        else:
            raise TypeError('Function must be callable and integral limits must be float or integer numbers.')

    def trapezoidal_v1(self, x):
        h = (x - self.a)/self.n
        I = 0.5*self.f(self.a)*h
        for i in range(1, int(self.n)):
            I += (self.f(self.a+i*h)*h)
        I += 0.5*self.f(x)*h
        return I
    
    def trapezoidal_v2(self, x):
        x = linspace(self.a, x, self.n+1)
        f_ = zeros_like(x)
        I = zeros_like(x)
        f_[0] = self.f(x[0])
        I[0] = 0
        for i in range(1, int(self.n)+1):
            f_[i] = self.f(x[i])
            I[i] = I[i-1] + 0.5*(x[i] - x[i-1])*(f_[i-1] + f_[i])
        return x, I