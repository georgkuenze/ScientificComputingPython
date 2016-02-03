# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 23:19:43 2015

@author: Georg
"""

from exercise_7_23 import Polynomial
from math import factorial
from numpy import *
import argparse

def get_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=0.0, help='value of polynomial', metavar='x')
    parser.add_argument('--N', type=str, default='0.0', help='degree of polynomial', metavar='N')
    
    args = parser.parse_args()
        
    if None not in vars(args):
        try:
            x = args.x
            N = list(eval(args.N))
        except:
            raise TypeError('Provide x-value as float number and degree of polynomial as list.')
    else:
        raise IndexError('You provided less or more than two input parameter.')
    return x, N

def taylor_coeff(n):
    coefficients = zeros(n)
    for k in range(n):
        coefficients[k] = 1.0/factorial(k)
    return coefficients

x, N = get_input()

for element in N:
    p = Polynomial(taylor_coeff(element))
    print 'N = %2d; Polynomial(x) = %9.3f; exp(x) = %9.3f' % (element, p(x), exp(x))