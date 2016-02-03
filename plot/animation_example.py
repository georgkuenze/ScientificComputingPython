# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 19:53:37 2015

@author: Georg
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time, glob, os

for filename in glob.glob('_tmp*.png'):
    os.remove(filename)

def Gauss(x, m, s):
    s = float(s)
    return (1.0/(np.sqrt(2*np.pi)*s))*np.exp(-0.5*((x-m)/s)**2)

m = 0
s_min = 0.2
s_max = 2.0
x = np.linspace(m - 3*s_max, m + 3*s_max, 1000)
s_values = np.linspace(s_min, s_max, 10)
max_f = Gauss(m, m, s_min)

fig = plt.figure()
plt.axis([x[0], x[-1], 0, max_f])
lines = plt.plot([], [])
plt.xlabel('X')
plt.ylabel('Y')

def init():
    lines[0].set_data([], [])
    return lines
    
def frame(args):
    frame_no, s, x, lines = args
    y = Gauss(x, m, s)
    lines[0].set_data(x, y)
    return lines

all_args = [(frame_no, s, x, lines)
            for frame_no, s in enumerate(s_values)]

anim = animation.FuncAnimation(fig, frame, all_args, interval=250, init_func=init, blit=True)
#anim.save('movie1.mp4', fps=5)
plt.show()