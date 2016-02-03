# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 15:57:28 2015

@author: Georg
"""

import numpy as np
import matplotlib.pyplot as plt

N  = 20                ## number of years
F  = 1.0E+6            ## fortune
x0 = F                 ## initial fortune
p  = 2.0               ## percent interest rate
q  = 200.0             ## percent of interest in first year
c0 = (p*q)/1.0E+4*F    ## consume in first yeat
I  = 1.5               ## percent iinflation

index_list = range(N)
x = np.zeros(len(index_list))
x[0] = x0
c = np.zeros_like(x)
c[0] = c0

for n in index_list[1:]:
    x[n] = x[n-1] + (p/100.0)*x[n-1] - c[n-1]
    c[n] = c[n-1] + (I/100.0)*c[n-1]

plt.rc('figure', figsize=(8,4))

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
plt.subplots_adjust(wspace=0.3, hspace=0.0)

ax1.plot(index_list, x, 'r.', label='fortune')
ax1.set_xlabel('years')
ax1.set_ylabel('amount')
ax1.legend(loc=1)

ax2.plot(index_list, c, 'b.', label='consume')
ax2.set_xlabel('years')
ax2.set_ylabel('amount')
ax2.legend(loc=1)