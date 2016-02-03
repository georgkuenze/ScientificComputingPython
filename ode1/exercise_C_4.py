# -*- coding: utf-8 -*-
"""
Created on Wed Oct 07 16:37:49 2015

@author: Georg
"""

import numpy as np
import matplotlib.pyplot as plt

dt = [1.1, 1.5, 1.9]
alpha = -1.0

def compute_ode(alpha, dt, u0=1.0):
    n = int(100.0/dt)
    t = np.linspace(0, 100, n+1)
    u = np.zeros(n+1)
    u[0] = u0
    for k in range(1,n+1):
        u[k] = u[0]*(1+alpha*dt)**k
    return t, u

for value in dt:
    t, u = compute_ode(alpha, value)
    plt.plot(t, u, label='dt = %1.1f' % value)
plt.legend(loc='best')