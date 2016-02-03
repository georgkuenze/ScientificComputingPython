# -*- coding: utf-8 -*-
"""
Created on Thu Oct 01 23:31:39 2015

@author: Georg
"""
import sys
import numpy as np
import matplotlib.pyplot as plt

def get_input():
    try:
        q = float(sys.argv[1])
        n = int(sys.argv[2])
    except:
        raise TypeError('Provide input data for q and n on command line e.g. "2.0 1000"')
    return q, n
    
def compute_ode(q, n, u0=1.0):
    if q == 1.0:
        T = 6.0
    elif q > 1.0:
        T = 1.0/(q-1) - 0.1
    else:
        raise ValueError('q is nagative.')
    t = np.linspace(0,T,n+1)
    dt = T/float(n)
    u  = np.zeros(n+1)
    u[0] = u0
    for k in range(n):
        u[k+1] = (u[k]**q)*dt + u[k]
    return u, t

def exact_ode(q, n):
    if q == 1.0:
        T = 6.0
        func = lambda x: np.exp(x)
    elif q > 1.0:
        T = 1.0/(q-1) - 0.1
        func = lambda x: (x*(1-q)+1)**(1.0/(1-q))
    else:
        raise ValueError('q is nagative.')
    t = np.linspace(0,T,n+1)    
    u = np.zeros(len(t))
    for i in range(len(t)):
        u[i] = func(t[i])
    return u, t

q, n = get_input()
u_app, t_app = compute_ode(q, n)
u_excat, t_exact = exact_ode(q, n)

plt.plot(t_app, u_app, 'k-', label='numeric solution')
plt.hold('on')
plt.plot(t_exact, u_excat, 'b-', label='exact solution')
plt.xlabel('t')
plt.ylabel('u(t)')
plt.legend(loc='best')
plt.show()