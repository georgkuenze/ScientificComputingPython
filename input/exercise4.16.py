# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 14:39:25 2015

@author: Georg
"""

import sys
from calendar import weekday

# Define function to get date input
def get_input():
    if len(sys.argv) < 4:
        raise IndexError('You provided not the full date. Specify "year month day".')
    elif len(sys.argv) > 4:
        raise IndexError('You typed in too many field. Specify "year month day".')
    try:
        y = int(sys.argv[1])
    except ValueError:
        raise ValueError("Year must be a number, not %s." % (sys.argv[1]))
    try:
        m = int(sys.argv[2])
    except ValueError:
        raise ValueError("Month must be a number, not %s." % (sys.argv[2]))
    try:
        d = int(sys.argv[3])
    except ValueError:
        raise ValueError("Day must be a number, not %s." % (sys.argv[3]))
    return y, m, d

# Function to return weekday
# Makes use of weekday function from module calendar
def print_weekday(y, m, d):
    number = weekday(y, m, d)
    n = [0, 1, 2, 3, 4, 5, 7]
    name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for i, j in zip(n, name):
        if i == number:
            print "'%d-%02d-%02d' is/was a %s." % (y, m, d, j)
            break
        else:
            continue

y, m, d = get_input()
print_weekday(y, m, d)