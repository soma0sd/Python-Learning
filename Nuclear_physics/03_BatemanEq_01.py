# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 19:25:00 2016
@author: soma0sd
"""
import numpy as np
import matplotlib.pyplot as plt

N0 = 1.0
lamb = [0.8, 0.7, 0.9, 0.3]
t = np.linspace(0, 20)

M1 = 1
for l in lamb: M1 *= l

Nt = 0
for i in lamb:
  M2 = 1
  for j in lamb:
    if i != j: M2 /= j-i
  Nt += M1*M2*N0*np.exp(-i*t)

plt.plot(t, Nt)
