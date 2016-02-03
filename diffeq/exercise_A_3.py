# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 23:43:34 2015

@author: Georg
"""

import datetime, glob, os
import numpy as np
import matplotlib.pyplot as plt

x0 = 100                         ## initial amount
p = 5                            ## annual growth rate
r = p/360.0                      ## daily growth rate

date1 = datetime.date(2007, 8, 3)
date2 = datetime.date(2011, 8, 3)
diff = date2 - date1
N = diff.days

## Version 1 with index list and array to store x
index_set = range(N+1)
x = np.zeros(len(index_set))

x[0] = x0
for n in index_set[1:]:
    x[n] = x[n-1] + (r/100.0)*x[n-1]

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(index_set, x, 'r.')
ax1.set_xlabel('days')
ax1.set_ylabel('amount money')


## Version 2 with while loop and days counter
## Series is written to file
m = [] + [x0]
days = [] + [0]
x_n_1 = x0 
counter = 0
for filename in glob.glob('exercise_A.5.txt'):
    os.remove(filename)

outfile = open('exercise_A.5.txt', 'w')
outfile.write(" Days     Money\n---------------\n    0   %7.3f\n" % x0)
while counter <= N:
    counter += 1
    days.append(counter)
    x_n = x_n_1 + (r/100.0)*x_n_1
    m.append(x_n)
    outfile.write("%5d   %7.3f\n" % (counter, x_n))
    x_n_1 = x_n
    
outfile.close()

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.plot(days, m, 'b.')
ax2.set_xlabel('days')
ax2.set_ylabel('amount money')    