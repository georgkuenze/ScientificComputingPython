# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 23:03:04 2015

@author: Georg
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 22:33:46 2015

@author: Georg
"""

import numpy
import glob, os
import matplotlib.pyplot as plt

def random_walk(np, ns, plot_step):
    # Delete old temporary image files
    for filename in glob.glob('temp_*.png'):
        os.remove(filename)

    # Boundary conditions
    x_L = 0; x_H = 1; y_L = 0; y_H = 1      
    
    # Create array which holds the particles' x and y coordinates
    # Initial coordinates are uniformly distributed in left half of box
    x_coor = numpy.random.uniform(0, 0.5*x_H, np)
    y_coor = numpy.random.uniform(0, y_H, np)       
    
    # Generate ns times random walks 
    walks = numpy.random.random_integers(1,4, size=ns*np)
    walks.shape = (ns, np)
    
    # Plot settings
    no_plots = ns//plot_step # integer divison!
    plt.ion()
    lines = [plt.plot([],[], ls='None', c='k')[0] for _ in range(2)]
    lines[0].set_data([x_L, x_H, x_H, x_L, x_L, 0.5*x_H, 0.5*x_H, 0.5*x_H, 0.5*x_H], \
    [y_L, y_L, y_H, y_H, y_L, y_L, 0.45*y_H, 0.55*y_H, y_H])
    lines[0].set_linestyle('-')
    lines[0].set_linewidth(2.0)
    lines[0].set_color('b')
    lines[1].set_data(x_coor, y_coor)
    lines[1].set_marker('o')
    xymax = 0.25*x_H+x_H; xymin = -0.25*x_H+x_L
    plt.axis([xymin, xymax, xymin, xymax])
    plt.draw()
    plt.savefig('tmp_%04d.png' % (0))
    counter = 0    
    
    # Loop over ns times random walks and update x,y coordinates
    for step in range(ns):
        this_walk = walks[step,:]
        y_coor += numpy.where(this_walk == 1, 0.1, 0)      # Step to NORTH == 1
        y_coor  = numpy.where(y_coor > y_H, y_H, y_coor)   # Set y back to upper limit of box
        
        y_coor -= numpy.where(this_walk == 2, 0.1, 0)      # Step to SOUTH == 2
        y_coor  = numpy.where(y_coor < y_L, y_L, y_coor)   # Set y back to lower limit of box
        
        x_coor_prev = numpy.copy(x_coor)   # Make a copy which holds previous x-coordinates
        x_coor -= numpy.where(this_walk == 3, 0.1, 0)      # Step to WEST  == 3
        x_coor  = numpy.where(numpy.logical_and(
        x_coor <= 0.5*x_H, 0.5*x_H <= x_coor_prev), 0.5*x_H, x_coor)   # Particles are not allowed to cross middle section
        x_coor  = numpy.where(numpy.logical_and(numpy.logical_and(
        0.45 < y_coor, y_coor < 0.55), this_walk == 3), x_coor_prev - 0.1, x_coor) # Allow Particles to cross middle section
        x_coor  = numpy.where(x_coor < x_L, x_L, x_coor)   # Set x back to left limit of box

        x_coor_prev = numpy.copy(x_coor)   # Make a copy which holds previous x-coordinates
        x_coor += numpy.where(this_walk == 4, 0.1, 0)      # Step to EAST  == 4
        x_coor  = numpy.where(numpy.logical_and(
        x_coor_prev <= 0.5*x_H, 0.5*x_H <= x_coor), 0.5*x_H, x_coor)   # Particles are not allowed to cross middle section
        x_coor  = numpy.where(numpy.logical_and(numpy.logical_and(
        0.45 < y_coor, y_coor < 0.55), this_walk == 4), x_coor_prev + 0.1, x_coor) # Allow Particles to cross middle section
        x_coor  = numpy.where(x_coor > x_H, x_H, x_coor)   # Set x back to right limit of box
        
        if (step+1) % plot_step == 0:
            lines[1].set_data(x_coor, y_coor)
            lines[1].set_marker('o')
            plt.draw()
            plt.savefig('tmp_%04d.png' % (counter+1))
            plt.pause(0.1)
            counter += 1
    
    return x_coor, y_coor

np = 10000
ns = 100
plot_step = 1
x_coor, y_coor = random_walk(np, ns, plot_step)