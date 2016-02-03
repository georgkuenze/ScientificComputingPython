# -*- coding: utf-8 -*-
"""
Created on Wed Sep 02 10:52:59 2015

@author: Georg
"""

from differentiation import *
from integration import *
from roots import *
from MinMax import *
import numpy as np
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
        plt.ylabel('df(x)')
        
    def plot_inverse(self):
        y, x = self.make_inverse()
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('g(x)')
        
    def make_inverse(self):
        f, a, b, n_points = self.f, self.a, self.b, self.res
        
        if a*b < 0:
            raise ValueError('Cannot compute inverse function because interval includes zero.')
        else:
            if a == 0:
                a += 0.01
            elif b == 0:
                b -= 0.01
                
        m  = MinMax_v1(f, a, b, n_points)
        mi = np.asarray(m.get_all_minima())
        mi = list(mi[:,0])
        ma = np.asarray(m.get_all_maxima())
        ma = list(ma[:,0])
        intervals = sorted(mi+ma)
        intervals = sorted(intervals+intervals[1:-1])
        
        for i in range(1, len(intervals)-1):
            if i % 2 != 0:
                intervals[i] -= 0.01
            else:
                intervals[i] += 0.01        
        
        F = lambda gamma: f(gamma) - xi    
        g = []
        x_all = []
        for k in range(0, len(intervals), 2):
            l, r = intervals[k], intervals[k+1]
            x = [(r-l)/float(n_points)*i + l for i in range(int(n_points)+1)]
            
            for i in range(len(x)):
                xi = x[i]
                
                if i == 0:
                    gamma0 = x[0]
                else:
                    gamma0 = g[i-1]
        
                n = Newton(F, dfdx='Numeric')
                gamma, F_value, expression, n = n.solve(gamma0, epsilon=1.0E-7, max_iter=100, store=False)
                g.append(gamma)
            x_all += x
        return g, x_all
        
        
    def extreme_points(self):
        f, a, b, res = self.f, self.a, self.b, self.res
        m = MinMax_v3(f, a, b, res)
        print m
    
    def inverse(self, x):
        f = self.f
        F = lambda gamma: f(gamma) - x
        n = Newton(F, dfdx='Numeric')
        gamma, F_value, expression, n = n.solve(x, epsilon=1.0E-7, max_iter=100, store=False)
        return gamma
    
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