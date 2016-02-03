# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 22:49:21 2015

@author: Georg
"""
from numpy import *
import sympy as sp

def _find_extrema(f, a, b, n):
    h = (b-a)/float(n)
    x = asarray([a+i*h for i in range(n+1)])
    y = f(x)
    P_min = []; P_max = []
    if y[0] < y[1]:
        P_min.append(x[0])
    elif y[0] > y[1]:
        P_max.append(x[0])
    for i in range(1, n):
        if y[i] < y[i-1] and y[i] < y[i+1]:
            P_min.append(x[i])
        elif y[i] > y[i-1] and y[i] > y[i+1]:
            P_max.append(x[i])
    if y[-1] < y[-2]:
        P_min.append(x[-1])
    elif y[-1] > y[-2]:
        P_max.append(x[-1])
        
    P_min = asarray(P_min); P_max = asarray(P_max)
    F_min = f(P_min); F_max = f(P_max)        
        
    return P_min, P_max, F_min, F_max 

def _refine_extrema(f, dxdy, a, b, n, eps):
    h = (b-a)/float(n)
    x = [a+i*h for i in range(n+1)]
    y = [f(i) for i in x]
    min_bounds = []; max_bounds = []
    for i in range(1, n):
        if y[i] < y[i-1] and y[i] < y[i+1]:
            min_bounds.append((x[i-1], x[i+1]))
        elif y[i] > y[i-1] and y[i] > y[i+1]:
            max_bounds.append((x[i-1], x[i+1]))
    
    P_min = []; P_max = []
    for (le, ri) in min_bounds:
        root = _bisection(dxdy, le, ri, eps)
        P_min.append(root)
    for (le, ri) in max_bounds:
        root = _bisection(dxdy, le, ri, eps)
        P_max.append(root)
    
    F_min = [f(i) for i in P_min]; F_max = [f(i) for i in P_max]
    P_min = asarray(P_min); P_max = asarray(P_max)
    F_min = asarray(F_min); F_max = asarray(F_max)     
        
    return P_min, P_max, F_min, F_max 

def _make_derivative(f_expr):
    x = sp.Symbol('x')
    f_expr = sp.sympify(f_expr)
    f = sp.lambdify([x], f_expr)
    dxdy_expr = sp.diff(f_expr)
    dxdy = sp.lambdify([x], dxdy_expr)
    
    return f, dxdy

def _bisection(f, l, r, eps):
    fl = f(l)
    if fl*f(r) > 0:
        return None
    
    i = 0   # iteration counter
    while (r-l) > eps:
        i += 1
        m = (l+r)/2.0
        fm = f(m)
        if fl*fm <= 0:
            r = m   # root is on the left half of [a,b]
        else:
            l = m   # root is on the right half of [a,b]
            fl = fm
    return m

class MinMax_v1:
    def __init__(self, func, left, right, n):
        if callable(func) and isinstance(left, (float, int)) and isinstance(right, (float, int)) \
        and isinstance(n, (float, int)):
            self.f = func
            self.a = float(left)
            self.b = float(right)
            self.n = int(n)
            
            self.P_min, self.P_max, self.F_min, self.F_max = _find_extrema(self.f, self.a, self.b, self.n)
        else:
            raise TypeError("""Argument 1 must be a function and arguments 2,3 and 4 
            must be float or integer numbers.""")
        
    def get_global_minimum(self):
        ix = argmin(self.F_min)
        return (self.P_min[ix], self.F_min[ix])
    
    def get_global_maximum(self):
        ix = argmax(self.F_max)
        return (self.P_max[ix], self.F_max[ix])
    
    def get_all_minima(self):
        all_x_min = self.P_min; all_y_min = self.F_min
        all_x_min = all_x_min.reshape((len(self.P_min),1))
        all_y_min = all_y_min.reshape((len(self.F_min),1))
        all_pairs_min = concatenate((all_x_min, all_y_min), axis=1)
        return all_pairs_min
    
    def get_all_maxima(self):
        all_x_max = self.P_max; all_y_max = self.F_max
        all_x_max = all_x_max.reshape((len(self.P_max),1))
        all_y_max = all_y_max.reshape((len(self.F_max),1))
        all_pairs_max = concatenate((all_x_max, all_y_max), axis=1)
        return all_pairs_max
    
    def __str__(self):
        s = ''
        s += 'All minima: '        
        for j in range(len(self.P_min)):
            s += '%.4f, ' % (self.P_min[j])
        s += '\nAll maxima: '
        for j in range(len(self.P_max)):
            s += '%.4f, ' % (self.P_max[j])
        s += '\nGlobal minimum: %.4f' % (self.P_min[argmin(self.F_min)])
        s += '\nGlobal maximum: %.4f' % (self.P_max[argmax(self.F_max)])
        return s

class MinMax_v2:
    def __init__(self, func_expr, left, right, n):
        if isinstance(func_expr, str) and isinstance(left, (float, int)) and isinstance(right, (float, int)) \
        and isinstance(n, (float, int)):
            self.a = float(left)
            self.b = float(right)
            self.n = int(n)
            
            self.eps = 1.0e-14
            
            self.f, self.dxdy = _make_derivative(func_expr)
            
            self.P_min, self.P_max, self.F_min, self.F_max = _refine_extrema(self.f, self.dxdy, self.a, self.b, self.n, self.eps)
        else:
            raise TypeError("""Argument 1 must be a function and arguments 2,3 and 4 
            must be float or integer numbers.""")
        
    def get_global_minimum(self):
        ix = argmin(self.F_min)
        return (self.P_min[ix], self.F_min[ix])
    
    def get_global_maximum(self):
        ix = argmax(self.F_max)
        return (self.P_max[ix], self.F_max[ix])
    
    def get_all_minima(self):
        all_x_min = self.P_min; all_y_min = self.F_min
        all_x_min = all_x_min.reshape((len(self.P_min),1))
        all_y_min = all_y_min.reshape((len(self.F_min),1))
        all_pairs_min = concatenate((all_x_min, all_y_min), axis=1)
        return all_pairs_min
    
    def get_all_maxima(self):
        all_x_max = self.P_max; all_y_max = self.F_max
        all_x_max = all_x_max.reshape((len(self.P_max),1))
        all_y_max = all_y_max.reshape((len(self.F_max),1))
        all_pairs_max = concatenate((all_x_max, all_y_max), axis=1)
        return all_pairs_max
    
    def __str__(self):
        s = ''
        s += 'All minima: '        
        for j in range(len(self.P_min)):
            s += '%.4f, ' % (self.P_min[j])
        s += '\nAll maxima: '
        for j in range(len(self.P_max)):
            s += '%.4f, ' % (self.P_max[j])
        s += '\nGlobal minimum: %.4f' % (self.P_min[argmin(self.F_min)])
        s += '\nGlobal maximum: %.4f' % (self.P_max[argmax(self.F_max)])
        return s

def test_MinMax_v1():
    def f(x):
        return x**2 - 1
    m = MinMax_v1(f, -1, 1, 100)
    eps = 0.02
    minimum = m.get_global_minimum()
    success = abs(minimum[0] - 0.0) <= eps
    if success:
        print 'Test successful!'
    assert success, 'Class MinMax_v1 failed! Found min = %g != 0.0' % (minimum[0])
    
def test_MinMax_v2():
    func_expr = 'x**2 -1'
    m = MinMax_v2(func_expr, -1, 1, 100)
    eps = 1.0e-5
    minimum = m.get_global_minimum()
    success = abs(minimum[0] - 0.0) <= eps
    if success:
        print 'Test successful!'
    assert success, 'Class MinMax_v2 failed! Found min = %g != 0.0' % (minimum[0])

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test_MinMax_v1':
        test_MinMax_v1()
    elif len(sys.argv) >= 2 and sys.argv[1] == 'test_MinMax_v2':
        test_MinMax_v2()

__all__ = ['_find_extrema', '_refine_extrema', '_make_derivative', '_bisection', 'test_MinMax_v1', 
           'test_MinMax_v2', 'MinMax_v1', 'MinMax_v2']