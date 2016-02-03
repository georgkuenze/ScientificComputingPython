# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 20:29:40 2015

@author: Georg
"""

from numpy import *

class Polynomial:
    def __init__(self, coefficients):
        if isinstance(coefficients, (list, ndarray)):
            self.coeff = array(coefficients)
    
    def __call__(self, x):
        x_arr = ones_like(self.coeff)*x
        s = sum(self.coeff*x_arr)
        return s
    
    def __add__(self, other):
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:len(other.coeff)] + other.coeff
            result_coeff = concatenate((result_coeff, self.coeff[len(other.coeff):]), axis=1)
        elif len(self.coeff) < len(other.coeff):
            result_coeff = other.coeff[:len(self.coeff)] + self.coeff
            result_coeff = concatenate((result_coeff, other.coeff[len(self.coeff):]), axis=1)
        else:
            result_coeff = self.coeff + other.coeff
        return Polynomial(result_coeff)
        
    def __sub__(self, other):
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:len(other.coeff)] - other.coeff
            result_coeff = concatenate((result_coeff, self.coeff[len(other.coeff):]), axis=1)
        elif len(self.coeff) < len(other.coeff):
            result_coeff = -1*other.coeff[:len(self.coeff)] + self.coeff
            result_coeff = concatenate((result_coeff, -1*other.coeff[len(self.coeff):]), axis=1)
        else:
            result_coeff = self.coeff - other.coeff
        return Polynomial(result_coeff)
        
    def __mul__(self, other):
        result_coeff = zeros(len(self.coeff)+len(other.coeff)+1)
        for i in range(len(self.coeff)):
            for j in range(len(other.coeff)):
                result_coeff[i+j] += self.coeff[i]*other.coeff[j]
        return Polynomial(result_coeff)
    
    def derivative(self):
        result_coeff = linspace(1, len(self.coeff)-1, len(self.coeff)-1) * self.coeff[1:]
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