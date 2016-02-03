# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:17:17 2015

@author: Georg
"""

import numpy as np
import euler_class
import matplotlib.pyplot as plt
import sys

class Logistic:
    """Problem class for a logistic ODE."""
    def __init__(self, alpha, R, U0, T):
        self.alpha, self.R, self.U0, self.T = alpha, float(R), U0, T
    
    def __call__(self, u, t):
        """Return f(u,t) for the logistic ODE."""
        return self.alpha*u*(1 - u/self.R)
    
    def __str__(self):
        """Return ODE and initial condition."""
        return "u'(t) = %g*u*(1 - u/%g), t in [0, %g]\nu(0) = %g" \
        % (self.alpha, self.R, self.T, self.U0)

def get_input():
    """Read alpha, R, U0, T, and n from the command line."""
    try:
        alpha = float(sys.argv[1])
        R     = float(sys.argv[2])
        U0    = float(sys.argv[3])
        T     = float(sys.argv[4])
        n     = int(sys.argv[5])
    except IndexError:
        print 'Usage: %s alpha R U0 T n' % sys.argv[0]
        sys.exit(1)
    return alpha, R, U0, T, n

def logistic():
    alpha, R, U0, T, n = get_input()
    problem = Logistic(alpha=alpha, R=R, U0=U0, T=T)
    solver = euler_class.ForwardEuler_v2(problem)
    solver.set_initial_condition(problem.U0)
    time_points = np.linspace(0, T, n+1)
    u, t = solver.solve(time_points)

    plt.plot(t, u)
    plt.xlabel('time'); plt.ylabel('u')
    plt.title('Logistic growth: alpha=%g, R=%g, dt=%g' \
    % (problem.alpha, problem.R, t[1]-t[0]))
    plt.savefig('logistic.pdf')
    plt.show(block=True)

if __name__ == '__main__':
    logistic()