# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:13:10 2015

@author: Georg
"""
import random
from numpy.random import random_integers
from numpy import zeros

# Three basic functions to make a DNA string and to count DNA bases
def get_base_frequency(dna):
    return {base: dna.count(base)/float(len(dna)) for base in 'ATGC'}

def format_frequencies(freq):
    return ', '.join(['%s: %.2f' % (base, freq[base]) for base in sorted(freq)])
    
def make_dna(N):
    ix2char = {0: 'A', 1: 'T', 2: 'C', 3: 'G'}
    dna_ix = random_integers(0,3, size=N)
    dna_char = zeros(N, dtype='str')
    for i in ix2char:
        dna_char[dna_ix == i] = ix2char[i]
    return ''.join(dna_char.tolist())

# Function to create a Markov chain
def create_markov_chain():
    """ 
    Function create 4x4 matrix as dictionary with transition
    probabilities for mutation from one base to another base
    """
    markov_chain = {}
    for from_base in 'ATGC':
        # Generate random transition probabilities by dividing
        # [0,1] into four intervals of random length
        slice_points = sorted([0] + [random.random() for i in range(3)] + [1])
        transition_probabilities = [slice_points[i+1] - slice_points[i] for i in range(4)]
        markov_chain[from_base] = {base: p for base, p in zip('ATGC', transition_probabilities)}
    return markov_chain

# Function to check that transition probabilities in markov chain are correct
def check_probabilities(markov_chain):
    for from_base in 'ATGC':
        s = sum(markov_chain[from_base][to_base] for to_base in 'ATGC')
        if abs(s-1) > 1.0e-15:
            raise ValueError('Transition probabilities for %s do not sum up to 1') % (from_base)

# Function to select a transition from a discrete probability distribution
def draw(prob_dist):
    """
    Function picks a value from a discrete probability distribution
    represented as a dictionary of form: P(x=value) = prob_dist[value]
    """
    limit = 0
    r = random.random()
    for value in prob_dist:
        limit += prob_dist[value]
        if r < limit:
            return value
        else:
            pass
# Function to check that draw results in frequencies equivalent to the 
# transition probabilities
def check_draw(prob_dist, N=10**6):
    frequencies = {value: 0 for value in prob_dist}
    for i in range(N):
        value = draw(prob_dist)
        frequencies[value] += 1
    for value in frequencies:
        frequencies[value] /= float(N)
    print 'Test that transition probabilities can be reproduced by Monte Carlo method.'
    print ', '.join(['%s: %.4f (exact %.4f)' % (v, frequencies[v], prob_dist[v]) for v in frequencies])

def mutate_via_markov_chain(dna, markov_chain):
    dna_list = list(dna)
    mutation_site = random.randint(0, len(dna_list)-1)
    from_base = dna_list[mutation_site]
    to_base = draw(markov_chain[from_base])
    dna_list[mutation_site] = to_base
    return ''.join(dna_list)

# Make Markov chain
mc = create_markov_chain()
print 'Generated Markov Chain - Transition probabilities for mutation from one DNA base to another one'
import pprint
pprint.pprint(mc)

# Test that transition probabilities can be reproduced by Monte Carlo method
print
check_draw(mc['A'])
print

# Test mutation via Markov chain

# Make a DNA string of 30nt
N = 30
dna = make_dna(N)
print 'Starting DNA: ', dna
print 'Base frequency: ', format_frequencies(get_base_frequency(dna))

mutations = 10**6
for i in xrange(mutations):
    dna = mutate_via_markov_chain(dna, mc)

print 'DNA after %.e mutations: ' % (mutations), dna
print 'Base frequency: ', format_frequencies(get_base_frequency(dna))