# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 18:58:46 2016
@author: soma0sd

두 입자 사이에 작용하는 퍼텐셜과 힘을 plot한다
"""
import numpy as np
import matplotlib.pyplot as plt


def potential(x, epsilon, sigma):
  ri = sigma/x
  return 4*epsilon*(ri**12-ri**6)


def force(x, epsilon, sigma):
  u = potential(x, epsilon, sigma)
  return -np.gradient(u)


x = np.linspace(0, 3, 100)
plt.plot(x, potential(x, 1, 1), 'b')  # 파란 선: 퍼텐셜
plt.plot(x, force(x, 1, 1), 'g')      # 녹색 선: 힘
plt.plot(x, np.zeros(100), 'r:')
plt.ylim(-1, 1)
plt.xlabel(r'distance [$\sigma^{-1}$]')
plt.ylabel(r'potential [$\epsilon^{-1}$]')