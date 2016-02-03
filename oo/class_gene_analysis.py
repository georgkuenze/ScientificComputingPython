# -*- coding: utf-8 -*-
"""
Created on Sat Sep 05 20:24:23 2015

@author: Georg
"""
from dna_functions import *

class Region:
    def __init__(self, dna, start, end):
        self._region = dna[start:end]
    
    def get_region(self):
        return self._region
    
    def __len__(self):
        return len(self._region)
    
    def __eq__(self, other):
        """Check if two Region instances are equal"""
        return self._region == other._region
    
    def __add__(self, other):
        """Add Region instances: self + other"""
        return self._region + other._region
    
    def __iadd__(self, other):
        """Increment Region instances: self += other"""
        self._region += other._region
        return self

class Gene:
    # Constructor method 1    
    #def __init__(self, dna, exon_regions):
    #    self._dna = dna
    #    self._exon_regions = exon_regions
    #    
    #    # Compute exons        
    #    self._exons = []
    #    for start, end in exon_regions:
    #        self._exons.append(Region(dna, start, end))
    #    
    #    # Compute introns
    #    self._introns = []
    #    prev_end = 0
    #    for start, end in exon_regions:
    #        self._introns.append(Region(dna, prev_end, start))
    #        prev_end = end
    #    self._introns.append(Region(dna, end, len(dna)))
    
    # Constructor method 2
    def __init__(self, dna, exon_regions):
        """
        dna: string or (urlbase, filename) tuple
        exon_regions: None, list of (start, end) tuples or (urlbase, filename) tuple
        In the case of (urlbase, filename) tuple, the file is downloaded and read.
        """
        if isinstance(dna, (list, tuple)) and len(dna) == 2 and \
        isinstance(dna[0], str) and isinstance(dna[1], str):
            download(urlbase=dna[0], filename=dna[1])
            dna = read_dnafile(dna[1])
        elif isinstance(dna, str):
            pass
        else:
            raise TypeError('dna=%s %s is not string or (urlbase, filename) tuple' \
            % (dna, type(dna)))
                
        self._dna = dna
    
        if exon_regions is None:
            self._exons   = None
            self._introns = None
        else:
            if isinstance(exon_regions, (list, tuple)) and len(exon_regions) == 2 and \
            isinstance(exon_regions[0], str) and isinstance(exon_regions[1], str):
                download(urlbase=exon_regions[0], filename=exon_regions[1])
                exon_regions = read_exon_regions(exon_regions[1])
            elif isinstance(exon_regions, (list, tuple)) and isinstance(exon_regions[0], (list, tuple)) and \
            isinstance(exon_regions[0][0], int) and isinstance(exon_regions[0][1], int):
                pass
            else:
                raise TypeError('exon_regions=%s %s is not list of (int, int)' \
                'or (urlbase, filename) tuple' % (exon_regions, type(exon_regions)))
            
            # Compute exons 
            self._exon_regions = exon_regions
            self._exons = []
            for start, end in exon_regions:
                self._exons.append(Region(dna, start, end))
            
            # Compute introns
            self._introns = []
            prev_end = 0
            for start, end in exon_regions:
                if start - prev_end > 0:
                    self._introns.append(Region(dna, prev_end, start))
                prev_end = end
            if len(dna) - end > 0:
                self._introns.append(Region(dna, end, len(dna)))
        
    def write(self, filenmae, chars_per_line=70):
        """Write DNA sequences to file with name filename."""
        tofile_with_line_sep(self._dna, filename, chars_per_line)
    
    def count(self, base):
        """Return number of occurrences of base in DNA."""
        return self._dna.count(base)
    
    def get_base_frequencies(self):
        """Return dictionary of base frequencies in DNA."""
        return get_base_frequencies(self._dna)
        
    def format_base_frequencies(self):
        """Return base frequencies formatted with two decimals."""
        return format_frequencies(self.get_base_frequencies())
    
    def create_mRNA(self):
        """Return string for mRNA."""
        if self._exons is not None:
            return create_mRNA(self._dna, self._exon_regions)
        else:
            raise ValueError('Cannot create mRNA for gene with no exon regions')
    
    def mutate_pos(self, pos, base):
        """Return Gene with a mutation to base at a given position pos."""
        dna = self._dna[:pos] + base + self._dna[pos+1:]
        return Gene(dna, self._exon_regions)
        
    def mutate_random(self, n=1):
        """
        Return Gene with n mutations at random positions.
        All mutations are equally probable.
        """
        mutated_dna = self._dna
        for i in range(n):
            mutated_dna = mutate(mutated_dna)
        return Gene(mutated_dna, self._exon_regions)
        
    def mutate_via_markov_chain(self, markov_chain):
        """
        Return Gene with a mutation at a random position.
        Mutation into new base is based on transition probabilities 
        in the markov_chain dict of dicts.
        """
        mutated_dna = mutate_via_markov_chain(self._dna, markov_chain)
        return Gene(mutated_dna, self._exon_regions)
    
    def get_dna(self):
        return self._dna
    
    def get_exons(self):
        return self._exons
    
    def get_introns(self):
        return self._introns
    
    def get_product(self):
        raise NotImplementedError('get_product() function not implemented in class %s' \
        % self.__class__.__name__)
        
    def __len__(self):
        return len(self._dna)
    
    def __add__(self, other):
        """self + other: append other._dna to self._dna"""
        if self._exons is None and other._exons is None:
            return Gene(self._dna + other._dna, None)
        else:
            raise ValueError('Cannot add Genes with exon regions')
    
    def __iadd__(self, other):
        """self += other: append other._dna to self._dna"""
        if self._exons is None and other._exons is None:
            self._dna += other._dna
            return self
        else:
            raise ValueError('Cannot append Genes with exon regions')
    
    def __eq__(self, other):
        """Check if two Gene instances are equal."""
        return self._dna == other._dna and self._exons == other._exons
    
    def __str__(self):
        """Print info about Gene instance."""
        s = 'Gene: ' + self._dna[:6] + '...' + self._dna[-6:] + ', length=%d bp' % len(self._dna)
        if self._exons is not None:
            s += ', %d exon regions' % len(self._exons)
        return s

