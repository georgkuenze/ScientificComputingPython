# -*- coding: utf-8 -*-
"""
Created on Sat Aug 01 20:17:33 2015

@author: Georg
"""
import pprint

def read_data(filename):
    data = {}    
    infile = open(filename, 'r')
    lines = infile.readlines()[3:9]
    for line in lines:
        line = line.replace('(early) ', '')
        line = line.replace('(late)', '')
        line = line.replace('present', '0.0')
        line = line.replace(' - ', '-')
        
        if 'ergaster' in line:
            words = line.split()
            name = ' '.join(words[0:2])
            when = words[2]
            height = words[3]
            mass = None
            brain_volume[4]
        else:
            words = line.split()
            brain_volume = words[-1]
            mass = words[-2]
            height = words[-3]
            when = words[-4]
            name = ' '.join(words[:-4])
        data[name] = {'Time': when, 'Mass': mass, 'Height': height, 'Brain': brain_volume}
    return data
    infile.close()

def sort_name(name1, name2):
    last_name1 = name1.split()[-1]
    last_name2 = name2.split()[-1]
    if last_name1 < last_name2:
        return -1
    elif last_name1 > last_name2:
        return 1
    else:
        return 0

input_file = 'human_evolution.txt'
data_dict = read_data(input_file)

print "%-20s %-10s %-8s %-8s %-10s\n%s" % ('Species', 'Brain Vol.', 'Height', 'Mass', 'When', '-'*58)
for name in sorted(data_dict, sort_name):
    print "%-20s %-10s %-8s %-8s %-10s" % (name, data_dict[name]['Brain'], data_dict[name]['Height'],
                              data_dict[name]['Mass'], data_dict[name]['Time'])