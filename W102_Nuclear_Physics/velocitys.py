# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:52:48 2016

@author: soma0sd
"""
import numpy as np
import matplotlib.pyplot as plt

sigma = 0.1
mu = 1.0
bins = (sigma*np.random.randn(1E5)+mu)
plt.hist(bins, 30)
plt.xlabel('Mean Velocity$^{-1}$', size=15)
plt.ylabel('Count', size=15)
