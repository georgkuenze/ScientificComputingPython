# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 17:51:38 2015

@author: Georg
"""

import numpy as np
import random
import matplotlib.pyplot as plt
from scipy import optimize

def simulate_one_path(T, S0, r, sigma):
    S = np.zeros(T+1)
    index_range = range(T+1)
    epsilon = np.random.normal(0,1,T)   # Array of normal distributed random numbers
    S[0] = S0
    
    for n in index_range[1:]:
        S[n] = (1-r)*S[n-1] + sigma*S[n-1]*epsilon[n-1]
    
    return S

def asian_option_N_paths(N, K, T, S0, r, sigma):
    # Array that holds the Asian option price over N simulations    
    option_N = np.zeros(N)
    
    option = 0
    for i in range(N):
        S = simulate_one_path(T, S0, r, sigma)
        Sm = np.mean(S) # Mean stock price during T days
        option += max(Sm-K, 0)*(1.0/((1+r)**T))
        option_N[i] = option/float(i+1)
    
    return option_N
    
# Initial parameter
N     = 1000     # Number of simulations
S0    = 100      # stock price at day = 0
T     = 100      # days
r     = 0.0002   # daily interest rate
sigma = 0.015    # volatility
K     = 102      # strike price

# Call function to calculate Asian option price in N number of simulations
option_price = asian_option_N_paths(N, K, T, S0, r, sigma)
option_price_err = np.absolute(option_price-option_price[-1]) # Error of option price
N_array = np.arange(len(option_price))                        # converges to zero when N increases

# Fit Curve error vs. N (error improves with 1/sqrt(N))
def residuals(p, y, x):
    c = p
    err = y - c/np.sqrt(x)
    return err
p0 = [100.0] # Initial guess of fit parameter

# Least-Squares fitting
plsq = optimize.leastsq(residuals, p0, args=(option_price_err[1:], N_array[1:]))
constant = plsq[0][0]

plt.rc('figure', figsize=(10,8))
fig = plt.figure()
plt.subplots_adjust(hspace=0.3)

ax1 = fig.add_subplot(211)
ax1.plot(N_array, option_price, lw=2.0)
ax1.set_xlabel('No. Simulations')
ax1.set_ylabel('Asian option price')
ax1.set_title('Asian option price vs. No simulations')

ax2 = fig.add_subplot(212)
ax2.plot(N_array, option_price_err, N_array[1:], constant/np.sqrt(N_array[1:]), 'r-', lw=2.0)
ax2.set_xlabel('No. Simulations')
ax2.set_ylabel('Error')
ax2.set_title('Error in Asian option price')

print 'Fit to curve: y = %.2f/sqrt(x).' % constant