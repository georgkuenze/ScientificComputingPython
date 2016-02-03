# -*- coding: utf-8 -*-
"""
Created on Fri Oct 09 15:42:24 2015

@author: Georg
"""

from ode_project import init_prms, solve
import numpy as np
import matplotlib.pyplot as plt
import glob, os

for filename in glob.glob('tmp_errors*.pdf'):
    os.remove(filename)

def exact_S_solution(t):
    return g*(1 - np.cos(t))

## Default values
m = 1; b = 2; L = 10; k = 1; beta = 0; S0 = 0; 
dt = 2*np.pi/40; g = 9.81; w_formula='0'; N = 200

m, b, L, k, beta, S0, dt, g, w, N = init_prms(m, b, L, k, beta, S0, dt, g, w_formula, N)

def w(t):
    return 0

S = solve(m, k, beta, S0, dt, g, w, N)
S = np.array(S)

tcoor = np.linspace(0, N*dt, len(S))
exact = exact_S_solution(tcoor)
error = exact - S
fig1, (ax1, ax2) = plt.subplots(1,2)
ax1.plot(tcoor, S, 'r-', label='numeric solution')
ax1.plot(tcoor, exact, 'b-', label='exact solution')
ax1.set_xlabel('time'); ax1.set_ylabel('S'); ax1.legend(loc=1)
ax2.plot(tcoor, error, 'b-', label='error')
ax2.set_xlabel('time'); ax2.set_ylabel('error'); ax2.legend(loc=1)
fig1.show()
fig1.savefig('tmp_errors_1.pdf')

fig2 = plt.figure()
dt = 2*np.pi/10
tstop = 8*np.pi
N = int(tstop/dt)
for i in range(6):
    dt /= 2.0
    N  *= 2
    S = solve(m, k, beta, S0, dt, g, w, N)
    S = np.array(S)
    tcoor = np.linspace(0, tstop, len(S))
    exact = exact_S_solution(tcoor)
    abserror = abs(exact - S)
    logerror = np.log10(abserror[1:])
    plt.plot(tcoor[1:], logerror)
    plt.xlabel('time'); plt.ylabel('log(absolute error)')
    plt.hold('on')
fig2.show()
fig2.savefig('tmp_errors_2.pdf')

fig3 = plt.figure()
dt = 2*np.pi/10
tstop = 8*np.pi
N = int(tstop/dt)
for i in range(6):
    dt /= 2.0
    N  *= 2
    S = solve(m, k, beta, S0, dt, g, w, N)
    S = np.array(S)
    tcoor = np.linspace(0, tstop, len(S))
    exact = exact_S_solution(tcoor)
    abserror = abs(exact - S)
    logerror = np.log10(abserror[1:])
    if i > 0:
        logerror_diff = logerror_prev - logerror[::2]
        plt.plot(tcoor[1::2], logerror_diff)
        plt.xlabel('time'); plt.ylabel('difference of log(absolute error)')
        plt.hold('on')
        meandiff = np.mean(logerror_diff)
        print 'average log10(abs(error)) difference: %g' % meandiff
    logerror_prev = logerror
fig3.show()
fig3.savefig('tmp_errors_3.pdf')