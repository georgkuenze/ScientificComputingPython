# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 22:55:41 2015

@author: Georg
"""
import matplotlib.pyplot as plt 

# Define function to calculate ball height
def height(t, v0, g):
    y = v0*t - 0.5*g*t**2
    return y

# Read input file
infile = open('ball_file.txt', 'r')
v0 = []
t = []
for line in infile:
    elements = line.split()     
    if elements[0] == 'v0:':   # Read initial velocity
        v0.append(float(elements[1]))
    elif elements[0] == 't:':
        elements = infile.next().split()   # If 't:' is encoutered, change to next line and split elements
        for element in elements:
            t.append(float(element))   # Covert elements to floats
    else:
        for element in elements:
            t.append(float(element))
infile.close()

# Sort time values and calculate height
t = sorted(t)
y = [height(x, v0[0], 9.81) for x in t]

# Make output file
outfile = open('ball_height.txt', 'w')
outfile.write('Height of a Ball with v0 = %.2f m/s\n%s\n' % (v0[0], '-'*21))
outfile.write('Time (s)   Height (m)\n')
for i in range(len(t)):
    outfile.write('%8.3f   %10.3f\n' % (t[i], y[i]))
outfile.close()

# Print results
print 'Height of a Ball with v0 = %.2f m/s\n%s' % (v0[0], '-'*21)
print 'Time (s)   Height (m)'
for i in range(len(t)):
    print '%8.3f   %10.3f' % (t[i], y[i])

# Make plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(t,y,'bo', label='points')
a = [(max(t) - min(t))/float(1000)*k + min(t) for k in range(1000)]
ax.plot(a, [height(x, v0[0], 9.81) for x in a], 'r-', label='line')
ax.legend(loc=1) 