# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 22:45:51 2015

@author: Georg
"""

from numpy import *
import matplotlib.pyplot as plt
import matplotlib.lines as mlines 
import argparse

plt.rc('figure', figsize=(8, 6))

# Function to read acceleration data und time interval from command line
def get_input():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--f', '--file', type=str, default='0', help='input_file', metavar='f')
    parser.add_argument('--dt', '--delta_t', type=str, default='0', help='time_interval', metavar='a')
    
    args = parser.parse_args()
    
    try:
        a = loadtxt(args.f, dtype='float64', unpack=False)
        dt = eval(args.dt)
    except IndexError:
        raise IndexError("Not all arguments were provided on the command line.")
    except ValueError:
        raise ValueError("Test if you provided input data in the correct format.")
    
    return a, dt

# Function to calculate velocity from acceleration
# through integration with trapezoid rule
def velocity(acceleration, dt):
    k = acceleration.size
    t = linspace(0, k*dt, k)
    v = [0]
    summe = 0
    for j in xrange(k-1):
        summe += dt*0.5*(acceleration[j] + acceleration[j+1])
        v.append(summe)
    v = array((v), dtype='float64')
    return t, v

a, dt = get_input()
t, v = velocity(a, dt)

# Make plot
fig = plt.figure()
ax1 = fig.add_subplot(111)
line1 = ax1.plot(t, v, 'k-', label='velocity')
ax1.set_ylabel('velocity (m/s)')
ax1.set_xlim(0, 100)
ax1.set_xlabel('time (s)')

ax2 = ax1.twinx()
line2 = ax2.plot(t, a, 'b-', label='acceleration')
ax2.set_ylabel('acceleration (m/s^2)')
#ax2.yaxis.tick_right()
#ax2.yaxis.set_label_position('right')
ax2.set_xlim(0, 100)

blue_line = mlines.Line2D([], [], color='blue', markersize=15, label='acceleration')
black_line = mlines.Line2D([], [], color='black', markersize=15, label='velocity')
plt.legend(handles=[blue_line, black_line], loc='best')
plt.show()