# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 21:49:13 2015

@author: Georg
"""
import numpy as np

def terminate(u, t, step_no):
    eps = 1.0E-6                     ## returns True if value
    return abs(u[step_no,0]) < eps   ## is close enough to zero

def Newton(f, x, dfdx, epsilon=1.0E-7, N=100, store=False):
    f_value = f(x)
    n = 0
    if store: info = [(x, f_value)]
    while abs(f_value) > epsilon and n <= N:
        dfdx_value = float(dfdx(x))
        if abs(dfdx_value) < 1E-14:
            raise ValueError("Newton: f'(%g)=%g" % (x, dfdx_value))

        x = x - f_value/dfdx_value

        n += 1
        f_value = f(x)
        if store: info.append((x, f_value))
    if store:
        return x, info
    else:
        return x, n, f_value

class Derivative:
    def __init__(self, f, h=1.0E-6):
        self.f = f
        self.h = h
    
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x-h))/(2.0*h)

class ODESolver:
    """Superclass for Solving ODEs."""
    def __init__(self, f):
        if not callable(f):
            raise TypeError('f is %s, not a function' % type(f))
        self.f = lambda u, t: np.asarray(f(u,t))
    
    def advance(self):
        """Advance solution one time step."""
        raise NotImplementedError
    
    def set_initial_condition(self, U0):
        if isinstance(U0, (float, int)):   ## scalar ODE
            self.neq = 1
            U0 = float(U0)
        else:                              ## system of ODEs
            U0 = np.asarray(U0)
            self.neq = U0.size
        self.U0 = U0
        
    def solve(self, time_points, terminate=None):
        if terminate is None:
            terminate = lambda u, t, step_no: False
        
        self.t = np.asarray(time_points)
        n = self.t.size
        if self.neq == 1:                  ##  scalar ODE
            self.u = np.zeros(n)
        else:                              ## system of ODEs
            self.u = np.zeros((n, self.neq))
            
        ## Assume that self.t[0] corresponds to self.U0
        self.u[0] = self.U0
        
        ## Time loop
        for k in range(n-1):
            self.k = k
            self.u[k+1] = self.advance()
            if terminate(self.u, self.t, self.k+1):
                break                      ## terminate loop over k
        return self.u[:k+2], self.t[:k+2]  ## returns only array slices that have
                                           ## been filled with values before break.
                                           ## If terminate was never true, the full
                                           ## array is returned

class ForwardEuler(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        u_new = u[k] + dt*f(u[k], t[k])
        return u_new
    
class RungeKutta4(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        dt2 = dt/2.0
        K1 = dt*f(u[k], t[k])
        K2 = dt*f(u[k] + 0.5*K1, t[k] + dt2)
        K3 = dt*f(u[k] + 0.5*K2, t[k] + dt2)
        K4 = dt*f(u[k] + K3, t[k] + dt)
        u_new = u[k] + (1/6.0)*(K1 + 2*K2 + 2*K3 + K4)
        return u_new

class BackwardEuler(ODESolver):
    def __init__(self, f):
        ODESolver.__init__(self, f)
        """Make a sample call to check that f is a scalar function."""
        try:
            u = np.array([1]); t = 1
            value = f(u, t)
        except IndexError:
            raise TypeError('f(u,t) must be a scalar function and return a float/int.')
    
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        def F(w):
            return w - dt*f(w, t[k+1]) -u[k]
        dFdw = Derivative(F)
        w_start = u[k] + dt*f(u[k], t[k])  ## Guess start value for Newton's method
                                           ## by a Forward Euler step
        u_new, n, F_value = Newton(F, w_start, dFdw, N=50)
        if n >= 50:
            print "Newton's method failed to converge at t=%g (%d iterations)" \
            % (t, n)
        if k == 0:
            self.Newton_iter = []
        self.Newton_iter.append(n)
        return u_new

registered_solver_classes = [
    ForwardEuler, RungeKutta4, BackwardEuler]

def test_exact_numerical_solution():
    a = 0.2; b = 3

    def f(u, t):
        return a + (u - u_exact(t))**5

    def u_exact(t):
        """Exact u(t) corresponding to f above."""
        return a*t + b

    U0 = u_exact(0)
    T = 8
    n = 10
    tol = 1E-15
    t_points = np.linspace(0, T, n)
    for solver_class in registered_solver_classes:
        solver = solver_class(f)
        solver.set_initial_condition(U0)
        u, t = solver.solve(t_points)
        u_e = u_exact(t)
        max_error = (u_e - u).max()
        msg = '%s failed with max_error=%g' % \
              (solver.__class__.__name__, max_error)
        assert max_error < tol, msg

if __name__ == '__main__':
    test_exact_numerical_solution()