# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 21:58:09 2015

@author: Georg
"""

from math import cos, factorial
from numpy import isclose

def cos_taylor_diff(x, N):
    n = 1
    an_prev = 1   ## initial condition a0
    cn_prev = 0   ## initial condition s0
    
    while n <= N:
        cn = cn_prev + an_prev
        an = -(x**2)/((2.0*n - 1)*2.0*n) * an_prev
        cn_prev = cn
        an_prev = an
        n += 1
    return cn, an

def test_cos_taylor_diff():
    """
    Test function for approxomation of cosine with difference
    function of taylor polynomial of N-th degree
    """
    x = 1.0
    N = 3
    
    c3 = 1 - (x**2)/factorial(2) + (x**4)/factorial(4)
    a3 = -(x**6)/factorial(6)
    
    polynom, err = cos_taylor_diff(x,N)
    
    success = isclose(c3, polynom) and isclose(a3, err)
    msg = "Difference equation failed."
    assert success, msg

def make_table(xlist, nlist):
    print "Result table for cosine approximation:"
    print "%s" % (66*'=')
    for x in xlist:
        exact = cos(x)
        for n in nlist:
            cn, an = cos_taylor_diff(x,n)
            print "x = %d   approx = %8.5f   exact = %8.5f   error = %8.5e"\
            % (int(x), cn, exact, abs(cn-exact))
        print "%s" % (66*'-')

test_cos_taylor_diff()
xlist = range(1,5)
nlist = [2**k for k in range(1,11)]
make_table(xlist, nlist)
