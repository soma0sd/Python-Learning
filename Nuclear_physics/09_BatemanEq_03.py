# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 08:25:22 2016
@author: soma0sd
"""
import pickle
import numpy as np
from matplotlib import pyplot as plt

nucid = '2350920'
N0 = 1E30

symbols = {0: 'n', 1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N', 8: 'O', 9: 'F', 10: 'Ne', 11: 'Na', 12: 'Mg', 13: 'Al', 14: 'Si', 15: 'P', 16: 'S', 17: 'Cl', 18: 'Ar', 19: 'K', 20: 'Ca', 21: 'Sc', 22: 'Ti', 23: 'V', 24: 'Cr', 25: 'Mn', 26: 'Fe', 27: 'Co', 28: 'Ni', 29: 'Cu', 30: 'Zn', 31: 'Ga', 32: 'Ge', 33: 'As', 34: 'Se', 35: 'Br', 36: 'Kr', 37: 'Rb', 38: 'Sr', 39: 'Y', 40: 'Zr', 41: 'Nb', 42: 'Mo', 43: 'Tc', 44: 'Ru', 45: 'Rh', 46: 'Pd', 47: 'Ag', 48: 'Cd', 49: 'In', 50: 'Sn', 51: 'Sb', 52: 'Te', 53: 'I', 54: 'Xe', 55: 'Cs', 56: 'Ba', 57: 'La', 58: 'Ce', 59: 'Pr', 60: 'Nd', 61: 'Pm', 62: 'Sm', 63: 'Eu', 64: 'Gd', 65: 'Tb', 66: 'Dy', 67: 'Ho', 68: 'Er', 69: 'Tm', 70: 'Yb', 71: 'Lu', 72: 'Hf', 73: 'Ta', 74: 'W', 75: 'Re', 76: 'Os', 77: 'Ir', 78: 'Pt', 79: 'Au', 80: 'Hg', 81: 'Tl', 82: 'Pb', 83: 'Bi', 84: 'Po', 85: 'At', 86: 'Rn', 87: 'Fr', 88: 'Ra', 89: 'Ac', 90: 'Th', 91: 'Pa', 92: 'U', 93: 'Np', 94: 'Pu', 95: 'Am', 96: 'Cm', 97: 'Bk', 98: 'Cf', 99: 'Es', 100: 'Fm', 101: 'Md', 102: 'No', 103: 'Lr', 104: 'Rf', 105: 'Db', 106: 'Sg', 107: 'Bh', 108: 'Hs', 109: 'Mt', 110: 'Ds', 111: 'Rg', 112: 'Cn', 113: 'Uut', 114: 'Fl', 115: 'Uup', 116: 'Lv', 118: 'Uuo'}


with open('decays02.pkl', 'rb') as f:
  data = pickle.load(f)

def calc_bateman(t, br, lamb):
  global N0
  M1, M2, value = 1, 1, 0
  for l in lamb[:-1]:
    M1 *= l
  for b in br:
    M1 *= b
  for l1 in lamb:
    M2 = 1
    for l2 in lamb:
      if l1 != l2:
        M2 *= l2-l1
    value += M1*np.exp(-l1*t)*N0/M2
  return value

def calc_chain(t, key, br=[1], lamb=[]):
  global chain, data
  if not key in chain.keys():
    chain[key] = t*0
  lamb += [data[key]['DC']]
  chain[key] += calc_bateman(t, br, lamb)
  for i in data[key]['DM']:
    br += [i[1]]
    for j in i[0]:
      calc_chain(t, j, br, lamb)

chain = {}
t = np.logspace(0, 20, 100)
calc_chain(t, nucid)
for key in chain.keys():
  sym = symbols[int(key[4:6])]
  A = int(key[:3])
  tx = '$^{'+str(A)+'}\mathrm{'+sym+'}$'
  plt.plot(t, chain[key], label=tx)
plt.loglog()
plt.ylim(1, N0*5)
sym = symbols[int(nucid[4:6])]
A = int(nucid[:3])
tx = '$^{'+str(A)+'}\mathrm{'+sym+'}$'
plt.title(tx+' Decay', fontsize=15)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, ncol=3, borderaxespad=0.)
plt.xlabel('Time [$\mathrm{sec}$]', fontsize=10)
plt.ylabel('# of Isotopes', fontsize=10)
del t, data, N0, key, nucid, sym

