# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 23:45:03 2015

@author: Georg
"""
import numpy as np
import pprint

dna_list = ['GGTAG', 'GGTAC', 'GGTGC', 'GGTAGC']

def freq_list_of_lists_v2(dna_list):
    n = max(len(dna) for dna in dna_list)    
    freq_matrix = [[0]*n for i in 'ATGC']
    base2index = {'A':0, 'T':1, 'G':2, 'C': 3}
    
    for dna in dna_list:
        for index, base in enumerate(dna):
            freq_matrix[base2index[base]][index] += 1
    return freq_matrix

def find_consensus_v1(freq_matrix):
    if isinstance(freq_matrix, list) and isinstance(freq_matrix[0], list):
        pass
    else:
        raise TypeError('frequency matrix must be a list of lists')
    
    base2index = {'A': 0, 'T': 1, 'G': 2, 'C': 3}
    consensus = []
    
    for i in range(len(freq_matrix[0])):
        max_base_freq = -1
        max_base = None
        for base in 'ATGC':
            if freq_matrix[base2index[base]][i] > max_base_freq:
                max_base_freq = freq_matrix[base2index[base]][i]
                max_base = base
            elif freq_matrix[base2index[base]][i] == max_base_freq:
                max_base = '-'
        consensus += max_base
    
    return consensus

frequency_matrix = freq_list_of_lists_v2(dna_list)
pprint.pprint(frequency_matrix)
consensus_sequence = find_consensus_v1(frequency_matrix)
print 'Consensus Sequence:', consensus_sequence


def freq_dict_of_dicts_v1(dna_list):
    n = max([len(dna) for dna in dna_list])
    freq_matrix = {base: {index: 0 for index in range(n)} for base in 'ATGC'}
    
    for dna in dna_list:
        for index, base in enumerate(dna):
            freq_matrix[base][index] += 1
    return freq_matrix

def find_consensus_v2(freq_matrix):
    if isinstance(freq_matrix, dict) and isinstance(freq_matrix['A'], dict):
        pass
    else:
        raise TypeError('frequency matrix must be a list of lists')
    
    consensus = ''
    
    for i in range(len(freq_matrix['A'])):
        max_base_freq = -1
        max_base = None
        for base in 'ATGC':
            if freq_matrix[base][i] > max_base_freq:
                max_base_freq = freq_matrix[base][i]
                max_base = base
            elif freq_matrix[base][i] == max_base_freq:
                max_base = '-'
        consensus += max_base
    
    return consensus
    
frequency_matrix_dict = freq_dict_of_dicts_v1(dna_list)
pprint.pprint(frequency_matrix_dict)
consensus_sequence = find_consensus_v2(frequency_matrix_dict)
print 'Consensus Sequence:', consensus_sequence 