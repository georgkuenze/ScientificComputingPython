# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 19:03:15 2015

@author: Georg
"""
from numpy import *

class Polynomial:
    def __init__(self, coefficients):
        if isinstance(coefficients, (list, ndarray)):
            self.coeff = coefficients
    
    def __call__(self, x):
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i
        return s
    
    def __add__(self, other):
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:]
            for i in range(len(other.coeff)):
                result_coeff[i] += other.coeff[i]
        else:
            result_coeff = other.coeff[:]
            for i in range(len(self.coeff)):
                result_coeff[i] += self.coeff[i]
        return Polynomial(result_coeff)
        
    def __sub__(self, other):
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:]
            for i in range(len(other.coeff)):
                result_coeff[i] -= other.coeff[i]
        else:
            result_coeff = other.coeff[:]
            for j in range(len(result_coeff)):
                result_coeff[j] = -1*result_coeff[j]
            for i in range(len(self.coeff)):
                result_coeff[i] += self.coeff[i]
        return Polynomial(result_coeff)
        
    def __mul__(self, other):
        result_coeff = zeros(len(self.coeff)+len(other.coeff)+1)
        for i in range(len(self.coeff)):
            for j in range(len(other.coeff)):
                result_coeff[i+j] += self.coeff[i]*other.coeff[j]
        return Polynomial(result_coeff)
    
    def derivative(self):
        result_coeff = zeros(len(self.coeff)-1)
        for i in range(1, len(self.coeff)):
            result_coeff[i-1] = i*self.coeff[i]
        return Polynomial(result_coeff)
    
    def __str__(self):
        s = ''
        for i in range(0, len(self.coeff)):
            if self.coeff[i] != 0:
                s += ' + %g*x^%d' % (self.coeff[i], i)
        #Fix layout
        s = s.replace('+ -', '- ')
        s = s.replace('*x^0', '')
        s = s.replace(' 1*', ' ')
        s = s.replace('x^1 ', 'x ')
        if s[0:3] == ' + ':
            s = s[3:]
        if s[0:3] == ' - ':
            s = '-' + s[3:]
        return s