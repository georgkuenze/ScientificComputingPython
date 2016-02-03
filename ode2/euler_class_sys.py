# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:46:17 2015

@author: Georg
"""

import numpy as np
import matplotlib.pyplot as plt

class ForwardEuler:
    """
    Class for solving a scalar ODE or a system of ODEs (represented as vector)
    
    du/dt = f(u, t)
    
    by the Forward Euler Method.
    
    Class attributes:
    t: array of time values
    u: array of solution values (of functions u0, u1, ... at time points t)
    k: step number of the most recently computed solution
    f: callable object implementing the function f(u,t)
    """
    def __init__(self, f):
        if not callable(f):
            raise TypeError('f is %s, not a function' % type(f))
        self.f = lambda u, t: np.asarray(f(u,t))   ## make sure that function returns array
        
    def set_initial_condition(self, U0):
        if isinstance(U0, (float, int)):   ## scalar ODE
            self.neq = 1
        else:                              ## System of ODEs
            U0 = np.asarray(U0)
            self.neq = U0.size
        self.U0 = U0
    
    def solve(self, time_points):
        """Compute u for t values in time_points list."""
        self.t = np.asarray(time_points)
        n = self.t.size
        if self.neq == 1:   ## scalar ODE
            self.u = np.zeros(n)
        else:               ## System of ODEs
            self.u = np.zeros((n,self.neq))
            
        ## Assume self.t[0] corresponds to self.U0
        self.u[0] = self.U0
        
        ## Time loop
        for k in range(n-1):
            self.k = k
            self.u[k+1] = self.advance()
        return self.u, self.t
    
    def advance(self):
        """Advance the solution one time step."""
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        u_new = u[k] + dt*f(u[k], t[k])
        return u_new

def demo():
    ## Parameter
    def f(u,t):
        return np.array([u[1], -u[0]])
    solver = ForwardEuler(f=f)
    U0 = [0.0, 1.0]
    T  = 8*np.pi
    n  = 2000
    
    solver.set_initial_condition(U0=U0)
    time_points = np.linspace(0, T, n)
    u, t = solver.solve(time_points)
    u0 = u[:,0]
    u1 = u[:,1]
    
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(t, u0, 'b-', label='numeric solution')
    ax1.plot(t, np.sin(t), 'r--', label='exact solution')
    ax1.set_xlabel('time'); ax1.set_ylabel('u'); 
    ax1.legend(loc=1); ax1.set_title('solution of du/dt')
    
    ax2.plot(t, u1, 'b-', label='numeric solution')
    ax2.plot(t, np.cos(t), 'r--', label='exact solution')
    ax2.set_xlabel('time'); ax2.set_ylabel('u'); 
    ax2.legend(loc=1); ax2.set_title('solution of d2u/dt')
    
    fig.savefig('ode_sys.pdf')
    fig.show()

if __name__ == '__main__':
    demo()