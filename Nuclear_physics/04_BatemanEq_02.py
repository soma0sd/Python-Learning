# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 22:11:54 2016

@author: soma0sd
"""
import numpy as np
import matplotlib.pyplot as plt

def bateman(t, k):
  global N0, lamb
  Nt = 0
  M1 = 1
  for l in lamb[:k-1]: M1 *= l
  for i in lamb[:k]:
    M2 = 1
    for j in lamb[:k]:
      if i != j: M2 /= j-i
    Nt += M1*M2*N0*np.exp(-i*t)
  return Nt

N0 = 1.0
lamb = [0.8, 0.7, 0.9, 0.3]
t = np.linspace(0, 20)

for i in range(len(lamb)): plt.plot(t, bateman(t, i+1))
plt.ylim(0, N0)
