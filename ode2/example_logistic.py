# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 23:13:36 2015

@author: Georg
"""

import ode_solver_classes
import numpy as np
import matplotlib.pyplot as plt
from scitools.StringFunction import StringFunction

def find_dt(problem, method=ode_solver_classes.ForwardEuler, tol=0.01, dt_min=1.0E-6):
    """
    Return a "solved" class Solver instance where the difference in the solution
    and one with a double time step is less than tol.
    
    problem: class Problem instance
    method: class from ode_solver_classes module
    tol: tolerance (chose relative to problem.R)
    dt_min: minimum allowed time step.
    """
    dt = problem.T/10.0   ## start with 10 intervals
    solver = Solver(problem, dt, method)
    solver.solve()
    
    from scipy import interpolate
    
    good_approximation = False
    
    ## time step is halved every loop step
    ## the ODE is solved with new time step
    ## value array is converted to continuous function
    ## maximal difference between continuous functions is calculated
    ## loop proceeds until difference < tolerance
    while good_approximation == False:
        dt = dt/2.0
        if dt < dt_min:
            raise ValueError('dt=%g < %g - abort' % (dt, dt_min))
        
        solver2 = Solver(problem, dt, method)
        solver2.solve()
        
        ## Make continuous functions u(t) and u2(t)
        u  = interpolate.interp1d(solver.t, solver.u, kind='cubic')
        u2 = interpolate.interp1d(solver2.t, solver2.u, kind='cubic')
        
        ## Sample the difference in n points in [0, t_end]
        n = 13
        t_end = min(solver2.t[-1], solver.t[-1])
        t = np.linspace(0, t_end, n)
        u_diff = np.abs(u(t) - u2(t)).max()
        print u_diff, dt, tol
        if u_diff < tol:
            good_approximation = True
        else:
            solver = solver2
    
    return solver2   

class Problem:
    def __init__(self, alpha, R, U0, T):
        """
        alpha, R: parameters in the ODE.
        U0: initial condition
        T: maximal length of time interval;
        asymptotic value R must be reached within 1% accuracy for some t <= T.
        """
        self.alpha, self.R, self.U0, self.T = alpha, R, U0, T
        
    def __call__(self, u, t):
        """Return f(u,t) for logistic ODE."""
        return self.alpha*u*(1 - u/self.R)
    
    def terminate(self, u, t, step_no):
        """Return True when asymptotic value R is reached."""
        tol = self.R*0.01
        return abs(u[step_no] - self.R) < tol
        
    def __str__(self):
        """Pretty print of physical parameters."""
        return 'alpha=%g, R=%g, U0=%g' % (self.alpha, self.R, self.U0)

class Problem2:
    def __init__(self, alpha, R, U0, T):
        """
        alpha, R: parameters in the ODE.
        U0: initial condition
        T: maximal length of time interval;
        asymptotic value R must be reached within 1% accuracy for some t <= T.
        """
        self.alpha, self.U0, self.T = alpha, U0, T
        if isinstance(R, (float, int)):
            self.R = lambda t: R
        elif callable(R):
            self.R = R
        else: raise TypeError('R is %s, has to be number or function' % type(R))
        
    def __call__(self, u, t):
        """Return f(u,t) for logistic ODE."""
        return self.alpha*u*(1 - u/self.R(t))
    
    def terminate(self, u, t, step_no):
        """Return True when asymptotic value R is reached."""
        tol = self.R(t[step_no])*0.01
        return abs(u[step_no] - self.R(t[step_no])) < tol
    
    def __str__(self):
        return 'alpha=%g, U0=%g' % (self.alpha, self.U0)

class Problem3(Problem):
    def __init__(self):
        ## Set default parameters
        self.alpha = 1.0
        self.R     = StringFunction('1.0', independent_variable='t')
        self.U0    = 0.01
        self.T     = 4.0
        
    def define_command_line_arguments(self, parser):
        """Add arguments to parser (argparse.ArgumentParser)."""
        
        def evalcmlarg(text):
            return eval(text)
            
        def toStringFunction(text):
            return StringFunction(text, independent_variable='t')
        
        parser.add_argument('--alpha', dest='alpha', type=evalcmlarg, default=self.alpha,
                            help='initial growth rate in logistic model')
        parser.add_argument('--R', dest='R', type=toStringFunction, default=self.R,
                            help='carrying capacity of the environment')
        parser.add_argument('--U0', dest='U0', type=evalcmlarg, default=self.U0,
                            help='initial condition')
        parser.add_argument('--T', dest='T', type=evalcmlarg, default=self.T,
                            help='time interval for integration [0,T]')
        return parser
    
    def set(self, **kwargs):
        """
        Set parameters as keyword arguments alpha, R, U0, T, or as args
        (objects returned by parser.parse_args()).
        """
        
        for prm in ('alpha', 'R', 'U0', 'T'):
            if prm in kwargs:
                setattr(self, prm, kwargs[prm])
        if 'args' in kwargs:
            args = kwargs['args']
            for prm in ('alpha', 'R', 'U0', 'T'):
                if hasattr(args, prm):
                    setattr(self, prm, getattr(args, prm))
                else:
                    print 'Really strange', dir(args)
    
    def __call__(self, u, t):
        """Return f(u,t) for logistic ODE."""
        return self.alpha*u*(1 - u/self.R(t))
    
    def terminate(self, u, t, step_no):
        """Return True when asymptotic value R is reached."""
        tol = self.R(t[step_no])*0.01
        return abs(u[step_no] - self.R(t[step_no])) < tol
    
    def __str__(self):
        return 'alpha=%g, U0=%g' % (self.alpha, self.U0)        

class Solver:
    def __init__(self, problem, dt, method=ode_solver_classes.ForwardEuler):
        """
        problem: instance of class Problem
        dt: time step
        method: class from ode_solver_classes module
        """
        self.problem, self.dt, self.method = problem, dt, method
    
    def solve(self):
        solver = self.method(self.problem)
        solver.set_initial_condition(self.problem.U0)
        n = int(round(self.problem.T/self.dt))
        time_points = np.linspace(0, self.problem.T, n+1)
        self.u, self.t = solver.solve(time_points, self.problem.terminate)
        
        ## The solution is terminated if the limiting value was reached
        if solver.k+1 == n:   ## no termination, final T was reached
            self.plot()
            raise ValueError('Termination criterion not reached, choose T > %g'
            % self.problem.T)
    
    def plot(self):
        filename = 'logistic_growth_' + self.problem.__str__() + '.pdf'
        plt.plot(self.t, self.u)
        plt.xlabel('time'); plt.ylabel('u'); 
        plt.title(self.problem.__str__() + ', dt=%g' % self.dt)
        plt.savefig(filename)
        plt.show()

class AutoSolver(Solver):
    """Subclass of Solver that automatically finds appropriate dt."""
    def __init__(self, problem, dt=None, method=ode_solver_classes.ForwardEuler, 
                 tol=0.01, dt_min=1.0E-6):
        Solver.__init__(self, problem, dt, method)
        if dt is None:
            solver = find_dt(self.problem, method, tol, dt_min)
            self.dt = solver.dt
            self.u, self.t = solver.u, solver.t
    
    def solve(self, method=ode_solver_classes.ForwardEuler):
        if hasattr(self, 'u'):
            ## Solution was computed by find_dt function in constructor method
            pass
        else:
            Solver.solve(self)

def demo1():
    problem = Problem(alpha=0.2, R=1, U0=0.1, T=40)
    solver  = Solver(problem=problem, dt=0.1)
    solver.solve()  
    solver.plot()

def demo2():
    problem = Problem(alpha=0.1, R=500, U0=2, T=130)
    solver  = AutoSolver(problem=problem, tol=1)
    solver.solve(method=ode_solver_classes.RungeKutta4)
    solver.plot()

def demo3():
    problem = Problem2(alpha=0.1, U0=2, T=130, R=lambda t: 500 if t < 60 else 100)
    solver  = AutoSolver(problem=problem, tol=1)
    solver.solve(method=ode_solver_classes.RungeKutta4)
    solver.plot()

def demo4():
    problem = Problem3()
    problem.set(alpha=0.1, U0=2, T=130, R=lambda t: 500 if t < 60 else 100)
    solver = AutoSolver(problem=problem, tol=1)
    solver.solve(method=ode_solver_classes.RungeKutta4)
    solver.plot()

def demo5():
    problem = Problem3()
    import argparse
    parser = argparse.ArgumentParser(description='Logistic ODE model')
    parser = problem.define_command_line_arguments(parser)
    
    ## Try --alpha 0.11 --T 130 --U0 2 --R "500 if t < 60 else 300"
    args = parser.parse_args()
    problem.set(args=args)
    solver = AutoSolver(problem, tol=1)
    solver.solve(method=ode_solver_classes.RungeKutta4)
    solver.plot()

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2:
        demo5()
    else:
        demo1()
        demo2()
        demo3()
        demo4()
    