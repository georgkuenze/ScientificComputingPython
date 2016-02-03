# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 23:25:05 2015

@author: Georg
"""

from numpy import *
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(9, 6))

g = 9.81    # m/s^2
s = 7.9e-2  # N/m
rho = 1000  # kg/m^3
h = 50      # m

lambda1 = linspace(0.001, 0.1, 1000)
lambda2 = linspace(1, 1000, 1000)

c1 = sqrt(((g*lambda1)/(2*pi))*(1 + s*((4*pi**2)/(rho*g*lambda1**2)))*tanh((2*pi*h)/lambda1))
c2 = sqrt(((g*lambda2)/(2*pi))*(1 + s*((4*pi**2)/(rho*g*lambda2**2)))*tanh((2*pi*h)/lambda2))

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.plot(lambda1, c1)
ax1.set_xlim(min(lambda1), max(lambda1))
ax2 = fig.add_subplot(122)
ax2.plot(lambda2, c2)
ax2.set_xlim(min(lambda2), max(lambda2))

fig.text(0.5, 0.04, 'wave length (m)', ha='center')
fig.text(0.08, 0.5, 'wave speed (m/s)', ha='center', rotation='vertical')
fig.text(0.5, 0.95, 'Wave speed at depth of 50m', ha='center')