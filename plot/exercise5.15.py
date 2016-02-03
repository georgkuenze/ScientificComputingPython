# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 09:56:10 2015

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
    parser.add_argument('--a', '--right', type=str, default='0.0', help='right border', metavar='a')
    parser.add_argument('--b', '--left', type=str, default='0.0', help='left border', metavar='b')
    parser.add_argument('--n', '--points', type=int, default=100, help='number of points', metavar='n')
    
    args = parser.parse_args()
    
    try:
        f = StringFunction(args.f, independent_variable='x')
        a = eval(args.a)
        b = eval(args.b)
        n = args.n
    except IndexError:
        raise IndexError("Not all arguments were provided on the command line.")
    except ValueError:
        raise ValueError("Test if you provided input data in the correct format.")
    
    return f, a, b, n

f, a, b, n = get_input()

# Vectorize function
f.vectorize(globals())
x = linspace(a, b, n)
y = f(x)

plt.plot(x, y, 'k.')
plt.xlabel('x')
plt.ylabel('y')

savetxt('xy_out.txt', transpose([x,y]), delimiter='\t', fmt='%.4f', header='List of x-y values')