# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 22:46:35 2015

@author: Georg
"""
from math import pi

class Ellipse:
    def __init__(self, a, b):
        self.a = float(a) # semi-major axis
        self.b = float(b) # semi-minor axis
    
    def area(self):
        from math import pi        
        return pi*self.a*self.b
    
    def circumference(self):
        from math import sqrt, pi, cos, sin
        # Function to approximate the circumference of an ellipse
        f = lambda x: sqrt(self.a**2 * cos(x)**2 + self.b**2 * sin(x)**2)
        h = (0.5*pi - 0.0)/float(1000)
        x = [h*i + 0.0 for i in xrange(1001)]
        integral = 0
        for i in x:
            integral += h*f(i)
        integral += 0.5*h*(0.5*pi + 0.0)
        return 4*integral

class Circle(Ellipse):
    def __init__(self, R):
        Ellipse.__init__(self, R, R)

e = Ellipse(2,4)
print 'Area of ellipse with a = %.2f and b = %.2f: %.2f' % (e.a, e.b, e.area())
print 'Circumference of ellipse with a = %.2f and b = %.2f: %.2f' % (e.a, e.b, e.circumference())
print 

c = Circle(4)
print 'Area of circle with radius = %.2f: %.2f' % (c.a, c.area())
print 'Approximated circumference of circle with radius = %.2f: %.2f' % (c.a, c.circumference())
print 'Exact circumference of circle with radius = %.2f: %.2f' % (c.a, 2*pi*c.a)