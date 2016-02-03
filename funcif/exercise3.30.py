# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 12:11:16 2015

@author: Georg
"""
# Approximation of log(1+x) by sum (1.0/i)*(x/(1+x))**i
def L3(x, eps=1.0e-6):
    x = float(x)
    i = 1
    term = (1.0/i)*(x/(1+x))**i
    s = term
    while abs(term) > eps:
        i += 1
        term = (1.0/i)*(x/(1+x))**i
        s += term
    return s, i

def L3_ci(x, eps=1.0e-6):
    x = float(x)
    i = 1.
    term = (1.0/i)*(x/(1+x))**i
    s = term
    while abs(term) > eps:
        i += 1
        term = (((i-1)/float(i))*(x/(1+x)))*term
        s += term
    return s, i

def table_L3(x):
    from math import log
    for k in range (4,14,2):
        eps = 10**(-k)
        approx, n = L3(x, eps=eps)
        exact = log(1+x)
        error = abs(exact - approx)
        print "tolerance = %.e; exact error = %.4e; n = %3d" % (eps, error, n)
        
def table_L3_ci(x):
    from math import log
    for k in range (4,14,2):
        eps = 10**(-k)
        approx, n = L3_ci(x, eps=eps)
        exact = log(1+x)
        error = abs(exact - approx)
        print "tolerance = %.e; exact error = %.4e; n = %3d" % (eps, error, n)

def test_L3_ci():
    x = 10
    result1 = L3(x)
    result2 = L3_ci(x)
    success = abs(result1[0] - result2[0]) < 1.0e-14
    if success:
        print "Both functions are equal within machine epsilon!"
    msg = "%s gives different result than %s" % (L3.__name__, L3_ci.__name__)
    assert success, msg

print "Approximation log(1+x) by sum -- version one:\n"
table_L3(10)
print "\nApproximation log(1+x) by sum -- version two:\n"
table_L3_ci(10)
print "\nEquivalence test:"
test_L3_ci()