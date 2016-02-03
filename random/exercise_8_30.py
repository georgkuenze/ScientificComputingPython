# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 20:30:10 2015

@author: Georg
"""

import random, time, sys
import matplotlib.pyplot as plt
import numpy
from math import sqrt

# Input parameter
np = int(sys.argv[1])   # number of particles
ns = int(sys.argv[2])   # number of steps
p  = float(sys.argv[3]) # probability for step to the right

probabilities = [p, 1-p]
positions = numpy.zeros(np)
y = numpy.zeros(np)

# Initialize plot
plt.ion()
lines = [plt.plot([],[])[0] for _ in range(ns)]
plt.axis([-5*sqrt(ns), 5*sqrt(ns), -0.2, 0.2])
plt.xlabel('x')
plt.ylabel('f(x)')

random.seed(3) # Set random seed
for j in range(ns):
    for i in range(np):
        r = random.random()
        if r <= p:
            positions[i] += 1
        else:
            positions[i] -= 1
    lines[j].set_data(positions, y)
    lines[j].set_linestyle('None')
    lines[j].set_marker('o')
    lines[j].set_color('blue')
    plt.draw()
    #plt.pause(0.1)
# plt.show(block=True) # Use this option when invoking the program from the terminal

random.seed(3) # Set the same random seed as in loop for plotting
positions = numpy.zeros((np,ns+1))
for j in range(1,ns+1):
    for i in range(np):
        r = random.random()
        if r <= p:
            positions[i][j] = positions[i][j-1] + 1
        else:
            positions[i][j] = positions[i][j-1] - 1

# Calculate average position of particles after ns steps
s = 0
for row in range(np):
    s += numpy.mean(positions[row][1:])
mean = s/float(np)
mean_theory = p*ns-(1-p)*ns # Theoretical value for average position

print 'Average position of %d particles after %d steps is %.3f.\nTheoretical value is %.3f.' \
% (np, ns, mean, mean_theory)