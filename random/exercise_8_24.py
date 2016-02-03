# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:28:16 2015

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

def advance_generation(parents, policy='one child', male_portion=0.5, fertility=1.0, 
                       outlier_portion=0.06, additional_children=5):
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
            new_children = get_children(len(daughters), male_portion, fertility=1.0)
            children = np.concatenate((children, new_children), axis=1)
            daughters = new_children[new_children == FEMALE]
            
    elif policy == 'one son + outlier':
        # Couples who stick to the one son policy
        couples_A = (1-outlier_portion)*couples
        # Couples who do not stick to the one son policy and want six children
        couples_B = outlier_portion*couples
        
        # First try
        children = get_children(couples_A, male_portion, fertility)
        
        # Continue in cases where child is female
        daughters = children[children == FEMALE]
        while len(daughters) > 0:
            new_children = get_children(len(daughters), male_portion, fertility=1.0)
            children = np.concatenate((children, new_children), axis=1)
            daughters = new_children[new_children == FEMALE]
            
        # Couples who get six children
        for i in range(1+additional_children):
            new_children = get_children(couples_B, male_portion, fertility=1.0)
            children = np.concatenate((children, new_children), axis=1)
        
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

# One son policy
print 'One son policy - start: %d' % (len(parents))
for i in range(10):
    new_parents = advance_generation(parents, policy='one son', male_portion=male_portion, fertility=fertility,
                                 outlier_portion=0.0, additional_children=0)
    diff = len(new_parents) - len(parents)
    parents = new_parents
    print '%2.d. generation of descendants: %7.d   difference: %7.d' % (i+1, len(parents), diff)
print

# Start population
np.random.seed(3)
r = np.random.random(N)
parents = np.zeros(N)
MALE = 1; FEMALE = 2
parents[r < 0.5] = MALE
parents[r >= 0.5] = FEMALE

# One son policy + outlier
print 'One son policy + outlier - start: %d' % (len(parents))
for i in range(10):
    new_parents = advance_generation(parents, policy='one son + outlier', male_portion=male_portion, fertility=fertility,
                                 outlier_portion=0.06, additional_children=5)
    diff = len(new_parents) - len(parents)
    parents = new_parents
    print '%2.d. generation of descendants: %7.d   difference: %7.d' % (i+1, len(parents), diff)