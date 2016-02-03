# -*- coding: utf-8 -*-
"""
Created on Wed Sep 02 10:52:59 2015

@author: Georg
"""

from numpy import *
from differentiation import *
from integration import *
from MinMax import *
import sympy as sp
import matplotlib.pyplot as plt

class CalculusCalculator:
    def __init__(self, f, a, b, resolution=700):
        if callable(f) and isinstance(a, (float, int)) and isinstance(b, (float, int)) \
        and isinstance(resolution, int):
            self.f, self.a, self.b, self.res = f, float(a), float(b), float(resolution)
        else:
            raise TypeError('Function must be callable; bounds and resolution must be float or integer.')
        
        self.diff_method = Central2
        self.int_method  = Trapezoidal
        
    def plot(self):
        f, a, b, res = self.f, self.a, self.b, self.res
        x = [((b-a)/res)*i + a for i in range(int(res)+1)]
        y = [f(i) for i in x]
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('f(x)')        
        
    def plot_derivative(self):
        f, a, b, res, diff_method = self.f, self.a, self.b, self.res, self.diff_method
        dydx = diff_method(f, h=1.0E-6)
        x = [((b-a)/res)*i + a for i in range(int(res)+1)]
        dy = [dydx(i) for i in x]
        plt.plot(x, dy)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        
    def extreme_points(self):
        f, a, b, res = self.f, self.a, self.b, self.res
        m = MinMax_v3(f, a, b, res)
        print m        
        
    def derivative(self, x):
        f, diff_method = self.f, self.diff_method
        dydx = diff_method(f, h=1.0E-06)
        return dydx(x)
        
    def set_differentiation_method(self, method):
        self.diff_method = method
    
    def integral(self, l, r, points=1000):
        f, int_method = self.f, self.int_method
        I = int_method(l, r, points)
        return I.integrate(f)
        
    def set_integration_method(self, method):
        self.int_method = method