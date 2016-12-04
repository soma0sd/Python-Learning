# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 23:57:40 2016
@author: soma0sd
"""
import numpy as np
import pickle as pkl

def stream2lamb(t: str, u: str):
  prefix = {' ': 1, 'm': 1E-3, 'u': 1E-6, 'n': 1E-9,
            'p': 1E-12, 'a': 1E-18, 'z': 1E-3, 'y': 1E-24,
            'k': 1E3, 'M': 1E6, 'G': 1E9, 'T': 1E12, 'P': 1E15,
            'E': 1E18, 'Z': 1E21, 'Y': 1E24}  # 접두사
  unit = {'s': 1, 'm': 60, 'h': 360, 'd': 86400, 'y': 31556926}  # 단위
  pn = set(['>', '<', '~'])  # 상한, 하한 문자 제거
  stb = ['stbl', 'p-unst', '', 'contamnt']  # 안정핵종 및 정보없음 판별
  t = t.replace('#', '').strip()
  u = u.strip()
  if t in stb:
    return -1.0
  elif 'R' in t:
    return -1.0
  elif set(t) & pn:
    _ = list(set(t) & pn)[0]
    hl = float(t.replace(_, ''))
  else:
    hl = float(t)
  if len(u) == 2:
    hl *= prefix[u[0]]*unit[u[1]]
  else:
    hl *= unit[u[0]]
  return np.log(2)/hl

def stream2mode(s: str):
  mode = []
  eq = set(['=', '~', '<', '>'])
  for m in s.strip(' \n').split(';'):
    if not '?' in m and m != '' and m != '...':
      _m = m.replace('#', '').split(' ')[0]
      _m = _m.split('[')[0]
      _e = list(set(_m) & eq)
      if len(_m) > 2:
        _ = _m.split(_e[0])
        mode.append([_[0], float(_[1])])
  return mode

data = {}
with open('nubtab12.asc') as f:
  stream = f.readlines()
  for s in stream:
    A = int(s[0:3])  # 질량수
    Z = int(s[4:7])  # 원자번호
    I = int(s[7])    # 이성질체
    lamb = stream2lamb(s[60:69], s[69:71])  # 붕괴상수
    mode = stream2mode(s[110:])             # 붕괴 모드
    key = "{:03d}{:03d}{}".format(A, Z, I)
    data[key] = {'decay const': lamb, 'mode': mode}
  del stream, s, A, Z, I, lamb, mode, key

with open('decays01.pkl', 'wb') as f:
  pkl.dump(data, f)
del data

with open('decays01.pkl', 'rb') as f:
  n_data = pkl.load(f)