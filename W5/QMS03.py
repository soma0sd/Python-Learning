# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 23:22:49 2016
@author: soma0sd

교류, 직류, 진동수를 조정하여 QMS의 필터효과를 시뮬레이션 한다
"""
import tkinter as tk

class QMS:
  def __init__(self, **kw):
    """초기화"""
    # Variables
    self.var = {'ACV': 0, 'DCV': 0 , 'f': 0, 'range': 21, 'E': 10}
    self.result = {}
    self.ion = []
    self.grid_row = 0
    self.var.update(kw)
    # App Load
    self.master = tk.Tk()
    self.master.title('QMS')
    self.frame_canvas()
    self.frame_menu()
    self.ion_generate()
    # App Loop
    self.master.mainloop()

  def frame_menu(self):
    """메뉴프레임"""
    frame = tk.Frame(self.master, bg='#000')
    frame.pack(side='right', fill='both')
    self._menu_object(frame, 'ACV')
    self._menu_object(frame, 'DCV')
    self._menu_object(frame, 'f')

  def frame_canvas(self):
    """캔버스 초기화"""
    self.canvas = tk.Canvas(self.master, width=400, height=300)
    self.canvas.pack(side='left')
    # Create View Line
    self.canvas.create_line(0, 100, 400, 100)
    self.canvas.create_line(0, 200, 400, 200)
    # Create Axis
    _ = self.canvas.create_line(15, 50, 15, 5, width=2, arrow='last')
    self.canvas.tag_raise(_)
    _ = self.canvas.create_line(14, 50, 65, 50, width=2, arrow='last')
    self.canvas.tag_raise(_)
    _ = self.canvas.create_line(15, 150, 15, 105, width=2, arrow='last')
    self.canvas.tag_raise(_)
    _ = self.canvas.create_line(14, 150, 65, 150, width=2, arrow='last')
    self.canvas.tag_raise(_)
    _ = self.canvas.create_text(5, 10, text='x')
    self.canvas.tag_raise(_)
    _ = self.canvas.create_text(60, 60, text='z')
    self.canvas.tag_raise(_)
    _ = self.canvas.create_text(5, 110, text='y')
    self.canvas.tag_raise(_)
    _ = self.canvas.create_text(60, 160, text='z')
    self.canvas.tag_raise(_)
    # Create Result View
    h = 380/self.var['range']
    for m in range(1, self.var['range']):
      self.canvas.create_line(h*m+10, 282, h*m+10, 277)
      self.canvas.create_text(h*m+10, 290, text=m)
      ix = self.canvas.create_rectangle(h*m+5, 209, h*m+15, 279, fill='#000')
      self.result[m]=ix

  def _menu_object(self, master, text):
    var = self.var[text] = tk.StringVar()
    var.set(0)
    _ = tk.Label(master, text=text, fg='#FFF', bg='#000')
    _.grid(row=self.grid_row, column=0, rowspan=2)
    _ = tk.Label(master, textvariable=var, fg='#FFF', bg='#000', width=3)
    _.grid(row=self.grid_row, column=1, rowspan=2)
    _ = tk.Button(master, text='+1', command=lambda *a: self._cmd_var(text,1))
    _.config(fg='#FFF', bg='#000')
    _.grid(row=self.grid_row, column=2, sticky='we')
    _ = tk.Button(master, text='-1', command=lambda *a: self._cmd_var(text,-1))
    _.config(fg='#FFF', bg='#000')
    _.grid(row=self.grid_row, column=3, sticky='we')
    _ = tk.Button(master, text='+10', command=lambda *a: self._cmd_var(text,10))
    _.config(fg='#FFF', bg='#000')
    _.grid(row=self.grid_row+1, column=2, sticky='we')
    _ = tk.Button(master, text='-10', command=lambda *a: self._cmd_var(text,-10))
    _.config(fg='#FFF', bg='#000')
    _.grid(row=self.grid_row+1, column=3, sticky='we')
    self.grid_row += 2

  def _cmd_var(self, key, d):
    """+/- Button Command"""
    i = int(self.var[key].get())
    self.var[key].set(i+d)
    self.ion_generate()

  def ion_generate(self):
    for i in self.ion:
      self.canvas.delete(i['idx'])
      self.canvas.delete(i['idy'])
    for m in range(1, self.var['range']):
      self.ion.append(self.__create_path(m))
    self._result_show()

  def __create_path(self, m):
    import numpy as np
    x, y, z = 0, 0, 0
    vx, vy, vz = 0, 0, np.sqrt(2*self.var['E']/m)
    posx, posy = [0, 50], [0, 150]
    AC = float(self.var['ACV'].get())
    DC = float(self.var['DCV'].get())/10
    f = int(self.var['f'].get())
    while True:
      z += vz
      phase = AC*np.cos(z*np.pi*f/400)
      # View 1
      V1 = DC+phase
      vx = vx+(V1/5**2)/m
      x = x+vx
      posx += [z, x+50]
      # View 2
      V2 = -DC-phase
      vy = vy+(V2/5**2)/m
      y = y+vy
      posy += [z, y+150]
      # return
      if z > 400:
        idx = self.canvas.create_line(posx, fill='#F00')
        idy = self.canvas.create_line(posy, fill='#00F')
        self.canvas.tag_lower(idx)
        self.canvas.tag_lower(idy)
        return {'idx': idx, 'idy': idy, 'z':z, 'm': m, 'mode': 0}
      elif not 10 < posx[-1] < 90:
        idx = self.canvas.create_line(posx, fill='#F00')
        idy = self.canvas.create_line(posy, fill='#00F')
        self.canvas.tag_lower(idx)
        self.canvas.tag_lower(idy)
        return {'idx': idx, 'idy': idy, 'z':z, 'm': m, 'mode': 1}
      elif not 110 < posy[-1] < 190:
        idx = self.canvas.create_line(posx, fill='#F00')
        idy = self.canvas.create_line(posy, fill='#00F')
        self.canvas.tag_lower(idx)
        self.canvas.tag_lower(idy)
        return {'idx': idx, 'idy': idy, 'z':z, 'm': m, 'mode': -1}

  def _result_show(self):
    hy = 70/400
    hx = 380/self.var['range']
    for i in self.ion:
      x = hx*i['m']+10
      y = 279
      ix = self.result[i['m']]
      if i['mode'] == 0:
        self.canvas.coords(ix, x-5, y-70, x+5, y)
        self.canvas.itemconfig(ix, fill='#000')
      elif i['mode'] == 1:  # Escape X-Axis
        by = y-i['z']*hy
        self.canvas.coords(ix, x-5, by, x+5, y)
        self.canvas.itemconfig(ix, fill='#F00')
      elif i['mode'] == -1:  # Escape Y-Axis
        by = y-i['z']*hy
        self.canvas.coords(ix, x-5, by, x+5, y)
        self.canvas.itemconfig(ix, fill='#00F')


QMS()
