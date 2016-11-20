# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 20:35:02 2016
@author: soma0sd
"""
import numpy as np
import tkinter as tk
import time

def potential(x, epsilon=1, sigma=1.0):
  ri = sigma/np.sqrt(x**2)
  return 4*epsilon*(ri**12-ri**6)

def force(dx, epsilon=1.0, sigma=1.0):
  ri = sigma/np.sqrt((dx/40)**2)
  if dx < 0:
    return 24*ri**6*(2*ri**6-1)
  else:
    return -24*ri**6*(2*ri**6-1)

class mcs:
  def __init__(self, v):
    self.v0 = v
    self.p = None
    root = tk.Tk()
    root.title('1D Motion')
    self.canv = tk.Canvas(root, width=400, height=200, bg='#FFF')
    self.canv.grid(row=0, column=0)
    self.setup()
    self.move()
    root.mainloop()

  def setup(self):
    w, h = self.canv.winfo_reqwidth()-4, self.canv.winfo_reqheight()-4
    self.p = self.canv.create_oval(w-10, h/2-10, w+10, h/2+10)
    self.canv.itemconfig(self.p, fill='#F00')
    self.canv.create_oval(w/2-10, h/2-10, w/2+10, h/2+10, fill='#000')
    self.canv.create_line(0, h/2, w, h/2, dash=(3, 5), fill='#F00')

  def move(self):
    t0 = time.time()
    w = self.canv.winfo_reqwidth()-4
    pos = self.canv.coords(self.p)
    x, y, v, a = pos[0]+10, pos[1]+10, self.v0, 0
    while True:
      time.sleep(0.05)
      dt = time.time()-t0
      a += force((w/2)-x)
      x += v*dt+0.5*a*dt
      self.canv.coords(self.p, x-10, y-10, x+10, y+10)
      if x <= 0:
        x = w
      elif x >= w:
        x = 0
      self.canv.update()
      t0 += dt

mcs(60)
