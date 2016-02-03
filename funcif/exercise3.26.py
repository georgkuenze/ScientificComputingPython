# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 10:35:48 2015

@author: Georg
"""
import matplotlib.pyplot as plt

# Define piecewise constant function
def piecewise(x, data):
    for i in range(len(data)-1):
        if data[i][0] < x <= data[i+1][0]:
            return data[i][1]
        else:
            continue
    for i in range(len(data)-1, len(data)):
        if x > data[i][0]:
            return data[i][1]
        else:
            continue
    if x < data[0][0]:
        print "x = %g is out of interval." % (x)

# Define Intervals and returned value
data = [(0,-1),(1,0),(1.5,4), (2,6)]

# Test piecewise function
result = piecewise(0.8, data)
print "x = %g gives value = %g back.\n" % (0.8, result)

result = piecewise(-0.8, data)
print result

# Plot piecewise function
n = 1000
x = [3./n*i + 0 for i in range(n+1)]
y = []
for i in range(len(x)):
    y.append(piecewise(x[i], data))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y, 'r-')
ax.set_ylim(-1.5,6.5)