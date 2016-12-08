# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 00:27:32 2016
@author: soma0sd
"""
import tkinter as tk
import numpy as np
import time

row = 4
col = 4
T_bot = 20
T_top = 80
m = 108*1.66053904E-27

K = 1.3806504E-23
Tmp = lambda x: x+273.15

root = tk.Tk()
root.title('Molecular Dynamics')
view = tk.Canvas(root, width=400, height=400, bg="#FFF")
view.grid(row=0, column=0)
_p = []

def temperate(y):
  global view, T_bot, T_top
  _h = view.winfo_reqheight()-4
  return ((y/_h) * ((T_top-T_bot)))+T_bot

def temp_color(temp):
  global T_bot, T_top
  ratio = (temp-T_bot) / ((T_top-T_bot))
  if ratio == 0.5:
    return '#000000'
  elif ratio < 0.5:
    return '#0000{:02X}'.format(256-(int(ratio*256)))
  elif ratio > 0.5:
    return '#{:02X}0000'.format(int(ratio*256))

_w, _h = view.winfo_reqwidth()-4, view.winfo_reqheight()-4
_r = 5
for _i in range(row):
  _ih = _h*(_i+1)/(row+1)
  for _j in range(col):
    _iw = _h*(_j+1)/(col+1)
    _Tm = temperate(_ih)
    _co = temp_color(_Tm)
    _v = np.sqrt(3*K*Tmp(_Tm)/m)
    _T = np.random.rand()*2*np.pi
    _id = view.create_oval(_iw-_r, _ih-_r, _iw+_r, _ih+_r, fill=_co)
    _dic = {'id': _id, 'Tm': _Tm}
    _dic.update({'x': _iw, 'y': _ih})
    _dic.update({'vx': _v*np.cos(_T), 'vy': _v*np.sin(_T)})
    _p.append(_dic)

def force(dx, epsilon=1.0, sigma=1.0):
  global view
  w = (view.winfo_reqwidth()-4)*0.1
  ri = sigma/np.sqrt((dx/w)**2)
  if dx < 0:
    return 24*ri**6*(2*ri**6-1)/dx
  else:
    return -24*ri**6*(2*ri**6-1)/dx

def temp_v(iT, fT, vx, vy):
  global K, m, Tmp
  theta = np.arctan2(vy, vx)
  dT = Tmp(fT)-Tmp(iT)
  if dT < 1E-6:
    return vx, vy
  newv = np.sqrt(3*K*dT/m)
  dvx, dvy = newv*np.cos(theta), newv*np.sin(theta)
  return vx+dvx, vy+dvy

def move_tick(dt):
  global _p, view, m
  w, h = view.winfo_reqwidth()-4, view.winfo_reqheight()-4
  for i in range(len(_p)):
    x, y = _p[i]['x'], _p[i]['y']
    vx, vy = _p[i]['vx'], _p[i]['vy']
    Fx, Fy = force(x)-force(w-x), force(y)-force(h-y)
    vx = vx-Fx*dt
    vy = vy-Fy*dt
    for j in range(i+1, len(_p)):
      if i != j:
        dx = _p[j]['x']-_p[i]['x']
        dy = _p[j]['y']-_p[i]['y']
        Fx, Fy = force(dx), force(dy)
        vx += Fx*dt
        vy += Fy*dt
        _p[j]['vx'] -= Fx*dt
        _p[j]['vy'] -= Fy*dt
    x = _p[i]['x'] = x+vx*dt
    y = _p[i]['y'] = y+vy*dt
    view.coords(_p[i]['id'], x-_r, y-_r, x+_r, y+_r)
    iT = _p[i]['Tm']
    fT = temperate(y)
    _p[i]['vx'], _p[i]['vy'] = temp_v(iT, fT, vx, vy)
    _p[i]['Tm'] = fT
    co = temp_color(iT)
    view.itemconfig(_p[i]['id'], fill=co)

while True:
  time.sleep(0.05)
  move_tick(0.002)
  view.update()

del T_bot, T_top, col, row, m, K
root.mainloop()
