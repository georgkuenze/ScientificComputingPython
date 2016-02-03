# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 23:00:02 2015

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
        
class F:
    def __init__(self, m):
        self.m = float(m)
        
    def __call__ (self, t):
        return (1 + 1/self.m)*t**(1/self.m)

def error_vs_n(f, exact, n_values, Method, a, b):
    import numpy as np
    log_n   = []
    log_err = []
    for n_value in n_values:
        m = Method(a, b, n_value)
        err = abs(exact - m.integrate(f))
        log_n.append(np.log(n_value))
        log_err.append(np.log(err))
    return log_n, log_err

import matplotlib.pyplot as plt
plt.rc('figure', figsize=(10,10))
fig, axes = plt.subplots(2,2,sharex=False,sharey=False)
plt.subplots_adjust(wspace=0.25, hspace=0.25)

n_values = [10, 20, 40, 80, 160, 320, 640]
m_values = [0.125, 0.25, 2, 8]
Colors = ["black", "red", "blue", "green", "yellow"]
Methods = [Midpoint, Trapezoidal, Simpson, GaussLegendre2, MonteCarlo]
coor = [(0,0), (0,1), (1,0), (1,1)]

for i in range(len(m_values)):
    f = F(m_values[i])
    for Method, Color in zip(Methods, Colors):
        n, e = error_vs_n(f, 1, n_values, Method, 0, 1)
        axes[coor[i]].plot(n, e, marker='o', label=Method.__name__, color=Color)
        axes[coor[i]].set_xlabel('log(n)')
        axes[coor[i]].set_ylabel('log(err)')
        axes[coor[i]].set_title('m = %g' % m_values[i])
        axes[coor[i]].legend(loc=3)

__all__ = ['Integrator', 'Midpoint', 'Trapezoidal', 'Simpson', 'GaussLegendre2', 'MonteCarlo']        