# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 14:52:48 2015

@author: Georg
"""

class Particle:
    def __init__(self, no, x, y, step):
        self.no   = no
        self.x    = x
        self.y    = x
        self.step = step
    
    def move(self, direction):
        self.step += 1
        
        # Comment: 1 is NORTH, 2 is SOUTH, 3 is WEST, 4 is EAST  
        if direction == 1:
            self.y += 1
        elif direction == 2:
            self.y -= 1
        elif direction == 3:
            self.x -= 1
        elif direction == 4:
            self.x += 1
    
    def __str__(self):
        return 'Particle %d, step = %d: x = %4d, y = %4d' \
        % (self.no, self.step, self.x, self.y)
    
    def __repr__(self):
        return self.__str__()

class Particles:
    def __init__(self, np, ns, plot_step, test=False):
        # Initialize attributes        
        self.particles = []
        self.np        = np
        self.ns        = ns
        self.plot_step = plot_step
        self.steps     = 0
        if test == True:
            self.seed = 10
        elif test == False:
            self.seed = None
        # Create a list of Particle instances
        for k in range(self.np):
            self.particles.append(Particle(k+1, 0, 0, 0))
        
    def move(self):
        import random
        for k in range(self.np):
            random.seed(self.seed)
            direction = random.randint(1, 4)
            self.particles[k].move(direction)
        self.steps += 1 # Update steps number
        
    def moves(self, plot=False):
        import glob, os
        import matplotlib.pyplot as plt     
        from math import sqrt
        
        # Delete old temporary image files
        for filename in glob.glob('temp_*.png'):
            os.remove(filename)
            
        # Random Walk of Particles without plotting
        if plot == False:
            for step in range(self.ns):
                self.move()
                
        # Random Walk of Particles with plotting
        elif plot == True:
            # Plot settings
            no_plots = self.ns//self.plot_step # integer divison!
            plt.ion()
            lines = [plt.plot([],[], ls='None', marker='o', c='k')[0] \
            for _ in range(no_plots)]
            xymax = 3*sqrt(self.ns); xymin = -xymax
            plt.axis([xymin, xymax, xymin, xymax])
            counter = 0
            # Loop over ns steps
            for step in range(self.ns):
                self.move()
                # Condition is true for every plot step
                if (step+1) % self.plot_step == 0:
                    x = [self.particles[i].x for i in range(self.np)]
                    y = [self.particles[i].y for i in range(self.np)]
                    lines[counter].set_data(x,y)
                    plt.draw()
                    plt.savefig('tmp_%04d.png' % (counter))
                    plt.pause(0.1)
                    counter += 1
                    
    def analysis(self):
        import numpy as np
        x_all  = np.array([self.particles[i].x for i in range(self.np)])
        y_all  = np.array([self.particles[i].y for i in range(self.np)])
        x_mean = np.mean(x_all); y_mean = np.mean(y_all)
        x_std  = np.std(x_all);  y_std  = np.std(y_all)
        print 'Distribution of %d particles after %d steps:' % (self.np, self.steps)
        print 'x = %4d +/- %.1f\ny = %4d +/- %.1f' % (x_mean, x_std, y_mean, y_std)
    
    def __str__(self):
        import pprint
        s = []
        for k in range(self.np):
            s += [self.particles[k].__str__()]
        return pprint.pformat(s, indent=1, width=1)
    
    def __repr__(self):
        return self.__str__()

class Particles_vec:
    def __init__(self, np, ns, plot_step, test=False):
        import numpy
        # Initialize attributes        
        self.np        = np
        self.x_coor    = numpy.zeros(np)
        self.y_coor    = numpy.zeros(np)
        self.ns        = ns
        self.plot_step = plot_step
        self.steps     = 0
        if test == True:
            self.seed  = 10
        elif test == False:
            self.seed  = None
        
        # Create an np x ns array of random moves
        numpy.random.seed(self.seed)        
        self.walks     = numpy.random.random_integers(1,4, size=ns*np)
        self.walks.shape = (ns, np)
        
    def moves(self, plot=False):
        import numpy
        import glob, os
        import matplotlib.pyplot as plt     
        
        # Delete old temporary image files
        for filename in glob.glob('temp_*.png'):
            os.remove(filename)
            
        # Random Walk of Particles without plotting
        # Comment: 1 is NORTH, 2 is SOUTH, 3 is WEST, 4 is EAST
        if plot == False:
            for step in range(self.ns):
                this_walk = self.walks[step,:]
                self.y_coor += numpy.where(this_walk == 1, 1, 0)
                self.y_coor -= numpy.where(this_walk == 2, 1, 0)
                self.x_coor -= numpy.where(this_walk == 3, 1, 0)
                self.x_coor += numpy.where(this_walk == 4, 1, 0)
                self.steps  += 1 # Update steps number
                
        # Random Walk of Particles with plotting
        elif plot == True:
            # Plot settings
            no_plots = self.ns//self.plot_step # integer divison!
            plt.ion()
            lines = [plt.plot([],[], ls='None', marker='o', c='k')[0] \
            for _ in range(no_plots)]
            xymax = 3*numpy.sqrt(self.ns); xymin = -xymax
            plt.axis([xymin, xymax, xymin, xymax])
            counter = 0
            # Loop over ns steps
            for step in range(self.ns):
                this_walk = self.walks[step,:]
                self.y_coor += numpy.where(this_walk == 1, 1, 0)
                self.y_coor -= numpy.where(this_walk == 2, 1, 0)
                self.x_coor -= numpy.where(this_walk == 3, 1, 0)
                self.x_coor += numpy.where(this_walk == 4, 1, 0)
                self.steps  += 1 # Update steps number
                
                # Condition is true for every plot step
                if (step+1) % self.plot_step == 0:
                    lines[counter].set_data(self.x_coor, self.y_coor)
                    plt.draw()
                    plt.savefig('tmp_%04d.png' % (counter))
                    plt.pause(0.1)
                    counter += 1
    
    def analysis(self):
        import numpy
        x_mean = numpy.mean(self.x_coor); y_mean = numpy.mean(self.y_coor)
        x_std  = numpy.std(self.x_coor);  y_std  = numpy.std(self.y_coor)
        print 'Distribution of %d particles after %d steps:' % (self.np, self.steps)
        print 'x = %4d +/- %.1f\ny = %4d +/- %.1f' % (x_mean, x_std, y_mean, y_std)
    
    def __str__(self):
        s = ''.join(['Particle %d, step = %d: x = %4d, y = %4d\n' \
        % (i+1, self.steps, self.x_coor[i], self.y_coor[i]) for i in range(self.np)])
        return s
        
    def __repr__(self):
        return self.__str__()
        
def random_walk_2D(np, ns, seed=None):
    import random
    x_coor = [0]*np
    y_coor = [0]*np
    for step in range(ns):
        for i in range(np):
            if seed != None:
                random.seed(seed)
                direction = random.randint(1,4)
                
                if direction == 1:
                    y_coor[i] += 1
                elif direction == 2:
                    y_coor[i] -= 1
                elif direction == 3:
                    x_coor[i] -= 1
                elif direction == 4:
                    x_coor[i] += 1
                
            elif seed == None:
                direction = random.randint(1,4)
                
                if direction == 1:
                    y_coor[i] += 1
                elif direction == 2:
                    y_coor[i] -= 1
                elif direction == 3:
                    x_coor[i] -= 1
                elif direction == 4:
                    x_coor[i] += 1
                
    return x_coor, y_coor
    
def random_walk_2D_vec(np, ns, seed=None):
    import numpy
    x_coor = numpy.zeros(np)
    y_coor = numpy.zeros(np)
    
    if seed != None:
        numpy.random.seed(seed)
        walks = numpy.random.random_integers(1,4, size=ns*np)
        walks.shape = (ns, np)
    elif seed == None:
        walks = numpy.random.random_integers(1,4, size=ns*np)
        walks.shape = (ns, np)
    
    for step in range(ns):
        this_walk = walks[step,:]
        y_coor += numpy.where(this_walk == 1, 1, 0)
        y_coor -= numpy.where(this_walk == 2, 1, 0)
        x_coor -= numpy.where(this_walk == 3, 1, 0)
        x_coor += numpy.where(this_walk == 4, 1, 0)
    
    return x_coor, y_coor
    
def test_Particles():
    import sys
    
    # Read parameter for test function from command line if provided
    np   = int(sys.argv[2])
    ns   = int(sys.argv[3])
    seed = 10 # Same seed as in Class Particle when used in test mode
    
    p = Particles(np, ns, 10, test=True) # Make Class instance in test mode
    x_random_walk, y_random_walk = random_walk_2D(np, ns, seed)
    p.moves()
    x_particles = [p.particles[i].x for i in range(np)]
    y_particles = [p.particles[i].y for i in range(np)]
    
    success = (x_random_walk == x_particles and y_random_walk == y_particles)
    if success:
        print 'Test of Class Particles was successful!'
    assert success, 'Test unseccessful. Got different results with Function and Class Particles.'

def test_Particles_vec():
    import sys
    
    # Read parameter for test function from command line if provided
    np   = int(sys.argv[2])
    ns   = int(sys.argv[3])
    seed = 10 # Same seed as in Class Particle when used in test mode
    
    p = Particles_vec(np, ns, 10, test=True) # Make Class instance in test mode
    x_random_walk, y_random_walk = random_walk_2D_vec(np, ns, seed)
    p.moves()
    x_particles = p.x_coor; y_particles = p.y_coor
    
    success = (all(x_random_walk == x_particles) and all(y_random_walk == y_particles))
    if success:
        print 'Test of Class Particles_vec was successful!'
    assert success, 'Test unseccessful. Got different results with Function and Class Particles_vec.'    
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 4 and sys.argv[1] == 'test_Particles':
        test_Particles() # Read np, ns from cml and call test function.
    elif len(sys.argv) >= 4 and sys.argv[1] == 'test_Particles_vec':
        test_Particles_vec() # Read np, ns from cml and call test function.
    elif len(sys.argv) < 4:
        sys.argv = [sys.argv[0], None, 4, 100] # Set np, ns manually, when not provided from cml.
        test_Particles()
        test_Particles_vec()
    
__all__ = ['Particle', 'Particles', 'Particles_vec', 'random_walk_2D', 'random_walk_2D_vec', 'test_Particles', 'test_Particles_vec']