# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 23:03:20 2015

@author: Georg
"""

import numpy as np
import matplotlib.pyplot as plt
import glob, os

for filename in glob.glob('heaviside_*.png'):
    os.remove(filename)

def s_H(x, e):
    condition1 = x < -1*e
    condition2 = np.logical_and(-1*e <= x, x <= e)
    condition3 = x > e
    
    r = np.where(condition1, 0.0, 0.0)
    r = np.where(condition2, 0.5+(x/(2.0*e)) + 0.5*(1/np.pi)*np.sin(np.pi*x/float(e)), r)
    r = np.where(condition3, 1, r)
    return r

x = np.linspace(-2.5, 2.5, 1000)
e_min = 0
e_max = 2
e_values = np.linspace(e_min, e_max, 10)

plt.ion()
lines = [plt.plot([],[], lw=2)[0] for _ in range(len(e_values))]
plt.axis([x[0], x[-1], -0.1, 1.1])
plt.xlabel('x')
plt.ylabel('f(x)')

counter = 0
for i in range(len(e_values)):
    y = s_H(x, e_values[i])
    lines[i].set_data(x,y)
    lines[i].set_label('e = %4.2f' % (e_values[i]))
    plt.legend(loc='best')
    plt.draw()
    plt.savefig('heaviside_%04d.png' % (counter))
    plt.pause(0.5)
    counter += 1