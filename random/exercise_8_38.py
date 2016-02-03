# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:17:31 2015

@author: Georg
"""
import random

def simulate(m, n, p, q, b):
    capital = 0
    correct = 0
    for i in range(n):
        capital -= p
        r = random.random()
        if r <= b:
            capital += q
            correct += 1
    return capital, correct

# Parameter
m = n = 4
p = 3
q = 6
b = 0.5 #1/float(m)

N = 10**6
money = 0; correct = 0
for i in xrange(N):
    m, c = simulate(m, n, p, q, b)
    money += m
    correct += c

av_money = money/float(N)
av_correct = correct/(float(N)*4)

print 'Average money earned: %.2f. Average probability of getting full score: %.2f.' \
% (av_money, av_correct) 