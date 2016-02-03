# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 17:17:56 2015

@author: Georg
"""

import random, sys
from math import sqrt
import numpy as np
from collections import OrderedDict

# Functions
def draw(hat):
    color = random.choice(hat)
    hat.remove(color)
    return color, hat

def option1(balls):   # 60 Euros
    if balls.count('red') == 3:
        return 1
    else:
        return 0
        
def option2(balls):   # 7+5*sqrt(len(balls))
    if balls.count('brown') >= 3:
        return 1
    else:
        return 0
    
def option3(balls):   # len(balls)**3 - 26
    if balls.count('yellow') == 1 and balls.count('brown') == 1:
        return 1
    else:
        return 0
        
def option4(balls):   # 23
    if all(color in balls for color in colors):
        return 1
    else:
        return 0

# setup parameter
colors = 'red', 'yellow', 'green', 'brown'
hat = []
hat += 5*['red']
hat += 5*['yellow']
hat += 3*['green']
hat += 7*['brown']

no_balls = int(sys.argv[1])
N = int(sys.argv[2])

# Loop over a large number of test experiments
success = np.zeros((4,N))
for i in range(N):
    balls = []

    for j in range(no_balls):
        color, hat = draw(hat)
        balls.append(color)
    
    success[0,i] = option1(balls)
    success[1,i] = option2(balls)
    success[2,i] = option3(balls)
    success[3,i] = option4(balls)
    
    hat += [balls.pop() for i in range(len(balls))]

# Calculate winning probability and capital
probabilities = OrderedDict()
for i in range(4):
    counts = np.sum(success[i])
    probabilities[i+1] = counts/float(N)

capital = OrderedDict()
capital[1] = probabilities[1] * 60 - 2*no_balls
capital[2] = probabilities[2] * (7+5*sqrt(no_balls)) - 2*no_balls
capital[3] = probabilities[3] * (no_balls**3 - 26) - 2*no_balls
capital[4] = probabilities[4] * 23 - 2*no_balls

print 'Result - Draw balls from the hat\n'
print 'Option    Probability    Capital  \n%s' % (34*'-')
for i in range(1,5):
    print '  %d        %8.5f     %9.5f' % (i, probabilities[i], capital[i])