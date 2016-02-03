# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 17:27:27 2015

@author: Georg
"""
import numpy as np
import matplotlib.pyplot as plt
import glob, os

for filename in glob.glob('t_earth_*.png'):
    os.remove(filename)

def temp_func(z, t, T0, A, alpha, omega):
    T = T0 + A*np.exp(-alpha*z)*np.cos(omega*t - alpha*z)
    return T

# Parameter for function
hours = 24                      # time period in hours
omega = 2*np.pi/(hours*60*60)   # frequency in s**-1
T0    = 10                      # mean temperature in degree celsius
A     = 10                      # max. temperature variation in degree celsius 
k     = 1.0e-6                  # heat conduction coefficient in m**2/s

alpha = np.sqrt(omega/(2.0*k))

# Initialize depth and time values
z_max = -(1/alpha)*np.log(0.0001)   # maximal depth in m at which T is decraesed to 0.001
z = np.linspace(0,z_max,100)
t_max = 24                         # total time 24 hours
t = np.arange(t_max)

plt.ion()
lines = [plt.plot([],[], lw=2)[0] for _ in range(len(t))]
plt.axis([z[0], z[-1], T0-A, T0+A])
plt.xlabel('depth / m')
plt.ylabel('T / degree celsius')

counter = 0
for i in range(0,len(t),2):
    T = temp_func(z, t[i]*3600, T0, A, alpha, omega)
    lines[i].set_data(z,T)
    lines[i].set_label('t = %d h' % (t[i]))
    plt.legend(loc=1)
    plt.draw()
    plt.savefig('t_earth_%04d.png' % (counter))
    plt.pause(0.5)
    counter += 1