# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 17:32:48 2015

@author: Georg
"""

class Line:
    def __init__(self, p1, p2):
        if isinstance(p1, (tuple, list)) and isinstance(p2, (tuple, list)):
            self.a = (p2[1] - p1[1])/float((p2[0] - p1[0]))
            self.b = p2[1] - self.a*p2[0]
        elif isinstance(p1, (float, int)) and isinstance(p2, (tuple, list)):
            self.a = float(p1)
            self.b = p2[1] - self.a*p2[0]
        elif isinstance(p1, (tuple, list)) and isinstance(p2, (float, int)):
            self.a = (p2[1] - p1[1])/float((p2[0] - p1[0]))
            self.b = float(p2)
        elif isinstance(p1, (float, int)) and isinstance(p2, (float, int)):
            self.a = float(p1)
            self.b = float(p2)
    
    def __call__(self, x):
        return self.a*x + self.b