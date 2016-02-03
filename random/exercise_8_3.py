# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:11:54 2015

@author: Georg
"""
import random

colors = ['black', 'white', 'green', 'blue', 'red', 'yellow', 'orange', 'brown', 'purple', 'cyan']

result = random.choice(colors)

print 'Colors are: ',
print '%s' % ([i for i in colors]),
print 'Color picked randomly: %s' % (result)