# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 15:01:10 2015

@author: Georg
"""

import numpy as np
import matplotlib.pyplot as plt

L  = 1000       ## loan
x0 = L          ## initial amount of loan
N  = 24         ## number of months
p  = 4          ## interest rate
y0 = L/float(N) ## payback first month

index_list = range(N+1)
x = np.zeros(len(index_list))
x[0] = x0
y = np.zeros(len(index_list))
y[0] = y0

for n in index_list[1:]:
    y[n] = (p/1200.0)*x[n-1] + L/float(N)
    x[n] = x[n-1] + (p/1200.0)*x[n-1] - y[n]

plt.rc('figure', figsize=(8,4))

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
plt.subplots_adjust(wspace=0.3, hspace=0.0)

ax1.plot(index_list, x, 'r.', label='loan')
ax1.set_xlabel('months')
ax1.set_ylabel('amount')
ax1.legend(loc=1)

ax2.plot(index_list, y, 'b.', label='payback')
ax2.set_xlabel('months')
ax2.set_ylabel('amount')
ax2.legend(loc=1)