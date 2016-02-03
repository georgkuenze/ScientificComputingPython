# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 22:20:20 2015

@author: Georg
"""
from math import cos, sin, pi
import glob, os

for filename in glob.glob('Newton_plot.pdf'):
    os.remove(filename)

def Newton(f, x, dfdx='numeric', eps=1.0E-7, N=100, store=False):
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

def func(x):
    return x**6 * sin(pi*x)

def derivative(x):
    return pi*x**6 * cos(pi*x) + 6*x**5 * sin(pi*x) 

def Newton_plot(f, x, dfdx, xmin, xmax, eps=1.0E-7):
    x0, n, series = Newton(f, x, dfdx, eps=eps, N=100, store=True)
    xn = [series[i][0] for i in range(len(series))]
    yn = [abs(series[i][1]) for i in range(len(series))]
    
    x = [(xmax-xmin)/100.0*i + xmin for i in range(101)]
    y = [f(x_) for x_ in x]
    
    plt.rc('figure', figsize=(8,8))
    fig = plt.figure()
    ax1 = fig.add_subplot(221); ax2 = fig.add_subplot(222); ax3 = fig.add_subplot(223)
    plt.subplots_adjust(wspace=0.3, hspace=0.3)
    
    ax1.plot(x, y, 'k-', label='f(x)')
    ax1.set_xlim(xmin, xmax)
    ax1.set_xlabel('x')
    ax1.set_ylabel('f(x)')
    ax1.legend(loc='best')    
    
    ax2.plot(range(len(series)), xn, 'bo', label='xn')
    ax2.set_xlabel('steps')
    ax2.set_ylabel('xn')
    ax2.legend(loc='best')
    
    ax3.semilogy(range(len(series)), yn, 'ro', label='abs(f(xn))')
    ax3.set_xlabel('steps')
    ax3.set_ylabel('abs(f(xn))')
    ax3.legend(loc='best')
    
    plt.suptitle("Convergence of Newton's method")
    
    fig.savefig('Newton_plot.pdf')

Newton_plot(func, -2.6, derivative, -4, 0, eps=1.0E-13)