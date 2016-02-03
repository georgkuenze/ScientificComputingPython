# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 10:01:16 2015

@author: Georg
"""

import numpy as np
import matplotlib.pyplot as plt
import time, glob, os

for filename in glob.glob('pi_*.png'):
    os.remove(filename)

# Define Function for approximation of pi
def approx_pi(n):
    points = np.arange(n+1)
    x = 0.5*np.cos(2*np.pi*(points/float(n)))
    y = 0.5*np.sin(2*np.pi*(points/float(n)))
    
    edge = np.zeros(n, dtype='float64')
    for i in range(n):
        edge[i] = np.sqrt((x[i+1]-x[i])**2 + (y[i+1]-y[i])**2)
    L = np.sum(edge)
    error = abs(np.pi - L)        
        
    return x, y, L, error

# Create an array of n-values
n_values = np.array([2**k for k in range(2,11)])

# x and y values for drawing a circle
x_val_circle = 0.5*np.cos(2*np.pi*(np.arange(2049)/float(2048)))
y_val_circle = 0.5*np.sin(2*np.pi*(np.arange(2049)/float(2048)))

plt.ion()
fig = plt.figure()
plt.axis([-0.6, 0.6, -0.6, 0.6])

# Create line object, returns a list of graphs
lines = plt.plot(x_val_circle, y_val_circle, [],[])

# Set line object properties
lines[0].set_lw(2.0)
lines[0].set_ls('-')
lines[0].set_color('b')
lines[1].set_marker('o')
lines[1].set_color('r')

plt.xlabel('X')
plt.ylabel('Y')

# Loop over n-values to calculate pi-approximation function
# and update x and y values
counter = 0
for n in n_values:
    x, y, L, err = approx_pi(n)
    # Update x,y data for 2nd graph i.e. lines[1]
    lines[1].set_data(x, y)
    lines[1].set_label('n = %4d \nerror = %.5e' % (n, err))
    plt.legend()
    plt.draw()
    plt.savefig('pi_%04d.png' % (counter))
    counter += 1
    time.sleep(0.2)