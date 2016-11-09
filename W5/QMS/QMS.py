# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 18:00:52 2016
@author: soma0sd
"""
import tkinter as tk

class QMS:
  def __init__(self):
    self.E = 3   # ion energy [ev] : 1.60217646E-19 J
    self.AC = 0  # AC voltage [V]
    self.DC = 0  # DC voltage [V]
    self.f = 0   # frequency for AC [Hz]
    self.rod_lenth = 0.1   # rod lenth [m]
    self.rod_radius = 0.01 # rod radius [m]
    self.width = 300       # canvas width
    self.height = 100      # canvas height
    root = tk.Tk()
    root.title('QMS simulation')
    root.mainloop()


QMS()
