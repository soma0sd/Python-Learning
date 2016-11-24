# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 05:51:15 2016
@author: soma0sd
"""
import tkinter as tk
import numpy as np
import time


def force(dx, epsilon=1.0, sigma=1.0):
  ri = sigma/np.sqrt((dx/40)**2)
  if dx < 0:
    return 24*ri**6*(2*ri**6-1)/dx
  else:
    return -24*ri**6*(2*ri**6-1)/dx



class md:
  def __init__(self, master, **kw):
    ini = {'size': 400, 'px': 3, 'py': 3, 'vmax': 100}
    ini.update(kw)


    point = [[0,(255, 0, 0)], [0.5,(0, 0, 0)], [1,(0, 0, 0)]]
    grid = np.arange(0, ini['size']*2, 1)
    self.color = cmap(point, grid)
    self.particle = []
    self.lines = []
    self.canvas = tk.Canvas(master, width=ini['size'],
                            height=ini['size'], bg='#FFF')
    self.canvas.pack()
    self.setup(ini['px'], ini['py'], ini['vmax'])

  def setup(self, arrx, arry, vmax):
    canvas = self.canvas
    w, h = canvas.winfo_reqwidth()-4, canvas.winfo_reqheight()-4
    hx, hy = w/(arrx+1), h/(arry+1)
    for ix in range(arrx):
      for iy in range(arry):
        vx = np.random.randint(0, vmax)-vmax/2
        vy = np.random.randint(0, vmax)-vmax/2
        px, py = (ix+1)*hx, (iy+1)*hy
        oxi = canvas.create_oval(self.p_coords(px, py), fill='#000')
        txi = canvas.create_text(px, py, text=ix*arry+iy, fill='#FFF')
        dic = {'id_o': oxi, 'id_t': txi, 'x': px, 'y': py,
               'vx': vx, 'vy': vy}
        self.particle.append(dic)
    for i, p1 in enumerate(self.particle):
      for p2 in self.particle[i+1:]:
        lxi = canvas.create_line(p1['x'], p1['y'], p2['x'], p2['y'])
        dx, dy = p2['x']-p1['x'], p2['y']-p1['y']
        dr = np.sqrt(dx**2+dy**2)
        txi = canvas.create_text(dx/2+p1['x'], dy/2+p1['y'],
                                 text="{:.0f}".format(dr))
        canvas.tag_lower(lxi)
        self.lines.append({'id_l': lxi, 'id_t': txi})

  def ani(self):
    canvas = self.canvas
    ptcs = self.particle
    line = self.lines
    t0 = time.time()
    while True:
      dt = time.time()-t0
      for i, p1 in enumerate(ptcs):
        fx, fy = 0, 0
        for p2 in ptcs[i+1:]:
          dx, dy = p2['x']-p1['x'], p2['y']-p1['y']
          dr = np.sqrt(dx**2+dy**2)
          fx += force(dr)*dx
          fy += force(dr)*dy
        p1['vx'], p1['vy'] = fx*dt+p1['vx'], fy*dt+p1['vy']
        p1['x'], p1['y'] = p1['vx']*dt+p1['x'], p1['vy']*dt+p1['y']
        self.particle_move(p1, p1['x'], p1['y'])
      idx = 0
      for i, p1 in enumerate(ptcs):
        for p2 in ptcs[i+1:]:
          self.line_move(line[idx], p1['x'], p1['y'], p2['x'], p2['y'])
          idx += 1
      t0 += dt
      canvas.update()

  def p_coords(self, x, y):
    return [x-7, y-7, x+7, y+7]

  def particle_move(self, p, x, y):
    canvas = self.canvas
    if x <= 0:
      p['x'] = canvas.winfo_reqwidth()-4
    elif y <= 0:
      p['y'] = canvas.winfo_reqheight()-4
    elif x >= canvas.winfo_reqwidth()-4:
      p['x'] = 0
    elif y >= canvas.winfo_reqheight()-4:
      p['y'] = 0
    canvas.coords(p['id_o'], self.p_coords(p['x'], p['y']))
    canvas.coords(p['id_t'], p['x'], p['y'])

  def line_move(self, l, x1, y1, x2, y2):
    canvas = self.canvas
    x, y = (x2-x1)/2+x1, (y2-y1)/2+y1
    try:
      dr = int(np.sqrt((x2-x1)**2+(y2-y1)**2))
      col = self.color.get_colorcode(dr)
      canvas.itemconfig(l['id_l'], fill=col)
    except:
      pass
    canvas.coords(l['id_l'], x1, y1, x2, y2)
    canvas.itemconfig(l['id_t'], text=dr)
    canvas.coords(l['id_t'], x, y)

class cmap:
  def __init__(self, points, grid):
    d = len(grid)
    data = {}
    for i, x in enumerate(grid):
      pos = i/d
      for j in range(len(points)-1):
        if points[j][0] <= pos <= points[j+1][0]:
          ratio = (pos-points[j][0])/(points[j+1][0]-points[j][0])
          rgbi = np.array(points[j][1])
          rgbf = np.array(points[j+1][1])
          rgbd = ratio*(rgbf-rgbi)
          rgb = rgbi+rgbd
          c = "#{:02X}{:02X}{:02X}".format(int(rgb[0]),
                                           int(rgb[1]),
                                           int(rgb[2]))
          data[x] = c
    self.map = data

  def get_colorcode(self, x):
    return self.map[x]


root = tk.Tk()
root.title('2D motion')
view = md(root)
btn = tk.Button(root, text='run', command=view.ani)
btn.pack()
root.mainloop()
