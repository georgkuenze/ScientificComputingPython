# -*- coding: utf-8 -*-
"""
Created on Thu Oct 08 23:14:33 2015

@author: Georg
"""

from ode_project import init_prms, solve
from math import cos
import matplotlib.pyplot as plt

def exact_S_solution(t):
    return g*(1-cos(t))
    
def check_S(S, t, step):
    error = exact_S_solution(t) - S[step]
    print 't = %5.2f   S[%04d] = %+g   error = %g' % (t, step, S[step], error)

## Fixed values for a test
from math import pi
m = 1; b = 2; L = 10; k = 1; beta = 0; S0 = 0; dt = 2*pi/40; g = 9.81; N = 200

def w(t):
    return 0

S = solve(m, k, beta, S0, dt, g, w, N, user_action=check_S)

plt.plot(S)
plt.xlabel('time')
plt.ylabel('Y')