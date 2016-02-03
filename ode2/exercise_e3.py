# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 19:59:39 2015

@author: Georg
"""

import ode_solver_classes
import numpy as np
import matplotlib.pyplot as plt

def f(u, t):
    return 0.1*u

def exact(t):
    return 0.2*np.exp(0.1*t)

U0 = 0.2
T = 20.0

for k in [10**i for i in range(1,4)]:
    solver  = ode_solver_classes.ForwardEuler(f)
    solver.set_initial_condition(U0=U0)
    time_points = np.linspace(0, T, k+1)
    u_approx, t_approx = solver.solve(time_points)
    plt.plot(t_approx, u_approx, lw=2, label = 'num. solution with n = %d points' % k)
    plt.hold('on')

u_exact = exact(np.linspace(0, T, 1000+1))
plt.plot(np.linspace(0, T, 11), u_exact[::100], 'bo', label = 'exact solution')
plt.xlabel('time'); plt.ylabel('u(t)'); plt.legend(loc='best')