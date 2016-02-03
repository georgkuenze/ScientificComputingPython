# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:04:46 2015

@author: Georg
"""

import numpy as np
import random
import matplotlib.pyplot as plt

def simulate_one_path(N, x0, p0, M, m):
    x = np.zeros(N+1)
    p = np.zeros(N+1)
    index_set = range(0,N+1)
    
    x[0] = x0; p[0] = p0
    
    for n in index_set[1:]:
        x[n] = x[n-1] + (p[n-1]/(100.0*12))*x[n-1]
        
        # Update interest rate
        r = random.randint(1,M)
        if r == 1:
            # Adjustment of gamma
            k = random.randint(1,2)
            gamma = m if k == 1 else -1*m
        else:
            gamma = 0
        
        pn = p[n-1] + gamma
        p[n] = pn if 1 <= pn <= 15 else p[n-1]
    
    return x, p

def simulate_n_paths(n, N, L, p0, M, m):
    # Arrays which holds the sum/average of n times paths
    xm = np.zeros(N+1)
    pm = np.zeros(N+1)
    # Arrays which holds the standard deviation
    xs = np.zeros(N+1)
    ps = np.zeros(N+1)
    # 2D-Arrays that hold five sample paths
    x_sample = np.zeros((5, N+1))
    p_sample = np.zeros((5, N+1))
    
    for i in range(n):
        x, p = simulate_one_path(N, L, p0, M, m)
        # Accumulate paths
        xm += x
        pm += p
        xs += x**2
        ps += p**2
        
        # Show 5 random paths
        if i % (n/5) == 0:
            x_sample[(i*5)//n] = x
            p_sample[(i*5)//n] = p
            
    # Compute average
    xm /= float(n)
    pm /= float(n)
    # Compute Variance
    xs = xs/float(n) - xm**2
    ps = ps/float(n) - pm**2
    # Remove all negative numbers (round off errors)
    xs[xs < 0] = 0
    ps[ps < 0] = 0
    # Compute standard deviation
    xs = np.sqrt(xs)
    ps = np.sqrt(ps)
    
    return xm, xs, x_sample, pm, ps, p_sample

# Initial parameter
x0 = 1         # initial investment
p0 = 5         # initial interest rate
N  = 10*12     # number of months
M  = 3         # p changes (on average) every M months
n  = 1000      # number of simulations
m  = 0.5       # adjustment of p

# Call function
xm, xs, x_sample, pm, ps, p_sample = simulate_n_paths(n, N, x0, p0, M, m)
months = np.arange(len(xm))

# Make plot
plt.rc('figure', figsize=(10,10))
fig = plt.figure()
plt.subplots_adjust(wspace=0.2, hspace=0.2)

ax1 = fig.add_subplot(221)
ax1.plot(months, xm, 'b-', months, xm+xs, 'r--', months, xm-xs, 'r--')
ax1.set_xticks([0,20,40,60,80,100,120])
ax1.set_title('Mean +/- 1st STD of investment')

ax2 = fig.add_subplot(222)
ax2.plot(months, pm, 'b-', months, pm+ps, 'r--', months, pm-ps, 'r--')
ax2.set_xticks([0,20,40,60,80,100,120])
ax2.set_title('Mean +/- 1st STD of interest rate')

ax3 = fig.add_subplot(223)
for i in range(5):
    ax3.plot(months, x_sample[i])
ax3.set_xticks([0,20,40,60,80,100,120])
ax3.set_title('Sample paths of investment')

ax4 = fig.add_subplot(224)
for i in range(5):
    ax4.plot(months, p_sample[i])
ax4.set_xticks([0,20,40,60,80,100,120])
ax4.set_title('Sample paths of interest rate')