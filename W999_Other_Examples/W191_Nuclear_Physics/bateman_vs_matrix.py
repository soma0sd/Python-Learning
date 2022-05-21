# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 00:31:53 2016
@author: soma0sd
"""
import numpy as np
import matplotlib.pyplot as plt

"""
constants
"""
m = 60
h = 3600
d = 86400
y = 31556925.9747 #sec
ln2 = np.log(2)

"""
variables
"""
N_0 = 1
name = ['Sr90', 'Y90']
lamb = [ln2/(29.1*y), ln2/(2.67*d)]
bran = [1, 1]
"""
name = ['U235', 'Th231', 'Pa231', 'Ac226', 'Th226', 'Ra226']
lamb = [ln2/(7.038E8*y), ln2/(1.063*d), ln2/(32500*y), ln2/(1.224*d), ln2/(30.9*m), ln2/(1599*y)]
bran = [1, 1, 1, 0.17, 0.83]
matr = np.array([[lamb[0], 0, 0, 0, 0, 0],
                 [bran[0]*lamb[0], lamb[1], 0, 0, 0, 0],
                 [0, bran[1]*lamb[1], lamb[2], 0, 0, 0],
                 [0, 0, bran[2]*lamb[2], lamb[3], 0, 0],
                 [0, 0, 0, bran[3]*lamb[3], lamb[4], 0],
                 [0, 0, 0, bran[4]*lamb[3], 0, lamb[5]]])
"""

"""
functions
"""
def bateman(t, N):
  global N_0, lamb, bran
  var1 = 1
  value = 0
  for i in range(N-1):
    var1 *= lamb[i]*bran[i]
  for i in range(N):
    var2 = 1
    for j in range(N):
      if i is j: continue
      else: var2 *= lamb[j]-lamb[i]
    value += N_0*var1*np.exp(-lamb[i]*t)/var2
  return value

"""
main
"""
t = np.logspace(0, 11, 200)
#t = np.linspace(1, 0.5*h)
plt.ylim(1E-30, 5)
#plt.xlim(1, 1E13)
for i in range(len(name)):
  val = lamb[i]*bateman(t, i+1)
  plt.plot(t, val, label=name[i])
plt.loglog()
plt.legend(loc=3)
plt.xlabel(r'Time [$sec$]')
plt.ylabel(r'Property')
del m, h, d, y, bran, name, i, lamb, ln2
