# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 19:29:47 2015

@author: Georg
"""
import numpy as np
import matplotlib.pyplot as plt

class ForwardEuler:
    """Class for solving an ODE with FowardEuler method."""
    def __init__(self, f):
        if not callable(f):
            raise TypeError('f is %s, not a function' % type(f))
        self.f = f
        
    def set_initial_condition(self, U0):
        self.U0 = float(U0)
    
    def solve(self, time_points):
        """Compute u for t values in time_points list."""
        self.t = np.asarray(time_points)
        self.u = np.zeros(len(time_points))
        ## Assume self.t[0] corresponds to self.U0
        self.u[0] = self.U0
        
        for k in range(len(self.t)-1):
            self.k = k
            self.u[k+1] = self.advance()
        
        return self.t, self.u
        
    def advance(self):
        """Advance the solution one time step."""
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        u_new = u[k] + dt*f(u[k], t[k])
        return u_new

class Exponential:
    """Problem class that holds the parameter of the ODE."""
    def __init__(self, U0, T):
        self.U0, self.T = float(U0), float(T)
        
    def __call__(self, u, t):
        return 0.1*u
    
    def __str__(self):
        """Return ODE and initial condition."""
        return "u'(t) = 0.1*u, t in [0, %g], u(0)=%g" % (self.T, self.U0)

def exact(t):
    return 0.2*np.exp(0.1*t)

for k in [10**i for i in range(1,4)]:
    problem = Exponential(U0=0.2, T=20)
    solver  = ForwardEuler(problem)
    solver.set_initial_condition(problem.U0)
    time_points = np.linspace(0, problem.T, k+1)
    t_approx, u_approx = solver.solve(time_points)
    plt.plot(t_approx, u_approx, lw=2, label = 'num. solution with n = %d points' % k)
    plt.hold('on')

u_exact = exact(np.linspace(0, problem.T, 1000+1))
plt.plot(np.linspace(0, problem.T, 11), u_exact[::100], 'bo', label = 'exact solution')
plt.xlabel('time'); plt.ylabel('u(t)'); plt.legend(loc='best')