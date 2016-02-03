# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 10:22:03 2015

@author: Georg
"""
import numpy as np

# Define Simpson function
# a and b are the boundaries of the integral
def Simpson(f, a, b, n=500):
    """
    Return the approximation of the integral of f
    from a to b using Simpson's rule with n intervals
    """
    
    # Validity tests
    if a > b:
        print "Error: a=%g > b=%g" % (a,b)
        return None
    # Check that n is an even number
    if n % 2 != 0:
        print "Error: n is not an even integer. Make n=%g to n+1=%g" % (n, n+1)
        n = n+1 # Make n an even integer
        
    h = (b-a)/float(n)
    sum1 = 0
    for i in range(1, n/2 + 1):
        sum1 += f(a + (2*i - 1)*h)
    
    sum2 = 0
    for i in range(1, n/2):
        sum2 += f(a + 2*i*h)
    
    integral = (b-a)/(3*float(n))*(f(a) + f(b) + 4*sum1 + 2*sum2)
    return integral

# Test Simpson function on polynomial
# Create 2nd order Polynomial
p = np.poly1d([2,3,2])
# Calculate integral of p
P = np.polyint(p)

# define boundaries of integral
a = 0
b = 2
# Define error
eps = 1e-14

int_exact = P(b) - P(a)
int_simpson = Simpson(p, a, b)

print "Integral exact polynomial: %.2f" % (int_exact)
print "Integral with Simpson func: %.2f" % (int_simpson)
print "Simpson function is exact within 1E-14" if abs(int_exact - int_simpson) < eps else "Simpson function is not exact"
print 

# Apply Simpson function to 1.5*sin(x)
f = lambda x: 1.5*np.sin(x)**3
F = lambda x: 0.5*np.cos(x)*(np.cos(x)**2 - 3)

# Define boundaries
a = 0
b = np.pi

# Make while loop
i = 5
n = 1000
while i <= n:
    int_simpson = Simpson(f, a, b, n=i)
    int_exact = F(b) -F(a)
    app_error = abs(int_exact - int_simpson)
    print "n= %3.d; Integral Simpson: %.8f; Integral exact: %.8f; Approximation error: %g" % (i, int_simpson, int_exact, app_error)
    i *= 5

# Make a test function for Simpson function
def test_Simpson():
    a = 0
    b = 2
    n = 10
    f = lambda x: 2*x**2 + 3*x + 3
    F = lambda x: (2/3.)*x**3 + 1.5*x**2 + 3*x
    int_exact = F(b) - F(a)
    int_simpson = Simpson(f, a, b, n)
    app_error = abs(int_exact - int_simpson)
    print "Simpson function is exact within error of %g for %d intervals" % (app_error, n)

print "\nTest Simpson function"
test_Simpson()