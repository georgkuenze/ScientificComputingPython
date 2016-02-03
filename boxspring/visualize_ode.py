# -*- coding: utf-8 -*-
"""
Created on Thu Oct 08 23:28:21 2015

@author: Georg
"""

from ode_project import init_prms, solve
import numpy as np
import matplotlib.pyplot as plt
import glob, os

for filename in glob.glob('tmp_*.pdf'):
    os.remove(filename)

def plot_S(S, t, step):
    if step == 0:
        return None
    
    tcoor = np.linspace(0, t, step+1)
    S = np.array(S[:len(tcoor)])
    Y = w(tcoor) - L - S - b/2
    lines[0].set_data(tcoor, Y)   
    plt.draw()

## Default values
m = 1; b = 2; L = 10; k = 1; beta = 0; S0 = 1; 
dt = 2*np.pi/40; g = 9.81; w_formula='0'; N = 200

m, b, L, k, beta, S0, dt, g, w, N = init_prms(m, b, L, k, beta, S0, dt, g, w_formula, N)

## Vectorize StringFunction w
w_formula = str(w)
if ' else ' in w_formula:
    w = np.vectorize(w)   ## General vectorization
else:
    w.vectorize(globals())

plt.ion()
lines = plt.plot(0, w(0)-L-S0-b/2.0)
plt.axis([0, dt*N, -35, -8])
plt.xlabel('time')
plt.ylabel('Y')

S = solve(m, k, beta, S0, dt, g, w, N, user_action=plot_S)

plt.savefig('tmp_Y.pdf')

tcoor = np.linspace(0, N*dt, N+1)
S     = np.array(S)

nrows = 2
if beta != 0:
    nrows += 1
if w_formula != '0':
    nrows += 1
    
fig, (axarr) = plt.subplots(nrows, sharex=True, sharey=False)

## Position Y(t)
Y = w(tcoor) - L - S - b/2.0
axarr[0].plot(tcoor, Y); axarr[0].set_xlabel('time'); axarr[0].set_ylabel('Y'); 
axarr[0].set_xlim([tcoor[0], tcoor[-1]])

## Spring Force (and S)
Fs = k*S
axarr[1].plot(tcoor, Fs); axarr[1].set_xlabel('time'); axarr[1].set_ylabel('Fs');
axarr[1].set_xlim([tcoor[0], tcoor[-1]])

## Friction Force
if beta != 0:
    Fd = beta*np.diff(S)
    ## len(diff(S)) = len(S) - 1, so we use tcoor[:-1]
    axarr[2].plot(tcoor[:-1], Fd); axarr[2].set_xlabel('time'); axarr[2].set_ylabel('Fd');
    axarr[2].set_xlim([tcoor[0], tcoor[-1]])
    
## Excitation
if w_formula != '0':
    w_array = w(tcoor)
    axarr[-1].plot(tcoor, w_array); axarr[-1].set_xlabel('time'); axarr[-1].set_ylabel('w(t)');
    axarr[-1].set_xlim([tcoor[0], tcoor[-1]])

plt.show()
plt.savefig('tmp_multi_plots.pdf')