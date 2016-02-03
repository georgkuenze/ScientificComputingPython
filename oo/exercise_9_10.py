# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 23:45:03 2015

@author: Georg
"""
import numpy as np

class Differentiation:
    table = {
    ('central', 2):  [0, 0, 0, -0.5, 0, 0.5, 0, 0, 0],
    ('central', 4):  [0, 0, 1./12, -2./3, 0, 2./3, -1./12, 0, 0],
    ('central', 6):  [0, -1./60, 3./20, -0.75, 0, 0.75, -3./20, 1./60, 0],
    ('central', 8):  [1./280, -4./105, 12./60, -0.8, 0, 0.8, -12./60, 4./105, -1./280],
    ('forward', 1):  [0, 0, 0, 0, 1, 1, 0, 0, 0],
    ('forward', 3):  [0, 0, 0, -1./3, -0.5, 1, -1./6, 0, 0],
    ('backward', 1): [0, 0, 0, -1, 1, 0, 0, 0, 0],
    ('backward', 3): [0, 0, 0.5, -2, 1.5, 0, 0, 0, 0]   
    }
    
    def __init__(self, f, h=1.0E-5, type='central', order=2):
        self.f, self.h, self.type, self.order = f, h, type, order
        self.weights = np.array(Differentiation.table[(type, order)])
        
    def __call__(self, x):
        f_values = np.array([self.f(x+i*self.h) for i in range(-4,5)])
        return np.dot(self.weights, f_values)/self.h

d = Differentiation(lambda x: np.sin(x), type='central', order=4)
approx = d(np.pi)
exact = np.cos(np.pi)
print 'Approximation with Instance of Class %s: %g; Exact Result: %g' % (d.__class__.__name__, approx, exact)