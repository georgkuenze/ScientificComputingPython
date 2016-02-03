# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 23:18:29 2015

@author: Georg
"""

import numpy as np

ix2char = {0: 'A', 1: 'T', 2: 'C', 3: 'G'}

def get_base_frequency(dna):
    return {base: dna.count(base)/float(len(dna)) for base in 'ATGC'}

def format_frequencies(freq):
    return ', '.join(['%s: %.2f' % (base, freq[base]) for base in sorted(freq)])

def make_dna(N):
    dna_ix = np.random.random_integers(0,3, size=N)
    dna_char = np.zeros(N, dtype='str')
    for i in ix2char:
        dna_char[dna_ix == i] = ix2char[i]
    return ''.join(dna_char.tolist())

def mutate_v2(dna, n):
    dna = np.array(list(dna), dtype='str')
    mutation_sites = np.random.random_integers(0, len(dna)-1, size=N)
    new_bases_ix = np.random.random_integers(0,3,size=N)
    new_bases_char = np.zeros(N, dtype='str')
    for i in ix2char:
        new_bases_char[new_bases_ix == i] = ix2char[i]
    dna[mutation_sites] = new_bases_char
    return ''.join(dna.tolist())

n = int(raw_input('How long DNA sequnce? '))
N = int(raw_input('How many mutations? '))

dna = make_dna(n)
dna_mut = mutate_v2(dna, N)

print '\nBase frequency of original DNA sequence:\n%s' % format_frequencies(get_base_frequency(dna))
print '\nBase frequency of mutated DNA sequence:\n%s' % format_frequencies(get_base_frequency(dna_mut))