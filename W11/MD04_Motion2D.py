# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 17:24:32 2016
@author: soma0sd
"""
import numpy as np
import tkinter as tk
import time

def force(dx, epsilon=1.0, sigma=1.0):
  ri = sigma/np.sqrt((dx/40)**2)
  if dx < 0:
    return 24*ri**6*(2*ri**6-1)/dx
  else:
    return -24*ri**6*(2*ri**6-1)/dx

class md:
  def __init__(self, master, v_max):
    self.cav = tk.Canvas(master, width=400, height=200, bg='#FFF')
    self.cav.pack()
    self.p = []
    for ix in range(1, 20):
      for iy in range(1, 10):
        x, y = ix*20, iy*20
        idx = self.cav.create_oval(x-5, y-5, x+5, y+5, fill='#F00')
        v = np.random.randint(0, v_max)
        t = np.random.rand()*2*np.pi
        _ = {'id': idx, 'x': x, 'y': y}
        _.update({'vx': v*np.cos(t), 'vy': v*np.sin(t)})
        _.update({'ax': 0, 'ay': 0})
        self.p.append(_)
    self.move()

  def move(self):
    t0 = time.time()
    while True:
      dt = time.time()-t0
      for i1, p1 in enumerate(self.p):
        for i2, p2 in enumerate(self.p[i1:]):
          dx, dy = p1['x']-p2['x'], p1['y']-p2['y']
          dr = np.sqrt(dx**2+dy**2)
          if dr < 1:
            continue
          F = force(dr)
          self.p[i1]['ax'] += F*dx
          self.p[i1]['ay'] += F*dy
          self.p[i2]['ax'] -= F*dx
          self.p[i2]['ay'] -= F*dy
          self.p[i1]['x'] += p1['vx']*dt+0.5*p1['ax']*dt**2
          self.p[i1]['y'] += p1['vy']*dt+0.5*p1['ay']*dt**2
          _ = [p1['x']-5, p1['y']-5, p1['x']+5, p1['y']+5]
          self.cav.coords(p1['id'], _)
      t0 += dt
      self.cav.update()

root = tk.Tk()
root.title('MD 2D test')
view = md(root, 30)
root.mainloop()
