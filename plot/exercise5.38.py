# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 15:05:43 2015

@author: Georg
"""

import numpy as np
from math import factorial
import matplotlib.pyplot as plt
import time, glob, os

for filename in glob.glob('velocity_*.png'):
    os.remove(filename)

# Define function for radial velocity across a pipeline
def velocity(R, beta, my, n):
    # R = radius
    # beta = pressure gradient
    # my = viscosity coefficient
    # n = 1 for water, air, n < 1 for plastic

    x = np.linspace(0, R, 100)
    v = (beta/(2*my))**(1.0/n) * (n/(n+1.0)) * (R**(1+1.0/n) - x**(1+1.0/n))
    v /= v[0]
    return v, x

# Define parameter
R = 1
beta = 0.02
my = 0.02
n = [10**k for k in np.linspace(0,-2,11)]

plt.ion()
lines = [plt.plot([],[], lw=2)[0] for _ in range(len(n))]
plt.axis([0, R, 0, 1.1])
plt.xlabel('r')
plt.ylabel('norm. v(r)')

counter = 0
for i in range(len(n)):
    v, r = velocity(R, beta, my, n[i])
    lines[i].set_data(r,v)
    lines[i].set_label('n = %4.2e' % (n[i]))
    plt.legend(bbox_to_anchor=(0.03,0.75), loc=2)
    plt.draw()
    plt.savefig('velocity_%04d.png' % (counter))
    plt.pause(0.5)
    counter += 1