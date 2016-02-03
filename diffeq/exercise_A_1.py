# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 13:10:11 2015

@author: Georg
"""

import numpy as np
import matplotlib.pyplot as plt

####################################################################################
## (A) Write a squence
####################################################################################

N = 100
n = np.arange(0,N,2)

a = (7 + 1/(n + 1.0))/(3 -1/(n + 1.0)**2)
aN_exact = 7.0/3.0
diff = abs(aN_exact - a[-1])

print 'Exercise (A)'
print '100-th element: %.4f, exact limit: %.4f, difference: %.4f' \
% (a[-1], aN_exact, diff)

####################################################################################
## (B) Write a function that checks for convergence
####################################################################################

def limit(seq, eps = 1.0E-14):
    convergence = True    
    counter = 1
    limit = seq[1]
    while convergence == True and counter < len(seq)-1:
        diff = abs(seq[counter-1] - seq[counter]) - abs(seq[counter] - seq[counter+1])
        if diff >= eps:
            limit = seq[counter+1]
            counter += 1
        elif eps > diff >= 0:
            limit = seq[counter+1]
            convergence = False
        elif diff < 0:
            limit = None
            convergence = False
    return limit

# Test limit() with two sequences
N = 100
n = np.arange(0,N,2)
a = (7 + 1/(n + 1.0))/(3 -1/(n + 1.0)**2)
b = np.arange(N)

print '\nExercise (B)'
print 'Limit of sequence 1: %14s\nLimit of sequence 2: %14s' % (limit(a), limit(b))

####################################################################################
## (C) Write another sequence and determine its limit
####################################################################################

def Dn_1(N):
    n = np.arange(N, dtype='float64')
    D = np.sin(2.0**-n)/2.0**-n
    return D

N = 1000
print '\nExercise (C)'
print 'Limit of sequence: %16s' % limit(Dn_1(N))

####################################################################################
## (D) Write another sequence and determine its limit
####################################################################################

def Dn_2(f, x, N):
    n = np.arange(N, dtype='float64')
    h = 2.0**-n
    D = np.zeros(len(h))
    for i in range(len(h)):
        D[i] = (f(x+h[i]) - f(x))/h[i]
    return D

f = np.sin
x = 0
N = 80
print '\nExercise (D)'
print 'Limit of sequence: %16s' % limit(Dn_2(f, x, N))
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(np.arange(N), Dn_2(f, x, N), 'ro')
ax1.set_xlabel('N')
ax1.set_ylabel('Dn')
ax1.set_title('Convergence of sequence to x=0 - Dn vs. N')

####################################################################################
## (E) Analyze sequence behaviour for x = pi
####################################################################################

def Dn_2(f, x, N):
    n = np.arange(N, dtype='float64')
    h = 2.0**-n
    D = np.zeros(len(h))
    for i in range(len(h)):
        D[i] = (f(x+h[i]) - f(x))/h[i]
    return D

f = np.sin
x = np.pi
N = 80
print '\nExercise (E)'
print 'Limit of sequence: %16s' % limit(Dn_2(f, x, N))
fig = plt.figure()
ax2 = fig.add_subplot(111)
ax2.plot(np.arange(N), Dn_2(f, x, N), 'ro')
ax2.set_xlabel('N')
ax2.set_ylabel('Dn')
ax2.set_title('Convergence of sequence to x=pi - Dn vs. N')

####################################################################################
## (F) Analyze sequence behaviour for x = pi
####################################################################################

def Dn_3(f, x, N):
    n = np.arange(N, dtype='float64')
    h = 2.0**-n
    D = np.zeros(len(h))
    Nominator   = np.zeros(len(h))
    Denominator = np.zeros(len(h))
    for i in range(len(h)):
        D[i] = (f(x+h[i]) - f(x))/h[i]
        Nominator[i] = f(x+h[i]) - f(x)
        Denominator[i] = h[i]
    return D, Nominator, Denominator
    
f = np.sin
x = np.pi
N = 80

Dn, Nom, Denom = Dn_3(f, x, N)
print ' n           Dn          Nom        Denom'
for i in range(N):
    print '%2d %12.8f %12.8f %12.8f' % (i+1, Dn[i], Nom[i], Denom[i])