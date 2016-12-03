# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 18:50:26 2016
@author: soma0sd
"""
import numpy as np
from matplotlib import pyplot as plt

def N(t, N0: int):
  global lamb
  return np.exp(-lamb*t)*N0

def MC(t, N0: int):
  global lamb
  N = N0
  data = []
  for ti in t:
    for n in range(int(N0)):
      if np.random.rand() < lamb:
        N -= 1
    N0 = N
    data.append(N)
  return data

lamb = 0.1
t = np.arange(0, 40, 1)

p = plt.subplot(221)
p.set_title('$N_0 = 1$')
p.plot(t, N(t, 1), 'r')
p.bar(t, MC(t, 1))

p = plt.subplot(222)
p.set_title('$N_0 = 10$')
p.plot(t, N(t, 10), 'r')
p.bar(t, MC(t, 10))

p = plt.subplot(223)
p.set_xlabel('$N_0 = 100$')
p.plot(t, N(t, 1E2), 'r')
p.bar(t, MC(t, 1E2))

p = plt.subplot(224)
p.set_xlabel('$N_0 = 1000$')
p.plot(t, N(t, 1E3), 'r')
p.bar(t, MC(t, 1E3))
