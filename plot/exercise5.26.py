# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 23:00:38 2015

@author: Georg
"""

from numpy import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

x = linspace(-4, 4, 500)
t = linspace(0, 4, 500)

xv, tv = meshgrid(x, t)

zv = exp(-(xv - 3*tv)**2)*sin(3*pi*(xv - tv))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xv, tv, zv, rstride=8, cstride=8, cmap=plt.cm.hsv)

ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('z')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, exp(-(x)**2)*sin(3*pi*(x)), 'r-')