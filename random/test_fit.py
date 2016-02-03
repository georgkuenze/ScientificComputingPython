# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:17:25 2015

@author: Georg
"""

import numpy as np
import scipy

def residuals(p, y, x):
    c = p
    err = y - c/np.sqrt(x)
    return err

p = (70.0)
x = np.array([0.1, 100, 200, 300, 400, 800], dtype='float64')
y = np.array([3, 0.75, 0.25, 0.2, 0.2, 0.1], dtype='float64')

plsq = scipy.optimize.leastsq(residuals, p, args=(y,x))

print plsq