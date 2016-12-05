# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 10:05:29 2016
@author: soma0sd
"""
from matplotlib import pyplot as plt
import pickle

nucid = '2380920'

with open('decays02.pkl', 'rb') as f:
  data = pickle.load(f)

lines = []

def decays(nucid):
  global data, lines
  for m in data[nucid]['DM']:
    for i, ems in enumerate(m[0]):
      if i < 1:
        iZ, fZ = int(nucid[4:6]), int(ems[4:6])
        iN, fN = int(nucid[:3])-iZ, int(ems[:3])-fZ
        plt.plot([iZ, fZ], [iN, fN])
        decays(ems)
plt.xlim(78, 94)
plt.title('$^{238}$U Decay Chain')
plt.xlabel('Z')
plt.ylabel('N')
decays(nucid)