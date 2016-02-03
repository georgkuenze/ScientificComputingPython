# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:02:45 2015

@author: Georg
"""
import numpy as np
import matplotlib.pyplot as plt
import ode_solver_classes
plt.rc('figure', figsize=(10,10))

class OscSystem:
    def __init__(self, m, beta, k, g, w):
        self.m, self.beta, self.k, self.g, self.w = \
        float(m), float(beta), float(k), float(g), w
    
    def __call__(self, u, t):
        u0, u1 = u
        m, beta, k, g, w = self.m, self.beta, self.k, self.g, self.w
        ## Use a finite difference for w''(t)
        h = 1.0E-6
        ddw = (w(t+h) - 2*w(t) + w(t-h))/(h**2)
        f = [u1, ddw + g - beta/m*u1 - k/m*u0]
        return f

f = OscSystem(m=1.0, beta=0.0, k=1.0, g=0.0, w=lambda t: 0)
u_init = [1, 0]   ## initial conditions
nperiods = 3.5    ## no of oscillation periods
T = 2*np.pi*nperiods

fig, axarr = plt.subplots(2,2)

for solver_class, i in zip([ode_solver_classes.ForwardEuler, 
                            ode_solver_classes.RungeKutta4], range(2)):
    if solver_class == ode_solver_classes.ForwardEuler:
        npoints_per_period = 200
    elif solver_class == ode_solver_classes.RungeKutta4:
        npoints_per_period = 20
    n = npoints_per_period*nperiods
    t_points = np.linspace(0, T, n+1)
    solver = solver_class(f)
    solver.set_initial_condition(u_init)
    u, t = solver.solve(t_points)
    
    u0_values = u[:, 0]
    u1_values = u[:, 1]
    u0_exact  = np.cos(t)
    u1_exact  = -1.0*np.sin(t)
    axarr[0, i].plot(t, u0_values, 'r-', label='numeric')
    axarr[0, i].plot(t, u0_exact, 'b-', label='exact')
    axarr[0, i].set_xlabel('time'); axarr[0, i].set_ylabel('u0')
    axarr[0, i].set_ylim([-1.5, 1.5]); axarr[0, i].legend(loc=1)
    axarr[0, i].set_title('Oscillating System Position - %s' % solver_class.__name__)
    axarr[1, i].plot(t, u1_values, 'r-', label='numeric')
    axarr[1, i].plot(t, u1_exact, 'b-', label='exact')
    axarr[1, i].set_xlabel('time'); axarr[1, i].set_ylabel('u1')
    axarr[1, i].set_ylim([-1.5, 1.5]); axarr[1, i].legend(loc=1)
    axarr[1, i].set_title('Oscillating System Velocity - %s' % solver_class.__name__)
fig.savefig('oscillating_system.pdf')
fig.show()