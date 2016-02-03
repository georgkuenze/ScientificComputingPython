# -*- coding: utf-8 -*-
"""
Created on Mon Jul 06 11:36:39 2015

@author: Georg
"""

C_degree = [i for i in range(0,45,5)]
F_degree = [(9.0/5)*C + 32.0 for C in C_degree]
table = [[C,F] for C, F in zip(C_degree, F_degree)]

import pprint
pprint.pprint(table)

import scitools.pprint2
scitools.pprint2.pprint(table)
scitools.pprint2.float_format = '%.2e'
scitools.pprint2.pprint(table)

for C, F in table[C_degree.index(5):C_degree.index(35)]:
    print '%5.1f %5.1f' % (C,F)

for element in table:
    for i in element:
        print i,
    print

print C_degree
C_degree_rev = reversed(C_degree)
for element in C_degree_rev:
    print element,