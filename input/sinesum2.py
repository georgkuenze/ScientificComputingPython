# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 15:27:30 2015

@author: Georg
"""
def f(t, T):
    if t < 0.5*T:
        return 1
    elif t == 0.5*T:
        return 0
    else:
        return -1

def S(t, n, T):
    from math import *
    summe = 0    
    for i in range(1, n+1):
        summe += 4/pi*(1/(2.*i-1))*sin((2*(2*i-1)*pi*t)/float(T))
    return summe

def table(n, T, alpha):
    print "Approximation of Sigma function with Fourier Series\n%s" % ('-'*51)
    print "alpha      n   Exact Val.   Approx. Val.      Error"    
    for a in alpha:
        t = a * T
        exact = f(t, T)
        for i in n:
            approx = S(t, i, T)
            diff = abs(exact - approx)
            print "%5.2f   %4d   %10.3f   %12.3f   %7.2e" % (a, i, exact, approx, diff)

def get_input():
    import argparse
    from math import *
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--T', type=str, default='0', help='Turning point Sigma function')
    parser.add_argument('--alpha', type=float, default=0.0, help='Alpha value', nargs='+')
    parser.add_argument('--n', type=int, default=0 , help='List of points', nargs='+')
    args = parser.parse_args()
    
    T = eval(args.T)
    alpha = args.alpha
    n = args.n
    return n, T, alpha
 
if __name__ == '__main__':
    n, T, alpha = get_input()
    table(n, T, alpha)

__all__ = ['get_input', 'table', 'f', 'S']