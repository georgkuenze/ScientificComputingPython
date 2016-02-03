# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 22:47:24 2015

@author: Georg
"""

import ode_solver_classes
import numpy as np
import matplotlib.pyplot as plt

## Test ForwardEuler method for different time steps
def f(u, t):
    return -u

solver = ode_solver_classes.ForwardEuler(f)
solver.set_initial_condition(1)

T = 3
plt.figure(1)
for dt in 1.5, 1.0, 0.5, 0.1:
    n = int(T/dt)
    time_points = np.linspace(0, T, n+1)
    u, t = solver.solve(time_points)
    plt.plot(t, u, label='dt = %g' % dt)
    plt.hold('on')
plt.plot(t, np.exp(-t), 'bo', label='exact solution')
plt.xlabel('time'); plt.ylabel('u'); plt.title('Dependence on time interval')
plt.legend(loc='best')

## Compare 4-th order Runge-Kutta and ForwardEuler method
T = 3; dt = 0.5
n = int(round(T/dt))
time_points = np.linspace(0, T, n+1)
plt.figure(2)
for solver_class in [ode_solver_classes.RungeKutta4, ode_solver_classes.ForwardEuler]:
    solver = solver_class(f)
    solver.set_initial_condition(1)
    u, t = solver.solve(time_points)
    plt.plot(t, u, label='%s' % solver_class.__name__)
    plt.hold('on')
plt.plot(t, np.exp(-t), 'bo', label='exact solution')
plt.xlabel('time'); plt.ylabel('u'); plt.title('Dependence on ODE solver method')
plt.legend(loc='best')