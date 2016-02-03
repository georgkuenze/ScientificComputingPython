# -*- coding: utf-8 -*-
"""
Created on Sat Aug 01 19:47:17 2015

@author: Georg
"""

import pprint


def read_constants(filename):
    constants = {}
    infile = open(filename, 'r')
    lines = infile.readlines()
    for line in lines[2:]:
        words = line.split()
        unit = words[-1]
        value = float(words[-2])
        name = ' '.join(words[:-2])
        constants[name] = (value, unit)
    infile.close()
    return constants

input_file = 'constants.txt'
dic_data = read_constants(input_file)

pprint.pprint(dic_data)
print
print "%-22s %-12s %s\n%s" % ('Constant', 'Value', 'Unit','-'*48)
for constant in dic_data:
    print "%-22s %e %s" % (constant, dic_data[constant][0], dic_data[constant][1])