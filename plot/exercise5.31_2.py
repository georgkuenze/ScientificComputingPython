# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 22:41:05 2015

@author: Georg
"""

import numpy as np
import matplotlib.pyplot as plt
import time, glob, os

for filename in glob.glob('wave_*.png'):
    os.remove(filename)

def wave_packet(x, t):
    y = np.exp(-(x - 3*t)**2)*np.sin(3*np.pi*(x - t))
    return y

x = np.linspace(-6, 6, 1000)
t_min = -1
t_max =  1
t_values = np.linspace(t_min, t_max, 60)

plt.ion()
fig = plt.figure()
plt.axis([x[0], x[-1], -1, 1])
lines = plt.plot([], [])
plt.xlabel('X')
plt.ylabel('Y')

counter = 0
for t in t_values:
    y = wave_packet(x, t)
    lines[0].set_data(x, y)
    #plt.legend(['t = %4.2f' % (t)])
    plt.draw()
    plt.savefig('wave_%04d.png' % (counter))
    counter += 1
    time.sleep(0.2)