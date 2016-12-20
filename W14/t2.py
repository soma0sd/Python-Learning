# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 15:38:04 2016

@author: soma0sd
"""
import numpy as np
import tkinter as tk
import time

"""const"""
elt = 0.8
g = 10
r = 7

def start():
  global canvas, triger, obj
  triger = True
  obj = canvas.create_oval(-r, -r, r, r, fill='#000')
  x, y = 0, 0
  vx, vy = np.random.random()*20+10, 0
  t0 = time.time()
  while triger:
    dt = time.time()-t0
    vy += g*dt*3
    x += vx*dt*3
    y += vy*dt*3
    canvas.coords(obj, x-r, y-r, x+r, y+r)
    canvas.update()
    if y >= 295 and vy > 0:
      vy = -vy*elt
    t0 += dt


def reset():
  global canvas, triger, obj
  triger = False
  if len(obj) > 0:
    canvas.delete('all')


triger = False
obj = None
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300, bg='#FFF')
btn_s = tk.Button(root, text='START', command=start)
btn_r = tk.Button(root, text='RESET', command=reset)

canvas.pack()
btn_s.pack()
btn_r.pack()
root.mainloop()
