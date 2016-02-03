# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 22:59:57 2015

@author: Georg
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

def f(t, T):
    return np.piecewise(t, [t < 0.5*T, t == 0.5*T, t > 0.5*T], [1, 0, -1])

def S(t, n, T):
    summe = 0    
    for i in range(1, n+1):
        summe += 4/np.pi*(1/(2.*i-1))*np.sin((2*(2*i-1)*np.pi*t)/float(T))
    return summe

# Calculate sigma function for three different ranges
T = [0.01*2*np.pi, 0.25*2*np.pi, 0.49*2*np.pi]
labels = []
for i in range(len(T)):
    labels.append("T = " + str(round(T[i], 2)))

elist = [np.zeros(1000, dtype='float') for i in xrange(len(T))]
x_list = np.rec.array(elist, names=labels)
y_list = np.rec.array(elist, names=labels)

for i, name in zip(range(len(T)), labels):
    x = np.linspace(0, T[i], 1000)
    x_list[name ] = x
    y = f(x, T[i])
    y_list[name] = y

# Make plot of sigma function
fig = plt.figure()
ax = fig.add_subplot(111)
color = iter(cm.rainbow(np.linspace(0,1,len(T))))
for i, name in zip(range(len(T)), labels):
    c=next(color)
    ax.plot(x_list[name], y_list[name], color=c, ls='-', lw=2, label=name)
ax.legend(loc='best')
ax.set_ylim(-1.4, 1.4)

# Calculate sigma function with approximation
n = [1,3,5,10,30,100, 1000]
T = 0.49*2*np.pi
labels = []
for i in range(len(n)):
    labels.append("n = " + str(n[i]))

elist = [np.zeros(1000, dtype='float') for i in xrange(len(n))]
y_list = np.rec.array(elist, names=labels)

for i, name in zip(range(len(n)), labels):
    x = np.linspace(0, T, 1000)
    y = S(x, n[i], T)
    y_list[name] = y

# Make plot of sigma function approximation
fig = plt.figure()
ax = fig.add_subplot(111)
color = iter(cm.rainbow(np.linspace(0,1,len(n))))
for i, name in zip(range(len(n)), labels):
    c=next(color)
    ax.plot(x, y_list[name], color=c, ls='-', lw=2, label=name)
ax.legend(loc='best')
ax.set_ylim(-1.4, 1.4)