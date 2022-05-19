# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 13:47:13 2016

@author: soma0sd
"""
import matplotlib.pyplot as plt
import numpy as np

def polarization(x):
  return np.cos(x*np.pi)**2

def zeros(x):
  return x*0+0.5

x = np.linspace(0, 2, 100)
plt.plot(x, polarization(x))
plt.plot(x, zeros(x), ":r")
plt.xlabel('$\Theta$ [$\pi^{-1}$]')
