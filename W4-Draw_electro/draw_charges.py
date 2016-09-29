# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 16:37:27 2016

@author: soma0
"""
import tkinter as tk
import numpy as np


class charge:
    def __init__(self, canvas, **kw):
        self.canvas = canvas
        self.config = {'charge': 0,
                       'x': 0,
                       'y': 0,
                       'r': 15}
        self.config.update(kw)
        self.moveable = False
        self.draw()

    def draw(self):
        canvas = self.canvas
        cx, cy = self.config['x'], self.config['y']
        r = self.config['r']
        charge = self.config['charge']
        if charge == 0:
            c = '#000'
        elif charge > 0:
            c = '#F00'
        else:
            c = '#00F'
        self.obj = canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill=c)
        self.txt = canvas.create_text(cx, cy, text=str(charge), fill='#FFF')

    def is_mouse_on(self, event):
        mx, my = event.x, event.y
        x, y = self.config['x'], self.config['y']
        r = self.config['r']
        dr = np.sqrt((mx-x)**2+(my-y)**2)
        if dr < r:
            return True
        else:
            return False

    def move(self, event):
        x = event.x
        y = event.y
        r = self.config['r']
        canvas.coords(self.obj, x-r, y-r, x+r, y+r)
        canvas.coords(self.txt, x, y)


class select_menu:
    def __init__(self, canvas, **kw):
        self.canvas = canvas
        self.config = {'width': 400,
                       'height': 60}
        self.config.update(kw)
        self.btns = []
        self.objs = charge_obj(canvas, self)
        self.draw_menu()

    def draw_menu(self):
        width = self.config['width']
        height = self.config['height']
        canvas = self.canvas
        cy = height/2
        canvas.create_rectangle(0, 0, width, height, fill='#343434')
        for i in range(11):
            if i == 5:
                continue
            cx = (i+1)*(width+2)/12
            tmp = charge(canvas, x=cx, y=cy, charge=i-5)
            self.btns.append(tmp)

    def B1_action(self, event):
        btn = self.btns
        obj = self.objs.obj
        if event.y < self.config['height']:
            for i in btn:
                if i.is_mouse_on(event):
                    print("Select charge: "+str(i.config['charge']))
                    self.objs.add(i.config['charge'])
        else:
            self._sel_obj = None
            for i in obj:
                if i.is_mouse_on(event):
                    print("Select charge: "+str(i.config['charge']))
                    self._sel_obj = i

    def B1_moving(self, event):
        if self._sel_obj is not None:
            self._sel_obj.move(event)
        else:
            pass


class charge_obj:
    def __init__(self, canvas, menu):
        self.canvas = canvas
        self.obj = []
        self.menu = menu

    def add(self, ch):
        canvas = self.canvas
        w, h = self.menu.config['width'], self.menu.config['height']
        rx = np.random.randint(30, w)
        ry = np.random.randint(h, 400-h)
        tmp = charge(canvas, x=rx, y=ry, charge=ch)
        self.obj.append(tmp)


master = tk.Tk()
canvas = tk.Canvas(master, width=400, height=400, bg="#000")
canvas.pack()

menu = select_menu(canvas)
canvas.bind('<Button-1>', menu.B1_action)
canvas.bind('<B1-Motion>', menu.B1_moving)

master.mainloop()
