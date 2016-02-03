# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:25:23 2015

@author: Georg
"""

import sympy
import matplotlib.pyplot as plt
from numpy import *

###############################################################################
#####################    Function and class definitions   #####################
###############################################################################

def make_derivative(f_str):
    x          = sympy.Symbol('x')
    func_expr  = sympy.sympify(f_str)
    f          = sympy.lambdify(x, func_expr)
    deriv_expr = sympy.diff(func_expr)
    df         = sympy.lambdify(x, deriv_expr)
    return f, df

def make_integral(f_str):
    x          = sympy.Symbol('x')
    func_expr  = sympy.sympify(f_str)
    f          = sympy.lambdify(x, func_expr)
    int_expr   = sympy.integrate(func_expr)
    F          = sympy.lambdify(x, int_expr)
    return f, F
    
class ArcLength_v1:
    def __init__(self, f):
        if isinstance(f, str):
            self.f, self.df = make_derivative(f)
        else:
            raise TypeError('Function should be provided as string')
    
    def __call__(self, a, b, n):
        self.a = float(a)
        self.b = float(b)
        self.n = int(n)
        
        index_set = range(self.n+1)        
        x         = linspace(a,b,self.n+1)
        s         = zeros_like(x)
        g_        = zeros_like(x)
        g         = lambda x: sqrt(1+(self.df(x))**2)
        s[0]      = 0
        g_[0]     = g(x[0])        
        
        for k in index_set[1:]:
            g_[k] = g(x[k])
            if g_[k] == inf:
                raise ZeroDivisionError('Float division by zero')
            s[k]  = s[k-1] + 0.5*(x[k] - x[k-1])*(g_[k-1] + g_[k])
        return s

class ArcLength_v2:
    def __init__(self, f):
        if callable(f):
            self.f = f
        else:
            raise TypeError('Function is not callable')
            
    def Central(self, x):
        f = self.f
        h = 1.0E-8
        return (f(x+h) - f(x-h))/(2*h)
    
    def __call__(self, a, b, n):
        self.a = float(a)
        self.b = float(b)
        self.n = int(n)
        
        index_set = range(self.n+1)        
        x         = linspace(a,b,self.n+1)
        s         = zeros_like(x)
        g_        = zeros_like(x)
        g         = lambda x: sqrt(1+(self.Central(x))**2)
        s[0]      = 0
        g_[0]     = g(x[0])        
        
        for k in index_set[1:]:
            g_[k] = g(x[k])
            if isnan( g_[k]):
                raise ValueError('Differentiation does not yield number')
            s[k]  = s[k-1] + 0.5*(x[k] - x[k-1])*(g_[k-1] + g_[k])
        return s

class ArcLength_v3:
    def __init__(self, f):
        if callable(f):
            self.f = f
        else:
            raise TypeError('Function is not callable')
    
    def __call__(self, a, b, n):
        self.a = float(a)
        self.b = float(b)
        self.n = int(n)
        
        index_set = range(self.n+1)        
        x         = linspace(a,b,self.n+1)
        s         = zeros(self.n+1)
        df_       = zeros(self.n)
        s[0]      = 0       
        
        for k in index_set[1:]:
            df_[k-1] = (self.f(x[k]) - self.f(x[k-1]))/(x[k] - x[k-1])
            s[k]  = s[k-1] + sqrt(1+(df_[k-1])**2)*(x[k] - x[k-1])
        return s

###############################################################################
#####################    Test functions for semicircle    #####################
###############################################################################

semi_circle_str = 'sqrt(4-x**2)'
def semi_circle_func(x):
    return sqrt(4-x**2)
exact_value = 2*pi

class_list_1 = []
l1 = ArcLength_v1(semi_circle_str);  class_list_1.append(l1)
l2 = ArcLength_v2(semi_circle_func); class_list_1.append(l2)
l3 = ArcLength_v3(semi_circle_func); class_list_1.append(l3)

print 'Results for semicircle:'
for method in class_list_1:
    try:
        print 'Method %s: %g. Exact result: %g.' \
        % (method.__class__.__name__, method.__call__(-2,2,1000)[-1], exact_value) 
    except:
        print 'Method %s: cannot compute arc for given function.' \
        % (method.__class__.__name__)

###############################################################################
#####################    Test functions for semicircle    #####################
###############################################################################

func_expr = '1/sqrt(2*pi)*exp(-4*x**2)'
def func(x):
    return 1/sqrt(2*pi)*exp(-4*x**2)

class_list_2 = []
s1 = ArcLength_v1(func_expr); class_list_2.append(s1)
s2 = ArcLength_v2(func); class_list_2.append(s1)
s3 = ArcLength_v3(func); class_list_2.append(s1)

plt.plot(linspace(-2,2,1000), [func(x) for x in linspace(-2,2,1000)], 'k-', label='function')
plt.hold('on')
print '\nResults for function: ', func_expr
for method in class_list_2:
    try:
        arc = method.__call__(-2,2,1000)
        print 'Method %s: %g' % (method.__class__.__name__, arc[-1])
        plt.plot(linspace(-2,2,1001), arc, label='%s' % method.__class__.__name__)
        plt.hold('on')
    except:
        print 'Method %s: cannot compute arc for given function.' \
        % (method.__class__.__name__)
plt.legend(loc='best')