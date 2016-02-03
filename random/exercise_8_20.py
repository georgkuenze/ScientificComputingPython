# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 15:41:06 2015

@author: Georg
"""
import sys
import random

p = float(sys.argv[1]) # transition probability
N = int(sys.argv[2]) # sequence length

def create_markov_chain(p):
    states = [0, 1]
    trans_prob = {}
    for from_number in states:
        trans_prob[str(from_number)] = {}
        for to_number in states:
            if from_number == to_number:
                trans_prob[str(from_number)][str(to_number)] = p
            else:
                trans_prob[str(from_number)][str(to_number)] = 1 - p
    return trans_prob

def generate_sequence(N):
    s = ''
    for n in xrange(N):
        r = random.randint(0,1)
        s += str(r)
    return s

def generate_sequence_with_markov_chain(N, markov_chain):
    s = ''
    from_number = str(random.randint(0,1))
    for n in xrange(N):
        limit = 0
        r = random.random()
        for to_number in markov_chain[from_number]:
            limit += markov_chain[from_number][to_number]
            if r < limit:
                from_number = to_number
                s += from_number
                break
    return s

trans_prob = create_markov_chain(p)
print 'Markov Chain - Transition probabilities'
import pprint
pprint.pprint(trans_prob)

seq1 = generate_sequence(N)
print 'Random sequence without transition probabilities:'
print seq1, '%g times 1; %g times 0' % (seq1.count('1')/float(N), seq1.count('0')/float(N))
print
seq2 = generate_sequence_with_markov_chain(N, trans_prob)
print 'Random sequence with transition probabilities'
print seq2, '%g times 1; %g times 0' % (seq2.count('1')/float(N), seq2.count('0')/float(N))