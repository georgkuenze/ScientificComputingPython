# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 16:22:46 2015

@author: Georg
"""

import matplotlib.pyplot as plt

N  = 20                ## number of years
F  = 1.0E+6            ## fortune
x0 = F                 ## initial fortune
p  = 2.0               ## percent interest rate
q  = 50.0             ## percent of interest in first year
c0 = (p*q)/1.0E+4*F    ## consume in first yeat
I  = 1.5               ## percent iinflation
t  = 27                ## percent tax

## Simulation with tax
x = [] + [x0]
c = [] + [c0]

n = 1
xn_1 = x0
xn_2 = x0
cn = c0
cn_1 = cn

while n <= N:
    if (xn_1 - xn_2) < 0:
        xn = xn_1 + (p/100.0)*xn_1 - cn_1
    else:
        xn = xn_1 + (p/100.0)*xn_1 - cn_1 - (t/100.0)*(xn_1 - xn_2)
    x.append(xn)
    cn = cn_1 + (I/100.0)*cn_1
    c.append(cn)
    xn_2 = xn_1
    xn_1 = xn
    cn_1 = cn
    n += 1

plt.rc('figure', figsize=(8,4))

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
plt.subplots_adjust(wspace=0.3, hspace=0.0)

ax1.plot(range(N+1), x, 'r.', label='fortune')
ax1.set_xlabel('years')
ax1.set_ylabel('amount')
ax1.legend(loc=1)

ax2.plot(range(N+1), c, 'b.', label='consume')
ax2.set_xlabel('years')
ax2.set_ylabel('amount')
ax2.legend(loc=1)

plt.suptitle('Simulation with tax')


## Simulation without tax
x = [] + [x0]
c = [] + [c0]

t = 0.0
n = 1
xn_1 = x0
xn_2 = x0
cn = c0
cn_1 = cn

while n <= N:
    if (xn_1 - xn_2) < 0:
        xn = xn_1 + (p/100.0)*xn_1 - cn_1
    else:
        xn = xn_1 + (p/100.0)*xn_1 - cn_1 - (t/100.0)*(xn_1 - xn_2)
    x.append(xn)
    cn = cn_1 + (I/100.0)*cn_1
    c.append(cn)
    xn_2 = xn_1
    xn_1 = xn
    cn_1 = cn
    n += 1

plt.rc('figure', figsize=(8,4))

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
plt.subplots_adjust(wspace=0.3, hspace=0.0)

ax1.plot(range(N+1), x, 'r.', label='fortune')
ax1.set_xlabel('years')
ax1.set_ylabel('amount')
ax1.legend(loc=1)

ax2.plot(range(N+1), c, 'b.', label='consume')
ax2.set_xlabel('years')
ax2.set_ylabel('amount')
ax2.legend(loc=1)

plt.suptitle('Simulation without tax')