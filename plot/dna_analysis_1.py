# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 22:04:42 2015

@author: Georg
"""

def freq_list(dna_list):
    n = len(dna_list[0])
    A = [0]*n
    T = [0]*n
    G = [0]*n
    C = [0]*n

    for dna in dna_list:
        for index, base in enumerate(dna):
            if base == 'A':
                A[index] += 1
            elif base == 'T':
                T[index] += 1
            elif base == 'G':
                G[index] += 1
            elif base == 'C':
                C[index] += 1
    return A, T, G, C

dna_list = ['GGTAG', 'GGTAC', 'GGTGC']

A, T, G, C = freq_list(dna_list)
print A
print T
print G
print C

def freq_list_of_lists_v1(dna_list):
    freq_matrix = [[0 for j in dna_list[0]] for i in 'ATGC']
    
    for dna in dna_list:
        for index, base in enumerate(dna):
            if base == 'A':
                freq_matrix[0][index] += 1
            elif base == 'T':
                freq_matrix[1][index] += 1
            elif base == 'G':
                freq_matrix[2][index] += 1
            elif base == 'C':
                freq_matrix[3][index] += 1
    return freq_matrix

frequency_matrix = freq_list_of_lists_v1(dna_list)
print frequency_matrix

def freq_list_of_lists_v2(dna_list):
    freq_matrix = [[0 for j in dna_list[0]] for i in 'ATGC']
    base2index = {'A':0, 'T':1, 'G':2, 'C': 3}
    
    for dna in dna_list:
        for index, base in enumerate(dna):
            freq_matrix[base2index[base]][index] += 1
    return freq_matrix

frequency_matrix = freq_list_of_lists_v1(dna_list)
print frequency_matrix

def freq_dict_of_lists_v1(dna_list):
    n = max([len(dna) for dna in dna_list])
    
    freq_matrix = {
    'A': [0]*n,
    'T': [0]*n,
    'G': [0]*n,
    'C': [0]*n    
    }
    
    for dna in dna_list:
        for index, base in enumerate(dna):
            freq_matrix[base][index] += 1
    return freq_matrix

dna_list = ['GGTAG', 'GGTAC', 'GGTGC', 'GGTAGC']
frequency_matrix = freq_dict_of_lists_v1(dna_list)
import pprint
pprint.pprint(frequency_matrix)

def freq_dict_of_lists_v2(dna_list):
    n = max([len(dna) for dna in dna_list])
    
    freq_matrix = {base: [0]*n for base in 'ATGC'}
    
    for dna in dna_list:
        for index, base in enumerate(dna):
            freq_matrix[base][index] += 1
    return freq_matrix

frequency_matrix = freq_dict_of_lists_v2(dna_list)
pprint.pprint(frequency_matrix)

from collections import defaultdict

def freq_dict_of_dicts_v1(dna_list):
    n = max([len(dna) for dna in dna_list])
    freq_matrix = {base: defaultdict(lambda: 0) for base in 'ATGC'}
    
    for dna in dna_list:
        for index, base in enumerate(dna):
            freq_matrix[base][index] += 1
    return freq_matrix

frequency_matrix = freq_dict_of_dicts_v1(dna_list)
pprint.pprint(frequency_matrix)

import numpy as np
def freq_dict_of_arrays_v1(dna_list):
    n = max([len(dna) for dna in dna_list])
    
    freq_matrix = {base: np.zeros(n, dtype='int64') for base in 'ATGC'}
    
    for dna in dna_list:
        for index, base in enumerate(dna):
            freq_matrix[base][index] += 1
    return freq_matrix
    
frequency_matrix = freq_dict_of_arrays_v1(dna_list)
pprint.pprint(frequency_matrix)

def freq_dict_of_arrays_v2(dna_list):
    n = max(len(dna) for dna in dna_list)
    
    freq_matrix = {base: np.zeros(n, dtype='int64') for base in 'ATGC'}
    for dna in dna_list:
        dna = np.array(dna, dtype='c')
        for base in 'ATGC':
            b = np.asarray(dna == base)
            if len(b) != n:
                b = np.append(b, np.zeros(n-len(b)))
            else:
                pass
            freq_matrix[base] += b
    return freq_matrix

frequency_matrix = freq_dict_of_arrays_v2(dna_list)
pprint.pprint(frequency_matrix)