class RNACodingGene(Gene):
    def get_product(self):
        return self.create_mRNA()
    
class ProteinCodingGene(Gene):
    def __init__(self, dna, exon_regions):
        Gene.__init__(self, dna, exon_regions)
        urlbase = 'http://hplgit.github.com/bioinf-py/data/'
        genetic_code_file = 'genetic_code.tsv'
        download(urlbase, genetic_code_file)
        code = read_genetic_code(genetic_code_file)
        self.genetic_code = code
    
    def get_product(self):
        return create_protein_fixed(self.create_mRNA(), self.genetic_code)

def test_lactase_gene():
    urlbase = 'http://hplgit.github.com/bioinf-py/data/'
    lactase_gene_file = 'lactase_gene.txt'
    lactase_exon_file = 'lactase_exon.tsv'
    lactase_gene = ProteinCodingGene(
        (urlbase, lactase_gene_file),
        (urlbase, lactase_exon_file))

    protein = lactase_gene.get_product()
    tofile_with_line_sep(protein, 'output', 'lactase_protein.txt')

    # Manual downloading and reading
    download(urlbase, lactase_gene_file)
    lactase_dna = read_dnafile(lactase_gene_file)
    download(urlbase, lactase_exon_file)
    lactase_exon_regions = read_exon_regions(lactase_exon_file)
    lactase_gene2 = Gene(lactase_dna, lactase_exon_regions)

    print lactase_gene
    print lactase_gene2

    assert lactase_gene == lactase_gene2

if __name__ == '__main__':
    test_lactase_gene()