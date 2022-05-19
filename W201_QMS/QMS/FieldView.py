# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 18:01:17 2016
@author: soma0sd
"""
import tkinter as tk
import numpy as np

class FieldView:
  def __init__(self, master, **kw):
    self.size = 200    # Size of View [px]
    self.rodW = 0.05   # Size of QMS side [m]
    self.ACV = 1       # AC Voltage of Rods [V]
    self.DCV = 2       # DC Voltage of Rods [V]
    self.f = 0         # Frequency for AC
    self.time = 0      # Time
    self.resol = 5     # resolution of color map [px]
    self.fmap = []     # color map {id, x, y}
    self.view = tk.Canvas(master)

  def set(self, **kw):
    self.options.update(kw)

  def get(self, name: str):
    return self.options[name]

  def pack(self, **kw):
    self._fLayout()
    self.view.pack(**kw)

  def grid(self, **kw):
    self._fLayout()
    self.view.grid(**kw)

  def set_time(self, time):
    self.time = time
    self._fMapping()
    self.view.update()

  def _fLayout(self):
    self.view.config(width=self.size, height=self.size)
    # colormap append
    res = self.resol
    for ix in range(int(self.size/res)):
      x = ix*res
      _x = x+res/2
      for iy in range(int(self.size/res)):
        y = iy*res
        _y = y+res/2
        _id = self.view.create_rectangle(x, y, x+res, y+res, width=0)
        self.fmap.append({'id': _id, 'x': _x, 'y': _y})
    self._fMapping()

  def _fMapping(self):
    cols = {-i: "#0000{:02X}".format(i) for i in range(256)}
    cols.update({i: "#{:02X}0000".format(i) for i in range(1, 256)})
    mv = self.DCV+self.ACV
    v = self.DCV+self.ACV*np.cos(2*np.pi*self.f*self.time)
    mp = self.size/2
    mpx = self._fTransMetre(0.8*self.size/2)
    fcol = lambda E: int(E*255/mv)
    for m in self.fmap:
      x = self._fTransMetre(m['x']-mp)
      y = self._fTransMetre(m['y']-mp)
      E = v*(x**2-y**2)/(2*mpx**2)
      self.view.itemconfig(m['id'], fill=cols[fcol(E)])

  def _fTransMetre(self, value):
    # px to metre
    return value*self.size/self.rodW

  def _fTransPx(self, value):
    # metre to px
    return value*self.rodW/self.size

if __name__ == '__main__':
  import time
  root = tk.Tk()
  root.title('QMS rods Field test')
  f = FieldView(root)
  f.size = 400
  f.pack()
  t0 = time.time()
  while True:
    f.set_time(time.time()-t0)
  root.mainloop()
