# -*- coding: utf-8 -*-
"""
Created on Wed Oct 07 21:37:52 2015

@author: Georg
"""

import numpy as np
import matplotlib.pyplot as plt

def growth_v1(a, b, u0, T, n):
    t  = np.linspace(0, T, n+1)
    dt = T/float(n)
    u  = np.zeros(n+1)
    u[0] = u0
    alpha = a - b*t
    for k in range(n):
        u[k+1] = u[k]*(1+alpha[k]*dt)
    return t, u

def growth_v2(a, b, u0, T, n):
    t  = np.linspace(0, T, n+1)
    dt = T/float(n)
    u  = np.zeros(n+1)
    u[0] = u0
    alpha = a - b*0.5*T
    for k in range(n):
        u[k+1] = u[k]*(1+alpha*dt)
    return t, u
    
a  = 1.0
b  = 0.1
u0 = 1.0
T  = 10.0
n  = 1000

t_v1, u_v1 = growth_v1(a, b, u0, T, n)
t_v2, u_v2 = growth_v2(a, b, u0, T, n)

plt.plot(t_v1, u_v1, label='time variant growth coefficient')
plt.hold('on')
plt.plot(t_v2, u_v2, label='constant growth coefficient')
plt.legend(loc='best')