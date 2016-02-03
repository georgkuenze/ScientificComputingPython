# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 21:04:17 2015

@author: Georg
"""

import numpy as np
import matplotlib.pyplot as plt
import ode_solver_classes
plt.rc('figure', figsize=(5,5))

def f(u, t):
    x, vx, y, vy = u
    g = 9.81
    return [vx, 0, vy, -g]

def terminate(u, t, step_no):
    return False if u[step_no, 2] >= 0 else True
    
def exact(x, theta, v0, g, y0):
    return x*np.tan(theta) - (1/(2.0*v0**2))*((g*x**2)/(np.cos(theta)**2)) + y0    
    
v0 = 5
theta = 80*np.pi/180
U0 = [0, v0*np.cos(theta), 0, v0*np.sin(theta)]
T = 1.2; dt = 0.01; n = int(round(T/dt))
t_points = np.linspace(0, T, n+1)
solver = ode_solver_classes.ForwardEuler(f)
solver.set_initial_condition(U0)
u, t = solver.solve(time_points=t_points, terminate=terminate)

x = u[:,0]; y = u[:,2]; y_exact = exact(x, theta, v0, 9.81, 0)

plt.plot(x, y, 'r-', label='numeric')
plt.hold('on')
plt.plot(x, y_exact, 'b-', label='exact')
plt.xlabel('x'); plt.ylabel('y'); plt.legend(loc=1)
plt.savefig('ball_trajectory.pdf')
plt.show()
