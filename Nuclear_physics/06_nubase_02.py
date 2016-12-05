# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 21:42:38 2016
@author: soma0sd
"""
import pickle
import numpy as np

nu_name = "nubtab12.asc"
pk_name = "decays02.pkl" # 피클링 파일명
ec_mode = ['IS', 'SF']   # 제외할 모드

"""
Constants
"""
t_unit = {'s': 1, 'm': 60, 'h': 360, 'd': 86400, 'y': 31556926}

prefix = {'m': 1E-3, 'u': 1E-6, 'n': 1E-9}
prefix.update({'p': 1E-12, 'a': 1E-18, 'z': 1E-3, 'y': 1E-24})
prefix.update({'k': 1E3, 'M': 1E6, 'G': 1E9, 'T': 1E12, 'P': 1E15})
prefix.update({'E': 1E18, 'Z': 1E21, 'Y': 1E24})

emis = {}
emis['A']  = [(-4, -2, 0)]
emis['B-'] = [(0, 1, 0)]
emis['-'] = emis['B-']
emis['B'] = emis['B-']
emis['2B-'] = [(0, 2, 0)]
emis['B-A'] = [(0, 1, 0), (-4, -2, 0)]
emis['B-n'] = [(0, 1, 0), (-1, 0, 0)]
emis['B-2n'] = [(0, 1, 0), (-1, 0, 0), (-1, 0, 0)]
emis['B-3n'] = [(0, 1, 0), (-1, 0, 0), (-1, 0, 0), (-1, 0, 0)]
emis['B-d'] = [(0, 1, 0), (-2, -1, 0)]
emis['B-t'] = [(0, 1, 0), (-3, -1, 0)]
emis['B+'] = [(0, -1, 0)]
emis['B+A'] = [(0, -1, 0), (-4, -2, 0)]
emis['B+p'] = [(0, -2, 0)]
emis['EC'] = [(0, -1, 0)]
emis['EC+B+'] = [(0, -1, 0), (0, -1, 0)]
emis['e+'] = [(0, -1, 0)]
emis['IT'] = [(0, 0, 1)]
emis['n'] = [(-1, 0, 0)]
emis['2n'] = [(-1, 0, 0), (-1, 0, 0)]
emis['p'] = [(-1, -1, 0)]
emis['P'] = [(-1, -1, 0)]
emis['2p'] = [(-1, -1, 0), (-1, -1, 0)]
emis['d'] = [(-2, -1, 0)]
emis['3H'] = [(-3, -1, 0)]
emis['14C'] = [(-14, -6, 0)]
emis['18O'] = [(-18, -8, 0)]
emis['20O'] = [(-20, -8, 0)]
emis['22Ne'] = [(-22, -10, 0)]
emis['24Ne'] = [(-24, -10, 0)]
emis['28Mg'] = [(-28, -12, 0)]
emis['30Mg'] = [(-30, -12, 0)]
emis['34Si'] = [(-34, -14, 0)]

"""
Functions
"""
# 라인 초기화
def mob_line(s: str):
  s = s.replace('#', ' ')
  return s

# 라인에서 질량수(A), 원자번호(Z), 이성질체(I) 추출
str_A = lambda s: int(s[:3])
str_Z = lambda s: int(s[4:7])
str_I = lambda s: int(s[7])
str_key = lambda A, Z, I: "{:03d}{:03d}{}".format(A, Z, I)

# 라인에서 붕괴상수 추출
def get_lambda(s: str):
  global prefix, t_unit
  _s = s[60:69].strip()
  _stbl = ['stbl', 'p-unst', 'R', 'contamnt']
  if _s == '' or [1 for i in _stbl if i in _s]:
    return 0.0
  eqs = list(set(['>', '<', '~']) & set(_s))
  if eqs:
    _s = _s.replace(eqs[0], ' ')
  hl = float(_s)
  _unit = s[69:71].strip()
  if len(_unit) == 2:
    unit = prefix[_unit[0]]*t_unit[_unit[1]]
  else:
    unit = t_unit[_unit[0]]
  return np.log(2)/(hl*unit)

# 모드로부터 방출핵종 출력
def get_emission(mode, A, Z, I):
  global emis
  mode = mode.strip()
  em = [emis[i] for i in emis.keys() if i == mode][0]
  da, dz, di = 0, 0, 0
  em_p = []
  for a, z, i in em:
    da, dz, di = da-a, dz-z, di-i
    if a <= -1:
      em_p.append("{:03d}{:03d}{}".format(-a, -z, 0))
  if di > 0:
    I = 0
  em_d = "{:03d}{:03d}{}".format(A-da, Z-dz, I)
  return [em_d]+em_p

# 라인에서 붕괴모드 추출
def get_mode(s: str, A, Z, I):
  global ec_mode
  data = []
  _mode = s[110:].replace('\n', '').split(';')
  for m in _mode:
    if '?' in m or m.strip() == '':
      continue
    eqs = list(set(['=','<','>', '~']) & set(m))
    if not eqs:
      continue
    _ = m.split(eqs[0])
    val = float(_[1].split(' ')[0].split('[')[0])/100
    mode = _[0]
    if [i for i in ec_mode if mode == i]:
      continue
    mode = mode.replace('SF', '')
    ems = get_emission(mode, A, Z, I)
    data.append([ems, val])
  return data


"""
Main
"""
data = {}
with open(nu_name, 'r') as f:
  for s in f.readlines():
    s = mob_line(s)
    A, Z, I = str_A(s), str_Z(s), str_I(s)
    lamb = get_lambda(s)
    mode = get_mode(s, A, Z, I)
    if A == 1 and Z == 0: mode = []
    key = str_key(A, Z, I)
    data[key] = {'DC': lamb, 'DM': mode}
  del s, A, Z, I, lamb, mode, key

with open(pk_name, 'wb') as f:
  pickle.dump(data, f)

del ec_mode, nu_name, pk_name, prefix, t_unit, emis
