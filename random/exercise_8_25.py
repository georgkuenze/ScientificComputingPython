# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 11:56:18 2015

@author: Georg
"""

import random

def find_number_v1(number, p, q):
    attempts = 0
    guess = 0
    while guess != number:
        guess = random.randint(p,q)
        attempts += 1
        if guess == number:
            #print 'Correct number found after %d attempts.' % (attempts)
            break
        elif guess < number:
            p = guess + 1
        else:
            q = guess - 1
    return attempts

def find_number_v2(number, p, q):
    attempts = 0
    guess = 0
    while guess != number:
        guess = int(round((q-p)/2.0+p))
        attempts += 1
        if guess == number:
            #print 'Correct number found after %d attempts.' % (attempts)
            break
        elif guess < number:
            p = guess + 1
        else:
            q = guess - 1
    return attempts

# Parameter for game
p = 1; q = 100                 # initial interval
number = random.randint(p,q)   # random number to guess
N = 10**6                      # number of trials the game is played

M1 = 0; M2 = 0                 # average value of attempts in both game versions
for i in xrange(N):
    M1 += find_number_v1(number, p=1, q=100)
    M2 += find_number_v2(number, p=1, q=100)
M1 /=float(N)
M2 /=float(N)
print 'Average value of attempts:\nVersion1 (Random guess): %.2f   Version2 (bisecting interval): %.2f' % (M1, M2)       