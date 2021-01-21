#!/usr/bin/python
'''
Spectrogram from wav file

https://stackoverflow.com/questions/15311853/plot-spectogram-from-mp3
'''
from scikits.audiolab import wavread
from pylab import *

signal, fs, enc = wavread('XC124158.wav')
specgram(signal)
show()
