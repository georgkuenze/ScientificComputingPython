# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 13:51:05 2015

@author: Georg
"""
from math import factorial, sin
from numpy import isclose

def sin_taylor_diff(x, N):
    n = 1
    an_prev = x   ## initial condition a0
    sn_prev = 0   ## initial condition s0
    
    while n <= N:
        sn = sn_prev + an_prev
        an = -(x**2)/((2.0*n + 1)*2.0*n) * an_prev
        sn_prev = sn
        an_prev = an
        n += 1
    return sn, an

def test_sin_taylor_diff():
    """
    Test function for approxomation of sine with difference
    function of taylor polynomial of N-th degree
    """
    x = 1.0
    N = 3
    
    s3 = x - (x**3)/factorial(3) + (x**5)/factorial(5)
    a3 = -(x**7)/factorial(7)
    
    polynom, err = sin_taylor_diff(x,N)
    
    success = isclose(s3, polynom) and isclose(a3, err)
    msg = "Difference equation failed."
    assert success, msg

def make_table(xlist, nlist):
    print "Result table for sine approximation:"
    print "%s" % (66*'=')
    for x in xlist:
        exact = sin(x)
        for n in nlist:
            sn, an = sin_taylor_diff(x,n)
            print "x = %d   approx = %8.5f   exact = %8.5f   error = %8.5e"\
            % (int(x), sn, exact, abs(sn-exact))
        print "%s" % (66*'-')

test_sin_taylor_diff()
xlist = range(1,5)
nlist = [2**k for k in range(1,11)]
make_table(xlist, nlist)