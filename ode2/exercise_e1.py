# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 18:50:22 2015

@author: Georg
"""

import numpy as np
import matplotlib.pyplot as plt

def f(u,t):
    return 0.1*u

def ForwardEuler(f, U0, T, n):
    """Solve u'=f(u,t), u(0)=U0, with n steps until t = T."""
    t = np.linspace(0, T, n+1)
    u = np.zeros(n+1)
    u[0] = U0
    dt = T/float(n)
    for k in range(n):
        u[k+1] = u[k] + dt*f(u[k], t[k])
    return t, u

def exact(t):
    return 0.2*np.exp(0.1*t)

U0 = 0.2
T = 20.0

for k in [10**i for i in range(1,4)]:
    t_approx, u_approx = ForwardEuler(f, U0, T, k)
    plt.plot(t_approx, u_approx, lw=2, label = 'num. solution with n = %d points' % k)
    plt.hold('on')

u_exact = exact(np.linspace(0, T, 1000+1))
plt.plot(np.linspace(0, T, 11), u_exact[::100], 'bo', label = 'exact solution')
plt.xlabel('time'); plt.ylabel('u(t)'); plt.legend(loc='best')