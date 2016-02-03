# -*- coding: utf-8 -*-
"""
Created on Wed Sep 02 10:29:10 2015

@author: Georg
"""

class Integrator:
    def __init__(self, a, b, n):
        self.a, self.b, self.n = a, b, n
        self.points, self.weights = self.construct_method()
    
    def construct_method(self):
        raise NotImplementedError('No integration rule in class %s' 
        % self.__class__.__name__)
    
    def integrate(self, f):
        s = 0
        for i in range(len(self.points)):
            s += self.weights[i] * f(self.points[i])
        return s
    
    def vectorized_integrate(self, f):
        import numpy as np
        return np.dot(self.weights, f(self.points))

class Midpoint(Integrator):
    def construct_method(self):
        import numpy as np
        a, b, n = self.a, self.b, self.n
        h = (b-a)/float(n)
        x = np.linspace(a+0.5*h, b-0.5*h, n)
        w = np.zeros(len(x)) + h
        return x, w

class Trapezoidal(Integrator):
    def construct_method(self):
        import numpy as np
        a, b, n = self.a, self.b, self.n
        h = (b-a)/(float(n) - 1)
        x = np.linspace(a, b, n)
        w = np.zeros(len(x)) + h
        w[0]  /= 2.0
        w[-1] /= 2.0
        return x, w

class Simpson(Integrator):
    def construct_method(self):
        import numpy as np
        if self.n % 2 != 1:
            print 'n=%d must be odd, 1 is added' % self.n
            self.n += 1
        a, b, n = self.a, self.b, self.n
        h = 2*(b-a)/(float(n)-1)
        x = np.linspace(a, b, n)
        w = np.zeros(len(x))
        w[0]  = h/6.0
        w[2:-2:2] = h/3.0
        w[1:-1:2] = 2*h/3.0
        w[-1] = h/6.0
        return x, w
    
class GaussLegendre2(Integrator):
    def construct_method(self):
        import numpy as np
        if self.n % 2 != 0:
            print 'n=%d must be even, 1 is substracted' % self.n
            self.n -= 1
        a, b, n = self.a, self.b, self.n
        h = 2*(b-a)/float(n)
        x = np.zeros(n)
        for i in range(0, n-1, 2):
            x[i]   = a + (i*0.5+0.5)*h - h/(2.0*np.sqrt(3))
            x[i+1] = a + (i*0.5+0.5)*h + h/(2.0*np.sqrt(3))
        w = np.zeros(len(x)) + h/2.0
        return x, w

class MonteCarlo(Integrator):
    def construct_method(self):
        a, b, n = self.a, self.b, self.n
        n *= 10**3
        import numpy as np
        x = np.random.uniform(a, b, n)
        w = np.zeros(len(x)) + (b-a)/float(n)
        return x, w
        
__all__ = ['Integrator', 'Midpoint', 'Trapezoidal', 'Simpson', 'GaussLegendre2', 'MonteCarlo']   