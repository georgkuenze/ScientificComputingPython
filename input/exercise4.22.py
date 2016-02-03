# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 17:26:32 2015

@author: Georg
"""

from scitools.StringFunction import StringFunction
from math import *
import random

def equal_v1(expr1, expr2, A=-100, B=100, n=1000):
    f1 = StringFunction(expr1, independent_variables=('a', 'b'))
    f2 = StringFunction(expr2, independent_variables=('a', 'b'))
    counter = 0    
    for i in range(n):
        a = float(random.uniform(A,B))
        b = float(random.uniform(A,B))
        try:
            f1(a,b) and f2(a,b)
        except ValueError:
            a = abs(a)
            b = abs(b)
        if f1(a,b) != f2(a,b):
            counter += 1
        else:
            continue
    return (counter/float(n))*100

def equal_v2(expr1, expr2, A=-100, B=200, n=1000, eps=1.0e-16):
    f1 = StringFunction(expr1, independent_variables=('a', 'b'))
    f2 = StringFunction(expr2, independent_variables=('a', 'b'))
    counter = 0    
    for i in range(n):
        a = float(random.uniform(A,B))
        b = float(random.uniform(A,B))
        try:
            f1(a,b) and f2(a,b)
        except ValueError:
            a = abs(a)
            b = abs(b)
        if abs(f1(a,b) - f2(a,b)) > eps:
            counter += 1
        else:
            continue
    return (counter/float(n))*100

functions = [('a-b', '-(b-a)'), ('(a/b)', '1/(b/a)'), ('(a*b)**4', '(a**4 * b**4)'), ('(a+b)**2', 'a**2 + (2*a*b) + b**2'),
             ('(a+b)*(a-b)', 'a**2 - b**2'), ('exp(a+b)', 'exp(a)*exp(b)'), ('log(a**b)', 'b*log(a)'), ('log(a*b)', 'log(a)+log(b)'),
             ('a*b', 'exp(log(a)+log(b))'), ('1/(1/a + 1/b)', '(a*b)/(a+b)'), ('a*(sin(b)**2 + cos(b)**2)', 'a'),
             ('sinh(a+b)', '(exp(a)*exp(b) - exp(-a)*exp(-b))/2.0'), ('tan(a+b)', 'sin(a+b)/cos(a+b)'), ('sin(a+b)', 'sin(a)*cos(b) + sin(b)*cos(a)')
             ]

failure_rate_v1 = []

for i in range(len(functions)):
    rate = equal_v1(functions[i][0], functions[i][1])
    failure_rate_v1.append(rate)

print "Failure rate of rounding errors at tolerance = 1.0e-16\n%s" % ('-'*87)
print "%30s %40s %10s" % ('Equation 1', 'Equation 2', 'Error')
for func, rate in zip(functions, failure_rate_v1):
    print "%30s = %38s %13.2f %%" % (func[0], func[1], rate)

eps = 1.0e-12 
failure_rate_v2 = []

for i in range(len(functions)):
    rate = equal_v2(functions[i][0], functions[i][1], eps=eps)
    failure_rate_v2.append(rate)
    
print "\nFailure rate of rounding errors at tolerance = %.1e\n%s" % (eps, '-'*87)
print "%30s %40s %10s" % ('Equation 1', 'Equation 2', 'Error')
for func, rate in zip(functions, failure_rate_v2):
    print "%30s = %38s %13.2f %%" % (func[0], func[1], rate)