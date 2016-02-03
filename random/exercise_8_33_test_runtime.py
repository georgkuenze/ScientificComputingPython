# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 20:13:33 2015

@author: Georg
"""

from exercise_8_33 import *
import time

p1 = Particles(100, 10**3, 10**1)
p2 = Particles_vec(100, 10**3, 10**1)
start = time.clock()
p1.moves()
intermediate = time.clock()
p2.moves()
end = time.clock()

print 'Comparison of run time:'
print 'Class Particle (scalar version): %.1f ms' % ((intermediate-start)*10**3)
print 'Class Particle_vec (vectorized version): %.1f ms' % ((end-intermediate)*10**3)
print 'Vectorized version is %g times faster than scalar version.' % ((intermediate-start)/(end-intermediate))