# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 17:01:51 2015

@author: Georg
"""

import datetime
import numpy as np
import matplotlib.pyplot as plt

## Conversion of dates as strings into datetime objects
datefmt   = '%Y,%m,%d'
dates     = ['2019,01,04', '2019,03,21', '2019,04,01', '2019,06,30', '2019,11,01', '2020,04,01']
end_date  = '2020,12,31'   ## end date
dates     += [end_date]

date_list = [datetime.datetime.strptime(date_, datefmt).date() for date_ in dates]
p_list    = [4.5, 4.75, 6.0, 5.0, 4.5, 2.0]   ## list of p-vales

diff  = date_list[-1] - date_list[0]
N     = diff.days

## Creation of an array of p-values
p = np.zeros(N)

end_ix = -1
for i in range(len(p_list)):
    diff     = (date_list[i+1] - date_list[i]).days
    start_ix = end_ix + 1
    end_ix   = start_ix + diff - 1
    for k in range(start_ix, end_ix+1):
        p[k] = p_list[i]

## Calculate the capital growth from difference equation
index_set = range(N+1)
x = np.zeros(len(index_set))
x0 = 100                         ## initial amount

x[0] = x0
for n in index_set[1:]:
    x[n] = x[n-1] + (p[n-1]/(3.6E+5))*x[n-1]


## plot capital and interest rate vs. days
plt.rc('figure', figsize=(8,4))

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
plt.subplots_adjust(wspace=0.3, hspace=0.0)

ax1.plot(index_set, x, 'r.', label='capital')
ax1.set_xlabel('days')
ax1.set_ylabel('amount')
ax1.legend(loc=4)

ax2.plot(range(N), p, 'b-', label='interest rate')
ax2.set_xlabel('days'); ax2.set_ylabel('p')
ax2.set_xlim(0, len(p)); ax2.set_ylim((0, max(p)+1))
ax2.legend(loc=4)

plt.suptitle('Capital Growth with variable p')