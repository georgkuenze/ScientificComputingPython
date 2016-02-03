# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 22:11:04 2015

@author: Georg
"""

class GrowthLogistic:
    def __init__(self, show_plot_on_screen = False):
        self.experiments = []
        self.remove_plot_files()
        self.show_plot_on_screen = show_plot_on_screen
    
    def run_one(self, y0, q, N):
        """Run one experiment."""
        import numpy as np
        import matplotlib.pyplot as plt
        y = np.zeros(N+1)
        index_set = range(N+1)
        y[0] = y0
        for n in index_set[1:]:
            y[n] = y[n-1] + q*y[n-1]*(1-y[n-1])
        
        plotfile = 'logistic_y0_%.2f_q_%.1f_N_%d.png' % (y0, q, N)
        self.experiments.append({'y0': y0, 'q': q, 'N': N, 'mean': np.mean(y[20:]),
                                 'y': y, 'plotfile': plotfile})
        
        plt.plot(range(len(y)), y, 'b-')
        plt.xlabel('N')
        plt.ylim(0, 1.1)
        plt.title('Logistic Growth for y0 = %.2f and q = %.2f' % (y0, q))
        plt.savefig('logistic_y0_%.2f_q_%.1f_N_%d.png' % (y0, q, N))
                
        if self.show_plot_on_screen == False:
            plt.clf()
        
    def run_many(self, y0_list, q_list, N):
        """Run many experiments."""
        for q in q_list:
            for y0 in y0_list:
                self.run_one(y0, q, N)
    
    def remove_plot_files(self):
        """Remove plot files with names 'logistic_y0*.png'."""
        import glob, os
        for plotfile in glob.glob('logistic_y0*.png'):
            os.remove(plotfile)
    
    def report(self, filename='report.html'):
        """
        Generate an HTML report with plots of all 
        experiments generated so far.
        """
        outfile = open('report.html', 'w')
        outfile.write('<html>\n<body>\n')
        for e in self.experiments:
            outfile.write('<p><img src="%s">\n' % e['plotfile'])
        outfile.write('</html>\n</body>')
        outfile.close()

__all__ = ['GrowthLogistic']