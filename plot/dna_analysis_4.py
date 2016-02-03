# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 23:29:08 2015

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

# Read genetic code function
def read_genetic_code_v1(filename):
    infile = open(filename, 'r')
    genetic_code = {}
    for line in infile:
        columns = line.split()
        genetic_code[columns[0]] = columns[1]
    return genetic_codes

def read_genetic_code_v2(filename):
    return dict([line.split()[0:2] for line in open(filename, 'r')])

def read_genetic_code_v3(filename):
    genetic_code = {}
    for line in open(filename, 'r'):
        columns = line.split()
        genetic_code[columns[0]] = {}
        genetic_code[columns[0]]['1-letter'] = columns[1]
        genetic_code[columns[0]]['3-letter'] = columns[2]
        genetic_code[columns[0]]['amino acid'] = columns[3]
    return genetic_code

def read_genetic_code_v4(filename):
    genetic_code = {}
    for line in open(filename, 'r'):
        c = line.split()
        genetic_code[c[0]] = {'1-letter': c[1], '3-letter': c[2], 'amino acid': c[3]}
    return genetic_code

# Download and read the genetic code
urlbase = 'http://hplgit.github.com/bioinf-py/data/'
genetic_code_file = 'genetic_code.tsv'
download(urlbase, genetic_code_file)
code = read_genetic_code_v3(genetic_code_file)

# Read DNA sequence function
def read_dnafile_v1(filename):
    dna = ''
    infile = open(filename, 'r')
    lines = infile.readlines()
    for line in lines:
        dna += line.strip()
    infile.close()
    return dna

# Read exon position function
def read_exon_regions_v1(filename):
    positions = []
    infile = open(filename, 'r')
    lines = infile.readlines()
    for line in lines:
        start, end = line.split()
        start, end = int(start), int(end)
        positions.append((start, end))
    infile.close()
    return positions

def read_exon_regions_v2(filename):
    return [tuple(int(x) for x in line.split()) for line in open(filename, 'r')]

# Download and read lactase gene
lactase_gene_file = 'lactase_gene.txt'
download(urlbase, lactase_gene_file)
lactase_gene = read_dnafile_v1(lactase_gene_file)

# Download and read exon regions of lactase gene
lactase_exon_file = 'lactase_exon.tsv'
download(urlbase, lactase_exon_file)
lactase_exon_regions = read_exon_regions_v2(lactase_exon_file)

# Create mRNA function
def create_mRNA(gene, exon_regions):
    mrna = ''
    for start, end in exon_regions:
        mrna += gene[start:end].replace('T', 'U')
    return mrna

# Save sequences to text file functions
def tofile_with_line_sep_v1(text, filename, chars_per_line=70):
    outfile = open(filename, 'w')
    for i in xrange(0, len(text), chars_per_line):
        start = i
        end = i + chars_per_line
        outfile.write(text[start:end] + '\n')
    outfile.close()

def tofile_with_line_sep_v2(text, foldername, filename, chars_per_line=70):
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

# Create Protein sequence from mRNA function
def create_protein(mrna, genetic_code):
    protein = ''     
    for i in xrange(len(mrna)/3):
        start = i*3
        end = start + 3
        protein += genetic_code[mrna[start:end]]['1-letter']
    return protein

def create_protein_fixed(mrna, genetic_code):
    protein_fixed = ''
    trans_start_pos = mrna.find('AUG')
    for i in range(len(mrna[trans_start_pos:])/3):
        start = trans_start_pos + i*3
        end = start + 3
        amino_acid = genetic_code[mrna[start:end]]['1-letter']
        if amino_acid == 'X':
            break
        protein_fixed += amino_acid
    return protein_fixed

# Create mRNA from lactase gene and save to file
mrna = create_mRNA(lactase_gene, lactase_exon_regions)
tofile_with_line_sep_v2(mrna, 'output', 'lactase_mrna.txt', chars_per_line=70)

# Create protein from lactase mRNA and save to file
protein = create_protein_fixed(mrna, code)
tofile_with_line_sep_v2(protein, 'output', 'lactase_protein.txt', chars_per_line=70)

print "Ten first amino acids of lactase protein:", protein[:10]
print "Ten last amino acids of lactase protein:", protein[-10:]
print "Length of lactase protein:", len(protein)

# Function to analyze congenital lactase deficiency
def congenital_lactase_def(lactase_gene, genetic_code, exon_regions,
                           output_folder=os.curdir, mrna_file=None, protein_file=None):
                               pos = 30049
                               mutated_gene = lactase_gene[:pos] + 'A' + lactase_gene[pos+1:]
                               mutated_mrna = create_mRNA(mutated_gene, exon_regions)
                               if mrna_file is not None:
                                   tofile_with_line_sep_v2(mutated_mrna, output_folder, mrna_file)
                               
                               mutated_protein = create_protein_fixed(mutated_mrna, genetic_code)
                               if protein_file is not None:
                                   tofile_with_line_sep_v2(mutated_protein, output_folder, protein_file)
                               return mutated_protein

# Create mutated protei in congenital lactase deficiency and save to file
mutated_protein = congenital_lactase_def(lactase_gene, code, lactase_exon_regions,
                                         output_folder='output', mrna_file='mutated_lactase_mrna.txt',
                                         protein_file='mutated_lactase_protein.txt')

print
print "Ten first amino acids of mutated lactase protein:", mutated_protein[:10]
print "Ten last amino acids of mutated lactase protein:", mutated_protein[-10:]
print "Length of mutated lactase protein:", len(mutated_protein)
                               