# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 09:12:25 2015

@author: Georg
"""
import numpy as np
import matplotlib.pyplot as plt
import glob, os

for filename in glob.glob('tmp_*.png'):
    os.remove(filename)

def Gauss(x, m, s):
    s = float(s)
    return (1.0/(np.sqrt(2*np.pi)*s))*np.exp(-0.5*((x-m)/s)**2)

m = 0
s_min = 0.2
s_max = 2.0
x = np.linspace(m - 3*s_max, m + 3*s_max, 1000)
s_values = np.linspace(s_min, s_max, 10)
max_f = Gauss(m, m, s_min)

plt.ion()
y = Gauss(x, m, s_max)
lines = [plt.plot([],[], lw=2)[0] for _ in range(len(s_values))]
plt.axis([x[0], x[-1], 0, max_f])
plt.xlabel('x')
plt.ylabel('f(x)')

counter = 0
for i in range(len(s_values)):
    y = Gauss(x, m, s_values[i])
    lines[i].set_data(x,y)
    lines[i].set_label('s = %4.2f' % (s_values[i]))
    plt.legend(loc='best')
    plt.draw()
    plt.savefig('tmp_%04d.png' % (counter))
    plt.pause(1)
    counter += 1