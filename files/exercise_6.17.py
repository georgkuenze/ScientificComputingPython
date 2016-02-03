# -*- coding: utf-8 -*-
"""
Created on Thu Aug 06 22:35:50 2015

@author: Georg
"""

def get_base_counts(dna):
    counts = {'A': 0, 'G': 0, 'T': 0, 'C': 0}
    for base in dna:
        if base in 'AGTC':
            counts[base] += 1
        else:
            pass
    return counts

dna = 'ADLSTTLLD'
cts = get_base_counts(dna)
print cts