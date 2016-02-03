# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 12:23:36 2015

@author: Georg
"""

import numpy as np
import matplotlib.pyplot as plt
import time, glob, os

for filename in glob.glob('orbit_*.png'):
    os.remove(filename)

# Define function to calculate a planet's orbit 
def orbit(omega, n, k, a, b):
    # time interval
    delta_t = 2*np.pi/(omega*n)
    
    # Calculate path of planet after k*delta_t time steps
    # and its velocity at tmax i.e. the outermost time
    # point of the increment
    if k == 0:
        t = 0
        t_max = 0
    else:
        steps = np.arange(k*n)
        t = steps * delta_t
        t_max = t.max()     # Position of planet and end of time increment
        
    x = a*np.cos(omega*t)   # a is semi-major axis of the ellipse
    y = b*np.sin(omega*t)   # b is semi-minor axis of the ellipse
    
    v = omega*np.sqrt((a*np.sin(omega*t_max))**2 + (b*np.cos(omega*t_max))**2)
    
    return x, y, v, t_max

# Define parameter
omega = 2*np.pi/365   # angular frequency
n = 1000              # number of time inervals
a = 2                 # semi-major axis of ellipse
b = 1                 # semi-minor axis of ellipse
inc = 50              # number of increments to be shown

plt.ion()
fig = plt.figure()
plt.axis([-1.1*a, 1.1*a, -1.1*b, 1.1*b])

# Create line object, returns a list of graphs
lines = plt.plot([],[], [],[])
lines[0].set_ls('-')
lines[0].set_color('k')
lines[1].set_marker('o')
lines[1].set_color('r')

plt.xlabel('X')
plt.ylabel('Y')

# Loop over increments to calculate the planet's orbit
# update x and y values and print velocity
counter = 0
for i in range(inc+1):
    k = float(i)/inc
    x, y, v, t_max = orbit(omega, n, k, a, b)
    # Update x,y data for 2nd graph i.e. lines[1]
    lines[0].set_data(x, y)
    lines[1].set_data(a*np.cos(omega*t_max), b*np.sin(omega*t_max))
    lines[1].set_label('velocity = %.2e rad/year' % (v))
    plt.legend()
    plt.draw()
    plt.savefig('orbit_%04d.png' % (counter))
    counter += 1
    time.sleep(0.2)