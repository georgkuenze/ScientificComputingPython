# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 22:44:37 2015

@author: Georg
"""

def get_base_counts(dna):
    counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for base in dna:
        counts[base] += 1
    return counts

def get_base_frequencies_v1(dna):
    counts = get_base_counts(dna)
    return {base: count*1.0/len(dna) for base, count in counts.items()}
    
def get_base_frequencies_v2(dna):
    return {base: dna.count(base)/float(len(dna)) for base in 'ATGC'}
    
def format_frequencies(frequencies):
    return ', '.join(['%s: %.2f' % (base, frequencies[base]) for base in frequencies])

dna = 'ACCAGAGT'

frequencies = get_base_frequencies_v2(dna)
print "Base frequencies in %s\n%s" % (dna, format_frequencies(frequencies))

import urllib, os
urlbase = 'http://hplgit.github.com/bioinf-py/data/'
yeast_file = 'yeast_chr1.txt'
if not os.path.isfile(yeast_file):
    url = urlbase + yeast_file
    urllib.urlretrieve(url, filename=yeast_file)
    
dna = ''
infile = open(yeast_file, 'r')
lines = infile.readlines()
for line in lines:
    dna += line.strip()
infile.close()

yeast_base_freq = get_base_frequencies_v2(dna)
print "\nBase frequencies in yeast DNA (length %d)\n%s" % (len(dna), format_frequencies(yeast_base_freq))