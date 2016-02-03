# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 12:22:45 2015

@author: Georg
"""

import numpy as np

# Define coefficients
coeff = list(input("Choose coefficients "))
print "Coefficients:", coeff
    
# Calculate polynomial
p = np.poly1d(coeff)

# Calculate roots of that polynomial
roots = np.roots(coeff)
print "Roots:", roots
print "No. roots", len(roots)

def calc_poly(x, rts):
    product = 1    
    for i in range(0, len(rts)):
        product *= (x - rts[i])
    return product

# Choose value from input
value = float(raw_input("Calculate Polynomial at value: "))

result_poly = p(value)
result_produt = calc_poly(value, roots)

eps = 1e-14

print "Exact result: %g; result of product function: %g" % (result_poly, result_produt)

if abs(result_poly - result_produt) < eps:
    print "Results are equal within %g" % (eps)
else:
    print "Results are not equal within %g" % (eps)