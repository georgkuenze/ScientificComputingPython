# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 11:45:41 2015

@author: Georg
"""

def sum_1k(M):
    k = 1
    summe = 0
    for i in range(k,M+1):
        summe += 1/float(i)
    return summe

def test_sum_1k():
    M = 5
    result = 2.25 + 1/30.
    success = result == sum_1k(M)
    if success is True:
        print "Sum function works."
    msg = "%s failed" % sum_1k.__name__
    assert success, msg

test_sum_1k()