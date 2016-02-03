# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:30:53 2015

@author: Georg
"""

from numpy import *
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(8, 6))
medium = ['air', 'water']

fig = plt.figure()


for i, material in enumerate(medium):
    exec("T, d = loadtxt('density_%s.dat', dtype='float64', unpack=True)" % (material))
    
    exec("ax%s = fig.add_subplot(1, 2, %d)" % (str(i+1), i+1))
    exec("ax%s.plot(T, d, 'o', label='%s')" % (str(i+1), material))
    x = linspace(T[0], T[-1], 1000)
    
    for k in [1,2]:
        coeff = polyfit(T, d, deg=k)
        p = poly1d(coeff)
        exec("fit_%s = p(x)" % (str(k)))

        exec("ax%s.plot(x, fit_%s, '-', label='degree=%d')" % (str(i+1), str(k), k))
    exec("ax%s.legend(loc='best')" % (str(i+1)))

fig.text(0.5, 0.04, 'Temperature / degree celsius', ha='center')
fig.text(0.04, 0.5, 'Density / kg/m^3', ha='center', rotation='vertical')