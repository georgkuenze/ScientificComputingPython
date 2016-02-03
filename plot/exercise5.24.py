# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 21:44:26 2015

@author: Georg
"""

from numpy import *
import matplotlib.pyplot as plt
import argparse
from scitools.StringFunction import StringFunction

# Get input data function
def get_input():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--f', '--function', type=str, default='0', help='function definition', metavar='f')
    parser.add_argument('--n', '--points', type=int, default=5, help='number of interpolation points', metavar='n')    
    parser.add_argument('--xmin', '--minimum', type=str, default='0', help='right border', metavar='xmin')
    parser.add_argument('--xmax', '--maximum', type=str, default='0', help='left border', metavar='xmax')
    parser.add_argument('--res', '--resolution', type=int, default=100, help='number of points plotted', metavar='res')

    
    args = parser.parse_args()
    
    try:
        f = StringFunction(args.f, independent_variable='x')
        n = args.n
        xmin = eval(args.xmin)
        xmax = eval(args.xmax)
        res = args.res

    except IndexError:
        raise IndexError("Not all arguments were provided on the command line.")
    except ValueError:
        raise ValueError("Test if you provided input data in the correct format.")
    
    return f, n, xmin, xmax, res

# Define Lagrange's polynomial interpolation formula
def p_L(x, xp, yp):
    Ls = zeros(xp.size, dtype='float64')
    p = 0
    
    for index, k in enumerate(xp):
        i = xp[where(xp!=k)]
        L = 1
        for j in xrange(len(i)):
            L *= ((x - i[j])/(float(k) - i[j]))
        Ls[index] = L
            
    for j,l in zip(yp, Ls):
        p += j*l
    
    return p

# Define plotting function
def graph(f, n, xmin, xmax, resolution=1001):
    f.vectorize(globals())    
    xp = linspace(xmin, xmax, n)
    yp = f(xp)
    
    x = linspace(xmin, xmax, resolution)
    y = zeros(x.size, dtype='float64')
    for ix in xrange(len(x)):
        y[ix] = p_L(x[ix], xp, yp)
    
    return x, y, xp, yp

f, n, xmin, xmax, res = get_input()
x, y, xp, yp = graph(f, n, xmin, xmax, resolution=res)

plt.plot(xp, yp, 'ro', label='input points')
plt.hold('on')
plt.plot(x, y, 'b-', label='interpolation')
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(x.min(), x.max())
plt.legend(loc='best')