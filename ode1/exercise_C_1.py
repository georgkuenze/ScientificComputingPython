# -*- coding: utf-8 -*-
"""
Created on Thu Oct 01 17:10:18 2015

@author: Georg
"""
import numpy as np
import matplotlib.pyplot as plt

def compute_ode(n, u0):
    t  = np.linspace(0,6,n+1)
    dt = 6.0/float(n)
    u  = np.zeros(n+1)
    u[0] = u0
    for k in range(n):
        u[k+1] = u[k]*(2*dt + 1) - dt
    return u, t

def exact_ode(n):
    t = np.linspace(0,6,int(n)+1)
    u = 1.5*np.exp(2*t) + 0.5
    return u, t

u_approx, t_approx = compute_ode(10000, 2)
u_exact, t_exact = exact_ode(10000)

plt.plot(t_approx, u_approx, 'k-', label='numeric solution')
plt.hold('on')
plt.plot(t_exact, u_exact, 'b-', label='exact solution')
plt.legend(loc='best')