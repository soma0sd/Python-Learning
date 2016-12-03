# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 23:57:40 2016
@author: soma0sd
"""
data = []
with open('nubtab12.asc') as f:
  raw = f.readlines()
  for l in raw:
    l = l.strip('\n')
    _ = [int(l[0:3])]
    _ += [int(l[4:7])]
    _ += [int(l[7])]
    _ += [l[11:17].strip()]
    _ += [l[19:38].strip()]
    _ += [l[38:56].strip()]
    _ += [l[56:60].strip()]
    _ += [l[60:69].strip()]
    _ += [l[69:71].strip()]
    _ += [l[110:].strip()]
    data.append(_)
  del raw, l
