# -*- coding: utf-8 -*-
"""MAGPOW.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NgEG0WJXGxXT0jSLRZnra9RTGa_CIdGk
"""

def MAGPOW(Windowed_Frames,num_FFT=512):
  # Find the magnitude of the one sided FFT
  # Real valued signal so symmetry can be used to find other side
  # Power is 1/number of samples *the square of the signal 
  MAG = np.abs(np.fft.rfft(Windowed_Frames, num_FFT))  # Magnitude of the FFT
  POW = ((1.0 / num_FFT) * ((MAG) ** 2))  # Power Spectrum
  return(MAG,POW)