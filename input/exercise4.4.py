# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 17:55:25 2015

@author: Georg
"""
# Function for conversion Fahrenheit to Degree Celsius
def f2c(F):
    C = (F-32)*(5.0/9.0)
    return C

# Open input file
infile = open('Fdeg.dat', 'r')

# Skip first three lines
counter = 0
while counter < 3:
    infile.readline()
    counter += 1

# Read in lines and split strings and float values
F = []
for line in infile:
    words = line.split(': ')
    F.append(float(words[1]))
    
# Close file
infile.close()

# Calculate Celsius degress from Fahrenheit
C = []
for i in range(len(F)):
    C.append(f2c(F[i]))

# Create output file
outfile = open('FandCdeg.dat', 'w')
outfile.write('Temperature data\n%s\n' % ('-'*27))
outfile.write('Fahrenheit   Degree Celsius\n')
for i, j in zip(F, C):
    outfile.write('%10.2f   %14.2f\n' % (i, j))
outfile.write('\n')
outfile.close()