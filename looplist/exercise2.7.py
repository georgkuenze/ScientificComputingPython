# -*- coding: utf-8 -*-
"""
Created on Mon Jul 06 16:48:47 2015

@author: Georg
"""

# Option 1
v_0 = 10 # m/s
g = 9.81 # m/s2
n = 20

def func(v_0, t, g):
    return v_0*t - (1/2)*g*t**2
    
t = [i*((2*v_0)/g - 0)/n + 0 for i in range(n+1)]
y = [func(v_0, x, g) for x in t]

print '%5s %6s' % ('t(s)', 'v(m/s)')
for i, j in zip(t, y):
    print '%5.2f %6.2f' % (i,j)
    
# Option 2
print '\n%5s %6s' % ('t(s)', 'v(m/s)')
x = 0
while x <= ((2*v_0)/g):
    y = func(v_0, x, g)
    print '%5.2f %6.2f' % (x, y)
    x += ((2*v_0)/g - 0)/n
    
# Make Nested lists
t = [i*((2*v_0)/g - 0)/n + 0 for i in range(n+1)]
y = [func(v_0, x, g) for x in t]
ty1 = [t, y]
ty2 = [[t,y] for t, y in zip(t, y)]

# Print ty1 (nested list of columns)
print '\n%5s %6s' % ('t(s)', 'v(m/s)')
for t, y in zip(ty1[0], ty1[1]):
    print '%5.2f %6.2f' % (t,y)

# Print ty2 (nested list of rows)
print '\n%5s %6s' % ('t(s)', 'v(m/s)')
for element in ty2:
    print '%5.2f %6.2f' % (element[0], element[1])