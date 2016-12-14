# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 12:32:54 2016
@author: soma0sd
"""
from matplotlib import pyplot as plt
from numpy import random
import numpy as np

def mc(count, ax):
  plt.plot(np.linspace(0, 1), np.sin(np.linspace(0, 1)))
  x = random.rand(count)
  y = random.rand(count)
  c = sum([1 for i in range(len(x)) if y[i] < np.sin(x[i])])
  print(c/count)
  plt.plot(x, y, '.')
  plt.show()

mc(100)
mc(1000)
mc(10000)