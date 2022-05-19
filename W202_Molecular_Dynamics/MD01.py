# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 00:27:32 2016
@author: soma0sd
"""
import tkinter as tk
import numpy as np
import time

"""
계산 클래스
"""
class calc_md:
  def __init__(self, master):
    self.row = 5
    self.column = 5
    self.temp_b = 300
    self.temp_t = -300
    self.dt = 0.0005
    self.size = 400
    self.p = []
    self.hist = [0]*10
    self.K = 1.3806488E-23
    self.amu = 1.660538782E-27
    self.view = tk.Canvas(master, width=self.size, height=self.size)
    self.view.config(bg='#FFF')
    self.result = tk.Canvas(master, width=120, height=self.size)
    self.result.config(bg='#FFF')
    self._particle_setup()

  def _particle_setup(self):
    row = self.row
    column = self.column
    size = self.view.winfo_reqwidth()-4
    coord = lambda ix, iy: (ix-4, iy-4, ix+4, iy+4)
    gap_r = size/(row+1)
    gap_c = size/(column+1)
    for i in range(row):
      y = gap_r*(i+1)
      c = self._temp_color(y)
      self._temp_velocity(y)
      for j in range(column):
        x = gap_c*(j+1)
        idx = self.view.create_oval(coord(x, y), fill=c)
        vx, vy = self._temp_velocity(y)
        self.p.append({'id': idx, 'x': x, 'y': y, 'vx': vx, 'vy': vy})

  def _temp_color(self, y):
    size = self.view.winfo_reqwidth()-4
    ratio = y/size
    if not 0 <= ratio <= 1:
      ratio = 0
    if ratio == 0:
      return '#FF00FF'
    elif ratio < 0.5:
      return '#{:02X}00FF'.format(int(ratio*255))
    elif ratio > 0.5:
      ratio = (ratio-0.5)*2
      return '#FF00{:02X}'.format(255-int(ratio*255))

  def _temp_velocity(self, y, theta=None):
    size = self.view.winfo_reqwidth()-4
    ratio = y/size
    T_top = self.temp_t+273.15
    T_btm = self.temp_b+273.15
    Tmp = (np.abs(T_top-T_btm)*ratio)+min([T_top, T_btm])
    v = np.sqrt(3*self.K*Tmp/self.amu)
    if theta is None:
      theta = np.random.rand()*np.pi*2
    vx, vy = v*np.cos(theta), v*np.sin(theta)
    return vx, vy

  def _force(self, dx, sigma=2):
    ri = sigma/np.sqrt(dx**2)
    return 24*ri**6*((2*ri**6)-1)/dx

  def move(self):
    p = self.p
    view = self.view
    size = self.size
    coord = lambda ix, iy: (ix-4, iy-4, ix+4, iy+4)
    while True:
      for i in range(len(p)):
        x, y = p[i]['x'], p[i]['y']
        vx, vy = p[i]['vx'], p[i]['vy']
        vx, vy = self._temp_velocity(y, np.arctan2(vy, vx))
        vx += self._force(x/20)*self.dt - self._force((size-x)/20)*self.dt
        vy += self._force(y/20)*self.dt - self._force((size-y)/20)*self.dt
        vy += 9.8*self.dt
        for j in range(i+1, len(p)):
          x2, y2 = p[j]['x'], p[j]['y']
          dr = np.sqrt((x-x2)**2+(y-y2)**2)
          vx += self._force(dr/30)*(x-x2)*self.dt
          vy += self._force(dr/30)*(y-y2)*self.dt
          p[j]['vx'] -=  self._force(dr/30)*(x-x2)*self.dt
          p[j]['vy'] -=  self._force(dr/30)*(y-y2)*self.dt
        x += vx*self.dt
        y += vy*self.dt
        view.coords(p[i]['id'], coord(x, y))
        view.itemconfig(p[i]['id'], fill=self._temp_color(y))
        p[i]['x'], p[i]['y'] = x, y
        p[i]['vx'], p[i]['vy'] = vx, vy
      hist = [0]*10
      for i in p:
        for h in range(len(hist)):
          if h*size/11 <= i['y'] < (h+1)*size/11:
            hist[h] += 1
      self.result.delete('all')
      ph = size/10
      for i, h in enumerate(hist):
        px = h*100/max(hist)
        py = i*ph
        self.result.create_rectangle(10, py+5, px+10, py+ph-5, fill='#F00')
      view.update()

  def grid(self):
    self.view.grid(row=0, column=0)
    self.result.grid(row=0, column=1)

"""
메인
"""
root = tk.Tk()
view = calc_md(root)
view.grid()
view.move()
root.mainloop()
