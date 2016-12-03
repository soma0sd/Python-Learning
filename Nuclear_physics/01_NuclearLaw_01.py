# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 19:25:18 2016
@author: soma0sd
"""
import numpy as np
from matplotlib import pyplot as plt

def N(t):
  global N0, lamb
  return np.exp(-lamb*t)*N0

lamb = 1.0  # 붕괴 상수
N0 = 1.0    # 초기 핵종량
t = np.linspace(0, 10)
plt.plot(t, N(t))
