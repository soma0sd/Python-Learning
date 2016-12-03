# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 18:50:26 2016
@author: soma0sd
"""
import numpy as np
from matplotlib import pyplot as plt

def N(t):
  global N0, lamb
  return np.exp(-lamb*t)*N0

lamb = 1.0
N0 = 1.0
t = np.linspace(0, 10)
plt.plot(t, N(t))
