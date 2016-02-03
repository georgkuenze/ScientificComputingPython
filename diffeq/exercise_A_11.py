# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 21:28:39 2015

@author: Georg
"""
import argparse, sys
from scitools.StringFunction import StringFunction
from math import *

###############################################################################
#####################  Define functions for root finding  #####################
###############################################################################

def Newton(f, x, dfdx='numeric', eps=1.0E-8, N=100, store=False):
    if dfdx == 'numeric':
        df = lambda x: (f(x+h) - f(x-h))/(2*1.0E-8)
    elif callable(dfdx):
        df = dfdx
    
    f_value = f(x)
    n = 0
    
    if store: info = [(x, f_value)]
    
    while abs(f_value) > eps and n <= N:
        df_value = float(df(x))
        if abs(df_value) < 1.0E-14:
            raise ValueError("Newton: f'(%g)=%g" % (x, df_value))
        
        x = x - f_value/df_value
        
        n += 1
        f_value = f(x)
        if store: info.append((x, f_value))
    if store:
        return x, n, info
    else:
        return x, n, f_value

def Secant(f, x1, x2, eps=1.0E-8, N=100, store=False):
    f_1 = f(x1)
    f_2 = f(x2)
    n = 0

    if store: info = [(x1, f_1)]    
    
    while abs(f_1) > eps and n <= N:
        if abs(f_1 - f_2) < 1.0E-14:
            raise ValueError("Secant method zero division")
        x1_copy = x1
        x1 -= (f_1*(x1-x2))/(f_1 - f_2)
        x2 = x1_copy
        
        f_1 = f(x1)
        f_2 = f(x2)
        
        n += 1
        
        if store: info.append((x1, f_1))
    
    if store:
        return x1, n, info
    else:
        return x1, n, f_1

def Bisection(f, a, b, eps=1.0E-8, N=100, store=False):
    fa = f(a)
    if fa*f(b) > 0:
        raise ValueError('No root in given interval.')
    
    n = 0
    
    if store: info = []
    
    while (b-a) > eps and n <= N:
        n += 1
        m = (a + b)/2.0
        fm = f(m)
        if fa*fm <= 0:
            b = m   ## root is on the left side
        else:
            a = m   ## root is on the right side
            fa = fm
            
        if store: info.append((m, fm))
        
    if store:
        return m, n, info
    else:
        return m, n, fm
    
###############################################################################
#####################          Reading input data         #####################
###############################################################################
    
parser = argparse.ArgumentParser()
parser.add_argument('--f', '--function', type=str, help='function')
parser.add_argument('--df', '--derivative', type=str, help='derivative')
parser.add_argument('--a', '--left', type=float, default=0.0, help='left boundary')
parser.add_argument('--b', '--right', type=float, default=0.0, help='right boundary')
parser.add_argument('--x0', '--first_x', type=float, default=0.0, help='first element')
parser.add_argument('--x1', '--second_x', type=float, default=0.0, help='second element')

args = parser.parse_args()
try:
    f  = StringFunction(args.f)
    df = StringFunction(args.df)
    a  = float(args.a)
    b  = float(args.b)
    x0 = float(args.x0)
    x1 = float(args.x1)
except:
    raise TypeError('Input arguments are not of correct type.')

###############################################################################
#####################    Call function and print output   #####################
###############################################################################

root, iterations, info = Newton(f, x0, dfdx=df, store=True)
print 'Newton method:'
print 'root x = %g found in %d iterations.' % (root, iterations)
for i in range(len(info)):
    print '%3d interations: x = %8g f(x) = %8g' % (i+1, info[i][0], info[i][1])
print

root, iterations, info = Secant(f, x0, x1, store=True)
print 'Secant method:'
print 'root x = %g found in %d iterations.' % (root, iterations)
for i in range(len(info)):
    print '%3d interations: x = %8g f(x) = %8g' % (i+1, info[i][0], info[i][1])
print

root, iterations, info = Bisection(f, a, b, store=True)
print 'Bisection method:'
print 'root x = %g found in %d iterations.' % (root, iterations)
for i in range(len(info)):
    print '%3d interations: x = %8g f(x) = %8g' % (i+1, info[i][0], info[i][1])
print