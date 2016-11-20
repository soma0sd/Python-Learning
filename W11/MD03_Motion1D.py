# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 12:15:32 2016
@author: soma0sd
"""
import tkinter as tk
import numpy as np
import time

def force(dx, epsilon=1.0, sigma=1.0):
  ri = sigma/np.sqrt((dx/50)**2)
  if dx < 0:
    return 24*ri**6*(2*ri**6-1)
  else:
    return -24*ri**6*(2*ri**6-1)


class md:
  def __init__(self, master, v):
    self.v = v
    self.cav = tk.Canvas(master, width=400, height=200, bg='#FFF')
    self.cav.pack()
    self.cav.create_line(0, 100, 400, 100, dash=(3, 3), fill='#F00')
    self.p1 = self.cav.create_oval(390, 90, 410, 110, fill='#00F')
    self.p2 = self.cav.create_oval(190, 90, 210, 110, fill='#00F')
    self.move()


  def move(self):
    t0 = time.time()
    pos1 = self.cav.coords(self.p1)
    pos2 = self.cav.coords(self.p2)
    y = 100
    x1, v1, v1, a1 = pos1[0]+10, pos1[1]+10, self.v, 0
    x2, v2, v2, a2 = pos2[0]+10, pos2[1]+10, 0, 0
    while True:
      time.sleep(0.05)
      dt = time.time()-t0
      a1 += force(x1-x2)
      a2 -= force(x1-x2)
      x1 -= v1*dt+0.5*a1*dt
      x2 -= v2*dt+0.5*a2*dt
      self.cav.coords(self.p1, x1-10, y-10, x1+10, y+10)
      self.cav.coords(self.p2, x2-10, y-10, x2+10, y+10)
      self.cav.update()
      if x1 <= 0:
        x1 = 400
      elif x1 >= 400:
        x1 = 0
      if x2 <= 0:
        x2 = 400
      elif x2 >= 400:
        x2 = 0
      t0 += dt


root = tk.Tk()
root.title('1D Motion 2')
view = md(root, 70)
root.mainloop()



