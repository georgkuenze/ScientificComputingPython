# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 16:43:40 2015

@author: Georg
"""

data = [
('Alpha Centauri A',    4.3,  0.26,      1.56),
('Alpha Centauri B',    4.3,  0.077,     0.45),
('Alpha Centauri C',    4.2,  0.00001,   0.00006),
("Barnard's Star",      6.0,  0.00004,   0.0005),
('Wolf 359',            7.7,  0.000001,  0.00002),
('BD +36 degrees 2147', 8.2,  0.0003,    0.006),
('Luyten 726-8 A',      8.4,  0.000003,  0.00006),
('Luyten 726-8 B',      8.4,  0.000002,  0.00004),
('Sirius A',            8.6,  1.00,      23.6),
('Sirius B',            8.6,  0.001,     0.003),
('Ross 154',            9.4,  0.00002,   0.0005),
]

# Sorting list with tuples
# First option - define sorting function

def sort_distance(a,b):
    if a[1] < b[1]:
        return -1
    elif a[1] > b[1]:
        return 1
    else:
        return 0

def sort_brightness(a,b):
    if a[2] < b[2]:
        return -1
    elif a[2] > b[2]:
        return 1
    else:
        return 0

def sort_luminosity(a,b):
    if a[3] < b[3]:
        return -1
    elif a[3] > b[3]:
        return 1
    else:
        return 0

print "Sorting with method one -- own sort function:\n"

print "Sort with decreasing distance:"
print "{0:<18s}{1:<9s}{2:<16s}{3:<12s}".format("Star", "Distance", "App. Brightness", "Luminosity")
for item in sorted(data, cmp=sort_distance):
    print "{0:<20s}{1:>6.1f}{2:>16.6f}{3:>11.5f}".format(item[0], item[1], item[2], item[3])

print "\nSort with decreasing app. brightness:"
print "{0:<18s}{1:<9s}{2:<16s}{3:<12s}".format("Star", "Distance", "App. Brightness", "Luminosity")
for item in sorted(data, cmp=sort_brightness):
    print "{0:<20s}{1:>6.1f}{2:>16.6f}{3:>11.5f}".format(item[0], item[1], item[2], item[3])

print "\nSort with decreasing luminosity:"
print "{0:<18s}{1:<9s}{2:<16s}{3:<12s}".format("Star", "Distance", "App. Brightness", "Luminosity")
for item in sorted(data, cmp=sort_brightness):
    print "{0:<20s}{1:>6.1f}{2:>16.6f}{3:>11.5f}".format(item[0], item[1], item[2], item[3])

# Second option - use key argument of sorted() function

print "\nSorting with method two -- key argument of sorted() function:\n"

print "Sorting with decreasing distance:"
print "{0:<18s}{1:<9s}{2:<16s}{3:<12s}".format("Star", "Distance", "App. Brightness", "Luminosity")
for item in sorted(data, key = lambda tup: tup[1]):
    print "{0:<20s}{1:>6.1f}{2:>16.6f}{3:>11.5f}".format(item[0], item[1], item[2], item[3])

print "\nSort with decreasing app. brightness:"
print "{0:<18s}{1:<9s}{2:<16s}{3:<12s}".format("Star", "Distance", "App. Brightness", "Luminosity")
for item in sorted(data, key = lambda tup: tup[2]):
    print "{0:<20s}{1:>6.1f}{2:>16.6f}{3:>11.5f}".format(item[0], item[1], item[2], item[3])

print "\nSort with decreasing luminosity:"
print "{0:<18s}{1:<9s}{2:<16s}{3:<12s}".format("Star", "Distance", "App. Brightness", "Luminosity")
for item in sorted(data, key = lambda tup: tup[3]):
    print "{0:<20s}{1:>6.1f}{2:>16.6f}{3:>11.5f}".format(item[0], item[1], item[2], item[3])
