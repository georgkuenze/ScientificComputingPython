# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 23:03:28 2015

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
        
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

# Function to evaluate
def func(x):
    return np.sin(x)

# Function to calculate error from exact integral 
def error_vs_n(f, exact, n_values, Method, a, b):
    log_n   = []
    log_err = []
    for n_value in n_values:
        m = Method(a, b, n_value)
        err = abs(exact - m.integrate(f))
        log_n.append(np.log(n_value))
        log_err.append(np.log(err))
    log_n = np.asarray(log_n)
    log_err = np.asarray(log_err)
    return log_n, log_err

# Function to fit linear curve
def residuals(p, y, x):
    C, r = p
    err = y - (r*x + C)
    return err

fig = plt.figure()
ax = fig.add_subplot(111)

n_values = [2**k+1 for k in range(2,12)]
p0 = [-2, -5] # initial guess for C and r
fit_results = {} 
Colors = ["black", "red", "blue", "green"]
Methods = [Midpoint, Trapezoidal, Simpson, GaussLegendre2]

for Method, Color in zip(Methods, Colors):
    n, e = error_vs_n(func, 1, n_values, Method, 0, np.pi/2.0)
    plsq = optimize.leastsq(residuals, p0, args=(e[:-1], n[:-1]))
    plsq[0][0] = np.e**plsq[0][0]
    fit_results[Method.__name__] = plsq[0]
    ax.plot(n, e, marker='o', label=Method.__name__, color=Color)
ax.set_xlabel('log(n)')
ax.set_ylabel('log(err)')
ax.legend(loc='best')

print '\nFitting results (Error = C*n**r)\n%s' % (32*'-')
print '%-14s %5s %8s' % ('Method', 'C', 'r')
for method in sorted(fit_results):
    print '%-14s: %6.3f %8.3f' % (method, fit_results[method][0], fit_results[method][1])