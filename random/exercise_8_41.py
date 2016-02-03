# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 23:01:14 2015

@author: Georg
"""

import numpy as np
import pprint
import matplotlib.pyplot as plt

h = 300 # time interval i.e. 1/300

# Read in data and create array
eta = []
infile = open('gauge.dat', 'r')
for line in infile:
    eta.append(float(line))
infile.close()

# Original data
eta = np.asarray(eta)
time = np.arange(len(eta))*1/float(h)

# Compute velocity
velocity = np.zeros(len(eta)-2)
for i in xrange(1, len(eta)-1):
    velocity[i-1] = (eta[i+1] - eta[i-1])/(2*float(h))

# Compute acceleration
acceleration = np.zeros(len(eta)-2)
for i in xrange(1, len(eta)-1):
    acceleration[i-1] = (eta[i+1] - 2*eta[i] + eta[i-1])/(float(h)**2)

# Compute filtered signal
filtered_1 = np.zeros(len(eta)-2)
for i in xrange(1, len(eta)-1):
    filtered_1[i-1] = 0.25*(eta[i+1] + 2*eta[i] + eta[i-1])

# Compute velocity from filtered data
velocity_f1 = np.zeros(len(filtered_1)-2)
for i in xrange(1, len(filtered_1)-1):
    velocity_f1[i-1] = (filtered_1[i+1] - filtered_1[i-1])/(2*float(h))

# Compute acceleration from filtered data
acceleration_f1 = np.zeros(len(filtered_1)-2)
for i in xrange(1, len(filtered_1)-1):
    acceleration_f1[i-1] = (filtered_1[i+1] - 2*filtered_1[i] + filtered_1[i-1])/(float(h)**2)
    
# Apply filter 10 times
template = np.copy(eta)
for i in range(1, 11):
    filtered_2 = np.zeros(len(template)-2)
    for j in xrange(1, len(template)-2):
        filtered_2[j-1] = 0.25*(template[j+1] + 2*template[j] + template[j-1])
    template = filtered_2

# Compute velocity from 10-fold filtered data
velocity_f2 = np.zeros(len(filtered_2)-2)
for i in xrange(1, len(filtered_2)-1):
    velocity_f2[i-1] = (filtered_2[i+1] - filtered_2[i-1])/(2*float(h))
    
# Compute acceleration from 10-fold filtered data
acceleration_f2 = np.zeros(len(filtered_2)-2)
for i in xrange(1, len(filtered_2)-1):
    acceleration_f2[i-1] = (filtered_2[i+1] - 2*filtered_2[i] + filtered_2[i-1])/(float(h)**2)

plt.rc('figure', figsize=(15,15))
fig = plt.figure()
plt.subplots_adjust(hspace=0.4, wspace=0.5)

ax1 = fig.add_subplot(331); ax1.plot(time[12:-12], eta[12:-12]); ax1.set_title('Time Domain - Original signal')
ax1.set_xlabel('time (sec)'); ax1.set_ylabel('eta(t)')

ax2 = fig.add_subplot(332); ax2.plot(time[12:-12], velocity[11:-11]); ax2.set_title('Velocity - Original signal')
ax2.set_xlabel('time (sec)'); ax2.set_ylabel('v(t**-1)')

ax3 = fig.add_subplot(333); ax3.plot(time[12:-12], acceleration[11:-11]); ax3.set_title('Acceleration - Original signal')
ax3.set_xlabel('time (sec)'); ax3.set_ylabel('a(t**-2)')


ax4 = fig.add_subplot(334); ax4.plot(time[12:-12], filtered_1[11:-11]); ax4.set_title('Time Domain - 1x Filtered signal')
ax4.set_xlabel('time (sec)'); ax4.set_ylabel('eta(t)')

ax5 = fig.add_subplot(335); ax5.plot(time[12:-12], velocity_f1[10:-10]); ax5.set_title('Velocity - 1x Filtered signal')
ax5.set_xlabel('time (sec)'); ax5.set_ylabel('v(t**-1)')

ax6 = fig.add_subplot(336); ax6.plot(time[12:-12], acceleration_f1[10:-10]); ax6.set_title('Acceleration - 1x Filtered signal')
ax6.set_xlabel('time (sec)'); ax6.set_ylabel('a(t**-2)')


ax7 = fig.add_subplot(337); ax7.plot(time[12:-12], filtered_2[2:-2]); ax7.set_title('Time Domain - 10x Filtered signal')
ax7.set_xlabel('time (sec)'); ax7.set_ylabel('eta(t)')

ax8 = fig.add_subplot(338); ax8.plot(time[12:-12], velocity_f2[1:-1]); ax8.set_title('Velocity - 10x Filtered signal')
ax8.set_xlabel('time (sec)'); ax8.set_ylabel('v(t**-1)')

ax9 = fig.add_subplot(339); ax9.plot(time[12:-12], acceleration_f2[1:-1]); ax9.set_title('Acceleration - 10x Filtered signal')
ax9.set_xlabel('time (sec)'); ax9.set_ylabel('a(t**-2)')