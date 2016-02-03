# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 12:47:16 2015

@author: Georg
"""

import urllib, os

# Download function
def download(urlbase, filename):
    if not os.path.isfile(filename):
        url = urlbase + filename
        try:
            urllib.urlretrieve(url, filename=filename)
        except IOError as e:
            raise IOError('No internet connection')
        # Check if downloaded file is an HTML file, which
        # is what github.com returns if the URL is not existing
        f = open(filename, 'r')
        if 'DOCTYPE html' in f.readline():
            raise IOError('URL %s does not exist' % (url))

# Read DNA sequence function
def read_dnafile(filename):
    dna = ''
    infile = open(filename, 'r')
    lines = infile.readlines()
    for line in lines:
        dna += line.strip()
    infile.close()
    return dna

# Read exon position function
def read_exon_regions(filename):
    return [tuple(int(x) for x in line.split()) for line in open(filename, 'r')]

# Create mRNA function
def get_exon_dna(gene, exon_regions):
    exon_dna = ''
    for start, end in exon_regions:
        exon_dna += gene[start:end]
    return exon_dna
    
def get_intron_dna(gene, exon_regions):
    intron_dna = ''
    for i in range(len(exon_regions)-1):
        intron_dna += gene[exon_regions[i][-1]:exon_regions[i+1][0]]
    intron_dna += gene[exon_regions[-1][-1]:len(gene)]
    return intron_dna
    
# Function to save sequence to file
def tofile_with_line_sep(text, foldername, filename, chars_per_line=70):
    if not os.path.isdir(foldername):
        os.makedirs(foldername)
    filename = os.path.join(foldername, filename)
    outfile = open(filename, 'w')
    
    if chars_per_line == 'inf':    # infinite number of characters per line
        outfile.write(text)
    else:
        for i in xrange(0, len(text), chars_per_line):
            start = i
            end = i + chars_per_line
            outfile.write(text[start:end] + '\n')
    outfile.close()

def get_base_frequency(dna):
    return {base: dna.count(base)/float(len(dna)) for base in 'AGTC'}
def format_frequencies(frequency):
    return ', '.join(["%s: %.2f" % (base, frequency[base]) for base in frequency])
    
# Download and read lactase gene
urlbase = 'http://hplgit.github.com/bioinf-py/data/'
lactase_gene_file = 'lactase_gene.txt'
download(urlbase, lactase_gene_file)
lactase_gene = read_dnafile(lactase_gene_file)

# Download and read exon regions of lactase gene
lactase_exon_file = 'lactase_exon.tsv'
download(urlbase, lactase_exon_file)
lactase_exon_regions = read_exon_regions(lactase_exon_file)

# Get exon and intron DNA and print to file
exon_dna = get_exon_dna(lactase_gene, lactase_exon_regions)
intron_dna = get_intron_dna(lactase_gene, lactase_exon_regions)
tofile_with_line_sep(exon_dna, 'output', 'lactase_exon_dna.txt', chars_per_line=70)
tofile_with_line_sep(intron_dna, 'output', 'lactase_intron_dna.txt', chars_per_line=70)
print "Length exonic DNA:", len(exon_dna), "nt"
print "Length intronic DNA:", len(intron_dna), "nt"
print "Length lactase gene:", len(lactase_gene), "nt"

freq_exon = get_base_frequency(exon_dna)
freq_intron = get_base_frequency(intron_dna)
print "Base frequency in exonic DNA:", format_frequencies(freq_exon)
print "Base frequency in intronic DNA:", format_frequencies(freq_intron)