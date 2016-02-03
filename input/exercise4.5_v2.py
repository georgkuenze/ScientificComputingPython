# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 18:59:26 2015

@author: Georg
"""

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
        print "You failed to provide a Fahrenheit temperature as input " \
        "on the command line."
        F = float(raw_input("Please provide a value in Fahrenheit: "))
    elif len(sys.argv) > 2:
        print "You provided too many input values."
        F = float(raw_input("Please provide only one value: "))
    else:
        try:
            F = float(sys.argv[1])
        except IndexError:
            print "Fahrenheit must be supplied on the command line."
            F = float(raw_input("Please provide a value in Fahrenheit: "))
        except ValueError:
            print "Value must be a number, not %s." % (sys.argv[1])
            F = float(raw_input("Please provide a value in Fahrenheit: "))
        if F < -459.4:
            print "F = %g is no physical meaningful value." % (F)
            F = float(raw_input("Please provide a value in Fahrenheit > -459.4: "))
    return F

# Main Program
F = read_f()
C = f2c(F)
print "%.2f Fahrenheit corresponds to %.2f Degree Celsius." % (F, C)