# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 22:57:30 2015

@author: Georg
"""

import numpy as np

def get_children(n, male_portion, fertility):
    n = (fertility*n)   # number of fertile people
    r = np.random.random(n)  # next generation
    children = np.zeros(n)
    children[r < male_portion] = MALE
    children[r >= male_portion] = FEMALE
    return children

def advance_generation(parents, policy='one child', male_portion=0.5, fertility=1.0):
    males = len(parents[parents == MALE])
    females = len(parents) - males
    couples = min(females, males)
    
    if policy == 'one child':
        children = get_children(couples, male_portion, fertility)
    elif policy == 'one son':
        # First try
        children = get_children(couples, male_portion, fertility)
        
        # Continue in cases where child is female
        daughters = children[children == FEMALE]
        while len(daughters) > 0:
            new_children = get_children(len(daughters), male_portion, fertility)
            children = np.concatenate((children, new_children), axis=1)
            daughters = new_children[new_children == FEMALE]
    return children

N = 10**6
male_portion = 0.51
fertility = 0.92

# Start population
np.random.seed(3)
r = np.random.random(N)
parents = np.zeros(N)
MALE = 1; FEMALE = 2
parents[r < 0.5] = MALE
parents[r >= 0.5] = FEMALE

# One child policy
print 'One child policy - start: %d' % (len(parents))
for i in range(10):
    parents = advance_generation(parents, policy='one child', male_portion=male_portion, fertility=fertility)
    print '%2.d. generation of descendants: %7.d' % (i+1, len(parents))
print

# Start population
np.random.seed(3)
r = np.random.random(N)
parents = np.zeros(N)
MALE = 1; FEMALE = 2
parents[r < 0.5] = MALE
parents[r >= 0.5] = FEMALE

# One son policy
print 'One son policy - start: %d' % (len(parents))
for i in range(10):
    parents = advance_generation(parents, policy='one son', male_portion=male_portion, fertility=fertility)
    print '%2.d. generation of descendants: %7.d' % (i+1, len(parents))