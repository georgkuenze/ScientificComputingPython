# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:42:30 2015

@author: Georg
"""

import numpy as np

class ForwardEuler_v1:
    def __init__(self, f, U0, T, n):
        self.U0, self.T, self.n = U0, T, n
        if callable(f):
            self.f = f
        else:
            raise TypeError('f is %s, not a function' % type(f))
        
        self.dt = T/float(n)
        self.u  = np.zeros(n+1)
        self.t  = np.zeros(n+1)
    
    def solve(self):
        """Compute solution for 0 <= t <= T."""
        self.u[0] = float(self.U0)
        self.t[0] = float(0)
        
        for k in range(self.n):
            self.k = k
            self.t[k+1] = self.t[k] + self.dt
            self.u[k+1] = self.advance()
        
        return self.u, self.t
    
    def advance(self):
        """Advance the solution one time step."""
        u, dt, f, k, t = self.u, self.dt, self.f, self.k, self.t
        
        u_new = u[k] + dt*f(u[k], t[k])
        return u_new

class ForwardEuler_v2:
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
        
        return self.u, self.t
        
    def advance(self):
        """Advance the solution one time step."""
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        u_new = u[k] + dt*f(u[k], t[k])
        return u_new

def test_ForwardEuler_v1_against_hand_calculations():
    """Verify ForwardEuler_v1 against hand calculations for 2 time steps."""
    solver = ForwardEuler_v1(lambda u, t: u, 1.0, 0.2, 2)
    u, t = solver.solve()
    exact = np.array([1, 1.1, 1.21])
    error = np.abs(exact - u).max()
    assert error < 1E-14, 'abs(exact - u) = %g != 0' % error

def test_ForwardEuler_v2_against_hand_calculations():
    """Verify ForwardEuler_v2 against hand calculations for 2 time steps."""
    solver = ForwardEuler_v2(lambda u, t: u)
    solver.set_initial_condition(1)
    u, t = solver.solve([0, 0.1, 0.2])
    exact = np.array([1, 1.1, 1.21])
    error = np.abs(exact - u).max()
    assert error < 1E-14, 'abs(exact - u) = %g != 0' % error

def test_ForwardEuler_against_linear_solution():
    """Use knowledge of an exact numerical solution for testing."""
    u_exact = lambda t: 0.2*t + 3
    solver = ForwardEuler_v2(lambda u, t: 0.2 + (u - u_exact(t))**4)
    
    ## Solve for first time interval [0, 1.2]
    solver.set_initial_condition(u_exact(0))
    u1, t1 = solver.solve([0, 0.4, 1.0, 1.2])
    
    ## Continue with a new time interval [1.2, 1.5]
    solver.set_initial_condition(u1[-1])
    u2, t2 = solver.solve([1.2, 1.4, 1.5])
    
    ## Append u2 to u1 and t2 to t1
    u = np.concatenate((u1, u2))
    t = np.concatenate((t1, t2))
    
    u_e = u_exact(t)
    error = np.abs(u_e - u).max()
    assert error < 1E-14, 'abs(exact - u) = %g != 0' % error

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        test_ForwardEuler_v1_against_hand_calculations()
        test_ForwardEuler_v2_against_hand_calculations()
        test_ForwardEuler_against_linear_solution()    