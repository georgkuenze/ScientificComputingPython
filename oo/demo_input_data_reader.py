# -*- coding: utf-8 -*-
"""
Created on Mon Sep 07 13:48:53 2015

@author: Georg
"""
import sys
import numpy as np
from scitools.StringFunction import StringFunction
from input_data_reader import *

p = dict(formula='x+1', a=0, b=1, n=2, filename='tmp.dat')

input_reader = eval(sys.argv[1])
del sys.argv[1]   # otherwise argparse don't like our extra options ...

inp = input_reader(p)
a, b, filename, formula, n = inp.get_all()
print inp

f = StringFunction(formula)
with open(filename, 'w') as outfile:
    for x in np.linspace(a,b,n):
        outfile.write('%12g %12g\n' % (x,f(x)))