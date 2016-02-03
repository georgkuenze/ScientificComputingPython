# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 21:44:30 2015

@author: Georg
"""

import numpy
import glob, os
import matplotlib.pyplot as plt

def random_walk(np, ns, plot_step):
    # Delete old temporary image files
    for filename in glob.glob('temp_*.png'):
        os.remove(filename)    
    
    # Create array which holds the particles' x and y coordinates
    x_coor = numpy.zeros(np)
    y_coor = numpy.zeros(np)
    
    # Boundary conditions
    x_L = -10; x_H = 10; y_L = -10; y_H = 10    
    
    # Generate ns times random walks 
    walks = numpy.random.random_integers(1,4, size=ns*np)
    walks.shape = (ns, np)
    
    # Plot settings
    no_plots = ns//plot_step # integer divison!
    plt.ion()
    lines = [plt.plot([],[], ls='None', c='k')[0] for _ in range(2)]
    lines[0].set_data([x_L, x_H, x_H, x_L, x_L], [y_L, y_L, y_H, y_H, y_L])
    lines[0].set_linestyle('-')
    lines[0].set_linewidth(2.0)
    lines[0].set_color('b')
    xymax = 2*numpy.sqrt(ns); xymin = -xymax
    plt.axis([xymin, xymax, xymin, xymax])
    counter = 0    
    
    # Loop over ns times random walks and update x,y coordinates
    for step in range(ns):
        this_walk = walks[step,:]
        y_coor += numpy.where(this_walk == 1, 1, 0)        # Step to NORTH == 1
        y_coor  = numpy.where(y_coor > y_H, y_H, y_coor)   # Set y back to y_H
        
        y_coor -= numpy.where(this_walk == 2, 1, 0)        # Step to SOUTH == 2
        y_coor  = numpy.where(y_coor < y_L, y_L, y_coor)   # Set y back to y_L
        
        x_coor -= numpy.where(this_walk == 3, 1, 0)        # Step to WEST  == 3
        x_coor  = numpy.where(x_coor < x_L, x_L, x_coor)   # Set x back to x_L
        
        x_coor += numpy.where(this_walk == 4, 1, 0)        # Step to EAST  == 4
        x_coor  = numpy.where(x_coor > x_H, x_H, x_coor)   # Set x back to x_H
        
        if (step+1) % plot_step == 0:
            lines[1].set_data(x_coor, y_coor)
            lines[1].set_marker('o')
            plt.draw()
            plt.savefig('tmp_%04d.png' % (counter))
            plt.pause(0.1)
            counter += 1
    
    return x_coor, y_coor

np         = 10
ns         = 400
plot_step  = 20

x_coor, y_coor = random_walk(np, ns, plot_step)