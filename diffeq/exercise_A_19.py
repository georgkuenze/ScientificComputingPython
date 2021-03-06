# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 18:45:45 2015

@author: Georg
"""
import numpy as np
import matplotlib.pyplot as plt
import sys, os, glob

for plotfile in glob.glob('logistic_y0_*.png'):
    os.remove(plotfile)

def logistic(y0, N, q):
    y = np.zeros(N+1)
    index_set = range(N+1)
    y[0] = y0
    for n in index_set[1:]:
        y[n] = y[n-1] + q*y[n-1]*(1-y[n-1])
    return y

def make_plot(y):
    plt.plot(range(len(y)), y, 'b-')
    plt.xlabel('N')
    plt.ylim(0, 1.1)
    plt.title('Logistic Growth for y0 = %.2f and q = %.2f' \
    % (y[0], (y[1]-y[0])/(y[0]*(1-y[0]))))
    plt.savefig('logistic_y0_%.2f_q_%.1f_N_%d.png' \
    % (y[0], (y[1]-y[0])/(y[0]*(1-y[0])), len(y)))

def read_input():
    try:
        y0 = float(sys.argv[1])
        q  = float(sys.argv[2])
        N  = int(sys.argv[3])
    except:
        raise IndexError('Usage %s: y0 q N' % sys.argv[0])
    return y0, q, N

y0, q, N = read_input()
y = logistic(y0, N, q)
make_plot(y)