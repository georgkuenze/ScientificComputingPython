# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:39:53 2015

@author: Georg
"""

import numpy as np
import random
import matplotlib.pyplot as plt

def simulate_one_path(N, T, x0, mu, sigma):
    d_t = T/float(N)
    x = np.zeros(N+1)
    index_range = range(0, N+1)
    r = np.random.normal(0,1,N)   # Array of normal distributed random numbers
    
    x[0] = x0
    
    for n in index_range[1:]:
        x[n] = x[n-1] + d_t*mu*x[n-1] + sigma*x[n-1]*np.sqrt(d_t)*r[n-1]
    
    return x

def simulate_n_paths(n, N, T, x0, mu, sigma):
    # Arrays which holds the sum/average of n times paths
    xm = np.zeros(N+1)
    # Arrays which holds the standard deviation
    xs = np.zeros(N+1)
    # 2D-Arrays that hold five sample paths
    x_sample = np.zeros((5, N+1))
    
    for i in range(n):
        x = simulate_one_path(N, T, x0, mu, sigma)
        # Accumulate paths
        xm += x
        xs += x**2
        
        # Show 5 random paths
        if i % (n/5) == 0:
            x_sample[(5*i)//n] = x
    
    # Compute average
    xm /= float(n)
    # Compute Variance
    xs = xs/float(n) - xm**2
    # Remove all negative numbers (round off errors)
    xs[xs < 0] = 0
    # Compute standard deviation
    xs = np.sqrt(xs)
    
    return xm, xs, x_sample
        
# Initial parameter
n     = 1000   # number of simulations
N     = 5000   # steps
T     = 180    # days
x0    = 5      # initial stock price
mu    = 0.01   # growth rate
sigma = 0.02   # volatility of stock price

xm, xs, x_sample = simulate_n_paths(n, N, T, x0, mu, sigma)
time = np.linspace(0,180,len(xm))

plt.rc('figure', figsize=(10,6))
fig = plt.figure()
plt.subplots_adjust(wspace=0.15)

ax1 = fig.add_subplot(121)
ax1.plot(time, xm, 'b-', time, xm+xs, 'r--', time, xm-xs, 'r--')
ax1.set_xticks([0,20,40,60,80,100,120,140,160,180])
ax1.set_title('Mean +/- 1st STD of stock price')

ax2 = fig.add_subplot(122)
for i in range(5):
    ax2.plot(time, x_sample[i])
ax2.set_xticks([0,20,40,60,80,100,120,140,160,180])
ax2.set_title('Sample paths of stock price')