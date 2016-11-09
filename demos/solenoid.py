# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:56:32 2016
@author: soma0sd
"""
import tkinter as tk


class solenoid:
  def __init__(self):
    self.master = tk.Tk()
    self.canvas = tk.Canvas(self.master, width=400, height=300)
    self.canvas.pack()
    self.coiling(10)
    self.master.mainloop()

  def coiling(self, N):
    hx = 200/N
    for i in range(N):
      x = hx*i+100
      self.canvas.create_oval(x-5, 95, x+5, 105, fill='#000')
      self.canvas.create_oval(x-5, 195, x+5, 205, fill='#000')

solenoid()

