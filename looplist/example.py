# -*- coding: utf-8 -*-
"""
Created on Mon Jul 06 12:28:50 2015

@author: Georg
"""

# Reading in data and convert to lines
data = []
f = open('C:/Users/Georg/Documents/PythonDokumente/Scipro-primer/src/misc/Oxford_sun_hours.txt', 'r')
lines = f.readlines()
f.close()

# convert lines in list
for line in lines[1:-1]:
    character = line[1:-3]    
    inner_list = [float(elt.strip()) for elt in character.split(', ')]
    data.append(inner_list)

# Prepare lists for average monthly sun hours and month names 
val_av_sun_h = []
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# calculate monthly abverage
for month in range(12):
    total_sun_h = 0
    for year in range(len(data)):
        total_sun_h += data[year][month]
    av_sun_h = total_sun_h/len(data)
    val_av_sun_h.append(av_sun_h)

# Create dictionary and print result
from collections import OrderedDict
dic_sun_h = OrderedDict(zip(months, val_av_sun_h))
print "Average number of sun hours per month between 1929 - 2009:"
for k, v in dic_sun_h.iteritems():
    print '%s: %5.1f' % (k, v)

# Find month with highest average sun hour
for k, v in dic_sun_h.iteritems():
    if v == max(val_av_sun_h):
        print "\nMonth with highest average sun hours:", k
    else:
        continue

# Average sun hours per day in Dec and Jan
print "\nAverage number of sun hours per day in Dec and Jan"

for decade in range(0, len(data)-10, 10):
    total_sun_h = 0    
    for i in range(10):
        total_sun_h += data[decade+i][11] + data[decade+i+1][0]
    av_sun_h_per_day = total_sun_h/(10*(31+30))
    print "Decade " + str(1930+decade) + "-" + str(1939+decade) + ": " + "%.1f" % (av_sun_h_per_day)