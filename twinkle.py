#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write `Twinkle Twinkle Little Star` from sine waves. 

@author: khe
"""
import numpy as np
from scipy.io import wavfile
import utils

right_hand_notes = ['C4', 'C4', 'G4', 'G4',
                   'A4', 'A4', 'G4',
                   'F4', 'F4', 'E4', 'E4',
                   'D4', 'D4', 'C4',
                   'G4', 'G4', 'F4', 'F4',
                   'E4', 'E4', 'D4',
                   'G4', 'G4', 'F4', 'F4',
                   'E4', 'E4', 'D4',
                   'C4', 'C4', 'G4', 'G4',
                   'A4', 'A4', 'G4',
                   'F4', 'F4', 'E4', 'E4',
                   'D4', 'D4', 'C4',]
right_hand_duration = [0.5, 0.5, 0.5, 0.5,
                       0.5, 0.5, 1]*6

left_hand_notes = ['C3',
                  'A3',
                  'F3',
                  'D3', 'C3',
                  'G3', 'F3',
                  'E3', 'D3',
                  'G3', 'F3',
                  'E3', 'D3',
                  'C3', 'E3', 'G3', 'C4',
                  'A3', 'A3', 'G3',
                  'F3', 'B2', 'E3', 'C3',
                  'D3', 'D3', 'C3']
left_hand_duration = [2,
                      2,
                      2,
                      1, 1,
                      1, 1,
                      1, 1,
                      1, 1,
                      1, 1,
                      0.5, 0.5, 0.5, 0.5,
                      0.5, 0.5, 1,
                      0.5, 0.5, 0.5, 0.5,
                      0.5, 0.5, 1]

factor = [0.68, 0.26, 0.03, 0.  , 0.03]
length = [0.01, 0.6, 0.29, 0.1]
decay = [0.05,0.02,0.005,0.1]
sustain_level = 0.1
right_hand = utils.get_song_data(right_hand_notes, right_hand_duration, 2,
                                 factor, length, decay, sustain_level)
factor = [0.73, 0.16, 0.06, 0.01, 0.02, 0.01  , 0.01]
length = [0.01, 0.29, 0.6, 0.1]
decay = [0.05,0.02,0.005,0.1]
left_hand = utils.get_song_data(left_hand_notes, left_hand_duration, 2,
                                 factor, length, decay, sustain_level)
data = left_hand+right_hand
data = data * (4096/np.max(data))
wavfile.write('data/twinkle_star.wav', 44100, data.astype(np.int16))