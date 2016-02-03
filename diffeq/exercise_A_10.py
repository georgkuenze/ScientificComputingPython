# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 23:49:02 2015

@author: Georg
"""

import numpy as np
import matplotlib.pyplot as plt

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
        
        if store:
            info.append((x1, f_1))
    
    if store:
        return x1, n, info
    else:
        return x1, n, f_1

def func1(x):
    return -x**5 + np.sin(x)

def func2(x):
    return x**6 * np.sin(np.pi*x)

plt.plot(np.linspace(0,5,100), func1(np.linspace(0,5,100)), label='function 1')
plt.hold('on')
plt.plot(np.linspace(0,5,100), func2(np.linspace(0,5,100)), label='function 2')
plt.legend(loc='best')

x, n, info = Secant(func1, 1.0, 2.0, eps=1.0E-12 ,store=True)
print "Root at x = %g found after %d steps." % (x, n)
for i in range(len(info)):
    print "Step %3d: x = %8g f(x) = %8g" %(i, info[i][0], info[i][1])

x, n, info = Secant(func2, 3.5, 3.8, eps=1.0E-12 ,store=True)
print "\nRoot at x = %g found after %d steps." % (x, n)
for i in range(len(info)):
    print "Step %3d: x = %8g f(x) = %8g" %(i, info[i][0], info[i][1])