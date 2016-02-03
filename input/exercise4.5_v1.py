# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 18:26:53 2015

@author: Georg
"""
import sys

# Function definitions
def f2c(F):
    C = (F-32)*(5.0/9.0)
    return C

def read_f():
    if len(sys.argv) < 2:
        raise IndexError("You failed to provide a Fahrenheit temperature as input " \
        "on the command line.")
    if len(sys.argv) > 2:
        raise IndexError("You provided too many input values.")
    try:
        F = float(sys.argv[1])
    except IndexError:
        raise IndexError("Fahrenheit must be supplied on the command line.")
        
    except ValueError:
        raise ValueError("Value must be a number, not %s." % (sys.argv[1]))
        
    if F < -459.4:
        raise ValueError("F = %g is no physical meaningful value." % (F))
    return F

# Main Program
F = read_f()
C = f2c(F)
print "%.2f Fahrenheit corresponds to %.2f Degree Celsius." % (F, C)