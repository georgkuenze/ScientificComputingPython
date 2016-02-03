# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 14:01:12 2015

@author: Georg
"""

import numpy as np
from math import factorial
import matplotlib.pyplot as plt
import time, glob, os

for filename in glob.glob('taylor_*.png'):
    os.remove(filename)

def func_exp(x, k):
    return x**k/factorial(k)

def func_sin(x, k):
    return (((-1)**k)*x**(2*k+1))/factorial(2*k+1)

def func_exp_minus(x, k):
    return (-1*x)**k/factorial(k)    

def animate_series(fk, M, N, xmin, xmax, n, exact):
    
    x = np.linspace(xmin, xmax, n)
    y_exact = exact(x)
    
    plt.ion()
    fig = plt.figure()
    plt.axis([xmin, xmax, y_exact.min(), y_exact.max()])    
    
    lines = plt.plot([],[], x, exact(x))
    lines[0].set_ls('None')
    lines[0].set_marker('o')
    lines[0].set_color('r') 
    lines[1].set_ls('-')
    lines[1].set_color('k')
    lines[1].set_label('exact function: %s' %(exact.__name__))
    
    plt.xlabel('X')
    plt.ylabel('Y')    
        
    k = np.arange(M,N+1)
    S = np.zeros(len(x), dtype='float64')
    
    counter = 0
    for i in range(len(k)):
        S += fk(x, k[i])
        
        lines[0].set_data(x, S)
        lines[0].set_label('taylor polynomial of degree %s' % (str(k[i])))
        plt.legend()
        plt.draw()
        plt.savefig('taylor_%04d.png' % (counter))
        counter += 1
    

# summation limits
M = 0
N = 80
xmin = 0
xmax = 13*np.pi
n = 1000

animate_series(func_sin, M, N, xmin, xmax, n, np.sin)