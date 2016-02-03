# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:15:16 2015

@author: Georg
"""

import numpy as np
import math as m

def v_func(x, mu=1E-6, exp = m.exp):
    nom = (1-exp(x/mu))
    denom = (1-exp(1/mu))
    v = nom/denom
    return v, nom, denom

print "%12s; %12s; %12s\n%s" %('v', 'nominator', 'deominator', 40*'-')
for i in [(a*0.1) for a in range(11)]:
    for j in [m.exp, np.exp]:
        v, nom, denom = v_func(i, mu=1E-2, exp=j)
        print "%12.5e; %12.5e, %12.5e" %(v, nom, denom)

x = np.linspace(0,1,10000, dtype='float64')
mu = np.array([1, 0.1, 0.01, 0.001], dtype='float64')
for l in mu:
    v, nom, denom = v_func(x, mu=l, exp=np.exp)
    plt.plot(x, v, lw=2, label='mu = %5.3f' % (l))
    plt.legend(loc='best')