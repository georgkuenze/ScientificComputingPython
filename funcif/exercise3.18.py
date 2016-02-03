# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 00:25:22 2015

@author: Georg
"""

import numpy as np

def diff(f, x, h=1e-10):
    dydx = (f(x+h) - f(x-h))/(2*h)
    return dydx

def test_diff():
    x = 2
    eps = 1e-6
    y = lambda x: x**2 + x + 1
    dydx = lambda x: 2*x + 1
    exact = dydx(x)
    approx = diff(y, x)
    success = abs(exact - approx) < eps
    if success is True:
        print "Differentiation is exact within limit %g" % (eps)
    msg = 'Differentiation is not exact'
    assert success, msg

print "Differentiation test:"
test_diff()

def application():
    functions = [lambda x: np.exp(x), lambda x: np.exp(-2*x**2), lambda x: np.cos(x), lambda x: np.log(x)]
    derivatives = [lambda x: np.exp(x), lambda x: -4*x*np.exp(-2*x**2), lambda x: -1*np.sin(x), lambda x: 1./x]
    names =['exp(x)', 'exp(-2*x**2)', 'cos(x)', 'log(x)']
    x = [0, 0, 2*np.pi, 1.]
    h = 0.01
    for i, name in zip(range(len(x)), names):
        exact = derivatives[i](x[i])
        approx = diff(functions[i], x[i], h)
        error = abs(exact - approx)
        print "Function: %12s; Exact result: %.4e; approximation: %.4e; error: %.4e" % (name, exact, approx, error)

print "\nDifferentiation application test:"
application()