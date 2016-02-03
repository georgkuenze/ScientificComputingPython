# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:34:37 2015

@author: Georg
"""

from numpy import *
import matplotlib.pyplot as plt
import sys

if len(sys.argv) < 3:
    raise IndexError("You have not provided two file names.")
if len(sys.argv) > 3:
    raise IndexError("Too many arguments provided on command line.")
for i in range(1,3):
    try:
        exec("file_name_%s = str(sys.argv[i])" % (i))
    except ValueError:
        raise ValueError("File name must be a string not %s") % (type(sys.argv[i]))
   
T_air, d_air = loadtxt(file_name_1, dtype='float64', unpack=True)
T_water, d_water = loadtxt(file_name_2, dtype='float64', unpack=True)

plt.plot(T_air, d_air, 'ko', label='Air')
plt.hold('on')
plt.plot(T_water, d_water, 'ro', label='Water')
plt.xlabel('Temperature / Degree Celsius')
plt.ylabel('Density / kg/m^3')
plt.ylim(-100, 1100)
plt.legend(loc='best')