# -*- coding: utf-8 -*-
"""
Created on Thu Aug 06 22:23:10 2015

@author: Georg
"""

def derivative(dic):
    deriv_dic = {}
    for key, value in dic.items():
        if key > 0:        
            deriv_dic[key-1] = key*value
        else:
            pass
    return deriv_dic

p = {0: -3, 3: 2, 5: -1}
derivative = derivative(p)
print derivative