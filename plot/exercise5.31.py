# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 22:14:15 2015

@author: Georg
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time, glob, os

for filename in glob.glob('_tmp*.png'):
    os.remove(filename)

def wave_packet(x, t):
    y = np.exp(-(x - 3*t)**2)*np.sin(3*np.pi*(x - t))
    return y

x = np.linspace(-6, 6, 1000)
t_min = -1
t_max =  1
t_values = np.linspace(t_min, t_max, 60)

fig = plt.figure()
plt.axis([x[0], x[-1], -1, 1])
lines = plt.plot([], [],)
plt.xlabel('X')
plt.ylabel('Y')

def init():
    lines[0].set_data([], [])
    return lines
    
def frame(args):
    frame_no, x, t, lines = args
    y = wave_packet(x, t)
    lines[0].set_data(x, y)
    return lines

all_args = [(frame_no, x, t, lines) for frame_no, t in enumerate(t_values)]

anim = animation.FuncAnimation(fig, frame, all_args, interval=250, init_func=init, blit=True)
#anim.save('movie1.mp4', fps=5)
plt.show()