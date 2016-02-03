# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 15:51:49 2015

@author: Georg
"""
import numpy as np
import matplotlib.pyplot as plt
import time

# Function to draw circle
def circle(radius):
    theta = np.linspace(0, 2*np.pi, 100)
    r = radius
    x = r*np.sin(theta)
    y = r*np.cos(theta)
    return x, y

# Functions to calculate Pi from the area of a circle
# which is determined by a Monte Carlo integration method
def MCint_v1(radius, n):
    a = -1*radius
    b = 1*radius
    x = np.random.uniform(a, b, n)
    y = np.random.uniform(a, b, n)
    
    # Count number of points inside circle
    inside = np.sum(x**2+y**2 <= radius**2)
    
    # Compute integral by counting points and get value of pi
    integral = inside/float(n)*(b-a)**2
    _pi = integral/float(radius)**2
    
    return _pi

def MCint_v2(radius, n):
    a = -1*radius
    b = 1*radius
    x = np.random.uniform(a, b, n)
    y = np.random.uniform(a, b, n)
    
    # Find inner and outer points
    ix1 = np.where(x**2+y**2 <= radius**2)
    x_in = x[ix1]; y_in = y[ix1]
    ix2 = np.where(x**2+y**2 > radius**2)
    x_out = x[ix2]; y_out = y[ix2]
    
    # Compute integral by counting points and get value of pi
    integral = len(x_in)/float(n)*(b-a)**2
    _pi = integral/float(radius)**2

    return _pi, x_in, y_in, x_out, y_out

def MCint_v3(radius, n, arraysize):
    a = -1*radius
    b = 1*radius    
    inside = 0
    
    rest = n % arraysize    
    batch_sizes = [arraysize] * (n//arraysize) + [rest]
    for batch_size in batch_sizes:
        x = np.random.uniform(a, b, batch_size)
        y = np.random.uniform(a, b, batch_size)
        
        # Count number of points inside circle
        inside += np.sum(x**2+y**2 <= radius**2)
        
    # Compute integral by counting points and get value of pi
    integral = inside/float(n)*(b-a)**2
    _pi = integral/float(radius)**2
    
    return _pi

# Initial Parameter
radius = 1

# Call Monte Carlo Integration function
start = time.clock()
i1, x_1, y_1, x_2, y_2 = MCint_v2(radius, 10**4)
intermediate = time.clock()
i2                     = MCint_v3(radius, 10**6, arraysize=10**4)
end = time.clock()

# Print result and make plot
print 'Method1: Integral: %.4f   Exact: %.4f   Diff.: %.4f   time: %5.1f ms' \
% (i1, np.pi, abs(i1-np.pi), (intermediate-start)*10**3)
print 'Method2: Integral: %.4f   Exact: %.4f   Diff.: %.4f   time: %5.1f ms' \
% (i2, np.pi, abs(i2-np.pi), (end-intermediate)*10**3)
fig = plt.figure()
ax = fig.add_subplot(111)
x, y = circle(radius)
ax.plot(x, y, 'b-', lw=3.0)
ax.plot(x_1, y_1, 'r.', label='inside')
ax.plot(x_2, y_2, 'k.', label='outside')
ax.legend(loc=1)