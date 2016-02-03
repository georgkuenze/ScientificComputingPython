# -*- coding: utf-8 -*-
"""
Created on Thu Jul 09 11:45:50 2015

@author: Georg
"""

from math import *
import sys
formula = sys.argv[1]
x = eval(sys.argv[2])
result = eval(formula)

print "%s for x=%g yields %g" % (formula, x, result)