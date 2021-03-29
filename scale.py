#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
C major scale with and without sustain. 

@author: khe
"""
import numpy as np
from scipy.io import wavfile
import utils

# Define scale and piano characteristics
scale = ['C4','D4','E4','F4','G4','A4','B4','C5']
note_values = [0.5]*8
factor = [0.68, 0.26, 0.03, 0.  , 0.03]
length = [0.01, 0.6, 0.29, 0.1]
decay = [0.05,0.02,0.005,0.1]
sustain_level = 0.1

# Without sustain (each note in separate bar)
scale_plain = utils.get_song_data(scale, note_values, bar_value=0.5,
                                 factor=factor, length=length, decay=decay, 
                                 sustain_level=sustain_level)
scale_plain = scale_plain * (4096/np.max(scale_plain))
wavfile.write('data/scale_plain.wav', 44100, scale_plain.astype(np.int16))

# With sustain (all note in one bar)
scale_sustain = utils.get_song_data(scale, note_values, bar_value=4,
                                 factor=factor, length=length, decay=decay, 
                                 sustain_level=sustain_level)
scale_sustain = scale_sustain * (4096/np.max(scale_sustain))
wavfile.write('data/scale_sustain.wav', 44100, scale_sustain.astype(np.int16))