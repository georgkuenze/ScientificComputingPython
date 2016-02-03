# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 23:04:26 2015

@author: Georg
"""

def count_pairs(dna, pair):
    dna = dna.lower()
    pair = pair.lower()    
    counter = 0    
    for i in range(0, len(dna)-1):
        dinucleotide = dna[i:i+2]
        if dinucleotide == pair:
            counter += 1
    return counter
    
def count_strings(dna, seq):
    dna = dna.lower()
    seq = seq.lower()
    n = len(seq)    
    counter = 0    
    for i in range(0, len(dna)-(n-1)):
        string = dna[i:i+n]
        if string == seq:
            counter += 1
    return counter

dna = "ATgcAtgcccATgcAg"
pair = "Ca"
seq = "cat"

print "Number of dinucleotides in DNA is", count_pairs(dna, pair)
print "Number of trinucleotides in DNA is", count_strings(dna, seq)
        