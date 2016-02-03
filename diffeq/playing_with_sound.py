# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 22:14:46 2015

@author: Georg
"""

import numpy as np
import scitools.sound

###############################################################################
#########################     Some basic functions    #########################
###############################################################################

def note(frequency, length, amplitude=1, sample_rate=44100):
    time_points = np.linspace(0, length, length*sample_rate)
    data = np.sin(2*np.pi*frequency*time_points)
    data = amplitude*data
    return data

def add_echo(data, beta=0.8, delay=0.002, sample_rate=44100):
    newdata = data.copy()
    shift = int(delay*sample_rate)
    newdata[shift:] = beta*data[shift:] + (1-beta)*data[:len(data)-shift]
    return newdata

###############################################################################
##########################      Generate a note      ##########################
###############################################################################

data1 = note(440, 10)
max_amplitude = 2**15 - 1
data1 *= max_amplitude

scitools.sound.write(data1, 'Atone.wav')
#scitools.sound.play('Atone.wav')

###############################################################################
##########################     Generate a melody     ##########################
###############################################################################

base_freq = 400.0
notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
notes2freq = {notes[i]: base_freq*2**(i/12.0) for i in range(len(notes))}

l = 0.2   ## basic durarion unit
tones = [('E', 3*l), ('D', 1*l), ('C#', 2*l), ('B', 2*l), ('A', 2*l), ('B', 2*l),
         ('C#', 2*l), ('D', 2*l), ('E', 3*l), ('F#', 1*l), ('E', 2*l), ('D', 2*l),
         ('C#', 4*l)]
samples = []
for tone, duration in tones:
    s = note(notes2freq[tone], duration)
    samples.append(s)

data2 = np.concatenate(samples)
data2 *= 2**15 - 1
scitools.sound.write(data2, 'melody.wav')
scitools.sound.play('melody.wav')


###############################################################################
##########################     Generate an echo      ##########################
###############################################################################

input_data = scitools.sound.read('melody.wav')
data3 = add_echo(input_data, delay = 1.0)
#data3 *= 2**15 - 1
scitools.sound.write(data3, 'echo.wav')
scitools.sound.play('echo.wav')