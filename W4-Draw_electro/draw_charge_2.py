# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 19:12:47 2016

@author: soma0
"""
import tkinter as tk
import numpy as np


class obj_charge:
    def __init__(self, frame, **kw):
        self.frame = frame
        self.config = {'x': 0, 'y': 0, 'r': 15,
                       'charge': 0}
        self.config.update(kw)
        if self.config['charge'] == 0:
            c = '#000'
        elif self.config['charge'] > 0:
            c = '#F00'
        else:
            c = '#00F'
        x, y, r = self.config['x'], self.config['y'], self.config['r']
        ch = self.config['charge']
        self.oval = frame.canvas.create_oval(x-r, y-r, x+r, y+r, fill=c)
        self.text = canvas.create_text(x, y, text=str(ch), fill='#FFF')

    def is_mouse_on(self, event):
        mx, my = event.x, event.y
        cx, cy = self.config['x'], self.config['y']
        r = self.config['r']
        if (mx-cx)**2+(my-cy)**2 < r**2:
            return True
        else:
            return False

    def move(self, event):
        x, y, r = event.x, event.y, self.config['r']
        self.config['x'], self.config['y'] = x, y
        self.frame.canvas.coords(self.oval, x-r, y-r, x+r, y+r)
        self.frame.canvas.coords(self.text, x, y)

    def delete(self):
        self.frame.canvas.delete(self.oval)
        self.frame.canvas.delete(self.text)

    def is_crush(self, x, y):
        cx, cy = self.config['x'], self.config['y']
        r = self.config['r']
        if (x-cx)**2+(y-cy)**2 < r**2:
            return True
        else:
            return False


class obj_control:
    def __init__(self, menu):
        self.canvas = menu.canvas
        self.mw = menu.config['w']
        self.mh = menu.config['h']
        self.obj = []

    def add(self, e):
        x = np.random.randint(30, self.mw)
        y = np.random.randint(self.mh, 470)
        self.obj.append(obj_charge(self, x=x, y=y, charge=e))

    def selection(self, event):
        for i in self.obj:
            if i.is_mouse_on(event):
                print("object select:", i.config['charge'])
                return i

    def delete(self, element):
        ind = self.obj.index(element)
        self.obj[ind].delete()
        del self.obj[ind]


class menu:
    def __init__(self, canvas, **kw):
        self.config = {'w': 500, 'h': 60}
        self.config.update(kw)
        self.canvas = canvas
        self.control = obj_control(self)
        canvas.create_rectangle(0, 0, self.config['w'], self.config['h'],
                                fill='#333')
        self.btn = []
        for i in range(11):
            if i == 5:
                continue
            x = (i+1)*(self.config['w'])/12
            y = self.config['h']/2
            c = i - 5
            self.btn.append(obj_charge(self, x=x, y=y, charge=c))
        canvas.bind('<Button-1>', self.B1_action)
        canvas.bind('<B1-Motion>', self.B1_move)

    def B1_action(self, event):
        if event.y < self.config['h']:
            self._sel_obj = None
            for i in self.btn:
                if i.is_mouse_on(event):
                    print("select charge:", i.config['charge'])
                    self.control.add(i.config['charge'])
        else:
            self._sel_obj = self.control.selection(event)

    def B1_move(self, event):
        if self._sel_obj is not None:
            self._sel_obj.move(event)
            if event.y < self.config['h']:
                self.control.delete(self._sel_obj)
                self._sel_obj = None


class stream:
    def __init__(self, frame):
        self.frame = frame

    def ani(self):
        lines = []
        while True:
            charges = self.frame.control.obj
            for l in lines:
                self.frame.canvas.delete(l)
            lines = []
            for chg in charges:
                x0, y0, r = chg.config['x'], chg.config['y'], chg.config['r']
                counter = np.abs(np.abs(chg.config['charge'])*4)
                for l in range(counter):
                    theta = np.pi*2*l/counter
                    rx, ry = x0+r*np.cos(theta), y0+r*np.sin(theta)
                    coord = [rx, ry]
                    rx, ry = rx+3*np.cos(theta), ry+3*np.sin(theta)
                    coord += [rx, ry]
                    for i in range(40):
                        tx, ty = self.fE(coord, charges, chg)
                        coord += [tx, ty]
                    if chg.config['charge'] > 0:
                        c = '#F00'
                    else:
                        c = '#00F'
                    tml = self.frame.canvas.create_line(coord, fill=c)
                    lines.append(tml)
            self.frame.canvas.update()

    def fE(self, coord, charges, chg):
        ix, iy = coord[-4], coord[-3]
        fx, fy = coord[-2], coord[-1]
        r = np.sqrt((fx-ix)**2+(fy-iy)**2)
        theta = np.arctan2(fy-iy, fx-ix)
        bx, by = fx+r*np.cos(theta), fy+r*np.sin(theta)
        Ex, Ey = 1E-10, 1E-10
        k = 1E3
        crush = False
        for c in charges:
            if chg == c:
                continue
            ex, ey, ec = c.config['x'], c.config['y'], c.config['charge']
            etheta = np.arctan2(ey-iy, ex-ix)
            if chg.config['charge'] > 0:
                b = -1
            else:
                b = 1
            ers = b*k*ec/((ex-ix)**2+(ey-iy)**2)
            Ex += ers*np.cos(etheta)
            Ey += ers*np.sin(etheta)
        if crush:
            return fx, fy
        return bx+Ex, by+Ey


master = tk.Tk()
canvas = tk.Canvas(master, width=500, height=500, bg='#000')
canvas.pack()
menu = menu(canvas)
ani = stream(menu)
canvas.after(0, ani.ani())
master.mainloop()
