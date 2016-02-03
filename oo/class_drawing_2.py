# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 19:28:45 2015

@author: Georg
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 02 23:15:01 2015

@author: Georg
"""

from pysketcher import *

R = 1     # Radius of wheel
L = 4     # Distance between wheels
H = 2     # Height of vehicle body
w_1 = 5   # Position of front wheel

xmax=w_1 + 2*L + 3*R
drawing_tool.set_coordinate_system(xmin=0, xmax=xmax, ymin=-1, ymax=2*R + 3*H, axis=False)

wheel1 = Composition({'wheel': Circle(center=(w_1, R), radius=R),
                      'cross': Composition({'cross1': Line((w_1,0), (w_1, 2*R)),
                                            'cross2': Line((w_1-R,R), (w_1+R,R))})})
wheel2 = wheel1.copy()
wheel2.translate((L,0))

under = Rectangle(lower_left_corner=(w_1-2*R, 2*R), width=2*R+L+2*R, height=H)
over = Rectangle(lower_left_corner=(w_1, 2*R+H), width=2.5*R, height=1.25*H)

wheels = Composition({'wheel1': wheel1, 'wheel2': wheel2})
body   = Composition({'under': under, 'over': over})
vehicle = Composition({'wheels': wheels, 'body': body})

ground = Wall(x=[R, xmax], y=[0, 0], thickness=-0.3*R)

fig2 = Composition({'vehicle': vehicle, 'ground': ground})
fig2.draw()
drawing_tool.display()
drawing_tool.savefig('tmp1.png')
drawing_tool.savefig('tmp1.pdf')

fig2['vehicle']['wheels'].set_filled_curves('blue')
fig2['vehicle']['wheels'].set_linewidth(6)
fig2['vehicle']['wheels'].set_linecolor('black')
fig2['vehicle']['body']['under'].set_filled_curves('red')
fig2['vehicle']['body']['over'].set_filled_curves(pattern='/')
fig2['vehicle']['body']['over'].set_linewidth(14)

drawing_tool.erase()  # avoid drawing old and new fig2 on top of each other
fig2.draw()
drawing_tool.display()
drawing_tool.savefig('tmp2.png')
drawing_tool.savefig('tmp2.pdf')

print fig2
fig2.recurse('fig2')
fig2.graphviz_dot('fig2', False)

from math import degrees
w_1 += L                           # Start position
fig2['vehicle'].translate((L,0))   # move to starting point for driving

def v(t):
    return -8*R*t*(1 - t/(2*R))

def move(t, fig2):
    x_displacement = dt*v(t)
    fig2['vehicle'].translate((x_displacement, 0))
    
    # Rotate wheels
    global w_1
    w_1 += x_displacement
    angle = -x_displacement/float(R)
    w1 = fig2['vehicle']['wheels']['wheel1']
    w1.rotate(degrees(angle), center=(w_1, R))
    w2 = fig2['vehicle']['wheels']['wheel2']
    w2.rotate(degrees(angle), center=(w_1+L, R))
    
import numpy
tp = numpy.linspace(0, 2*R, 25)
dt = tp[1]- tp[0]

files = animate(fig2, tp, move, moviefiles=True, pause_per_frame=0.2)