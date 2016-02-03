# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 23:11:01 2015

@author: Georg
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

x = np.arange(11)
y = x/(0.5+x)

#f = interpolate.interp1d(x, y, kind='cubic')

x_new = np.arange(0, 10.1, 0.1)
#y_new = f(x_new)
tck = interpolate.splrep(x,y)
y_new = interpolate.splev(x_new, tck, der=0)

plt.plot(x,y, 'bo')
plt.hold('on')
plt.plot(x_new, y_new, 'r.')
plt.show()