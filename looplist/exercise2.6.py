# -*- coding: utf-8 -*-
"""
Created on Mon Jul 06 16:30:56 2015

@author: Georg
"""

a = 1.
b = 100.
n = 20
liste = [i*((b-a)/n)+a for i in range(n+1)]
for element in liste:
    print '%.2f' % (element),