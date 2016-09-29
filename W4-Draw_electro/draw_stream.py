# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 18:03:10 2016
@author: soma0sd
"""
import tkinter as tk
import numpy as np


class SingleCharge:
    def __init__(self, canvas, x, y, charge, **kw):
        self.opt = {'r': 15}
        self.opt.update(kw)
        self.canvas = canvas
        self.x = x
        self.y = y
        self.charge = charge
        # Draw Charge
        r = self.opt['r']
        if charge > 0:
            c = '#F00'
        if charge < 0:
            c = '#00F'
        self.oval = canvas.create_oval(x-r, y-r, x+r, y+r, fill=c)
        self.text = canvas.create_text(x, y, text=str(charge), fill='#FFF')

    def is_crush(self, x, y):
        ix = x - self.x
        iy = y - self.y
        if self.opt['r']**2 > ix**2+iy**2:
            return True
        else:
            return False

    def clone(self, **kw):
        option = {'x': np.random.randint(30, 470),
                  'y': np.random.randint(80, 470)}
        option.update(kw)
        return SingleCharge(self.canvas, option['x'],  option['y'],
                            self.charge)

    def move(self, x, y):
        self.x = x
        self.y = y
        r = self.opt['r']
        self.canvas.coords(self.oval, x-r, y-r, x+r, y+r)
        self.canvas.coords(self.text, x, y)

    def delete(self):
        self.canvas.delete(self.oval)
        self.canvas.delete(self.text)


class control:
    def __init__(self, canvas, **kw):
        self.opt = {'w': 500, 'h': 50, 'maxima': 5}
        self.opt.update(kw)
        self.canvas = canvas
        self.btn = []
        self.object = []
        self._flag = None
        # Menu Draw
        maxi = self.opt['maxima']
        width = self.opt['w']
        cy = self.opt['h']/2
        for i in range(maxi*2+1):
            if i == maxi:
                continue
            bt = SingleCharge(canvas, (i+1)*width/(maxi*2+2), cy, i-maxi)
            self.btn.append(bt)
        canvas.bind('<Button-1>', self.B1Action)
        canvas.bind('<B1-Motion>', self.B1Motion)
        canvas.after(0, self.animation)

    def B1Action(self, event):
        # Find active button
        self._flag = None
        for b in self.btn:
            if b.is_crush(event.x, event.y):
                self.object.append(b.clone())
        for o in self.object:
            if o.is_crush(event.x, event.y):
                self._flag = o

    def B1Motion(self, event):
        if self._flag is None:
            return None
        self._flag.move(event.x, event.y)
        if event.y < 50:
            self.delete_object(self._flag)

    def delete_object(self, obj):
        obj.delete()
        del self.object[self.object.index(obj)]
        return None

    def animation(self):
        dr = 3
        lines = []
        while True:
            for li in lines:
                self.canvas.delete(li)
            lines = []
            for o in self.object:
                chg = o.charge
                N = np.abs(chg*4)
                for li in range(N):
                    theta = np.pi*2*li/N
                    ix = o.x+o.opt['r']*np.cos(theta)
                    iy = o.y+o.opt['r']*np.sin(theta)
                    lines.append(self._draw_stream(ix, iy, dr, theta, o))
            self.canvas.update()

    def _draw_stream(self, ix, iy, r, theta, obj):
        x, y = ix+r*np.cos(theta), iy+r*np.sin(theta)
        crd = [ix, iy, x, y]
        i = 0
        while 0 < x < 500 and 50 < y < 500 and self._is_line_crush(x, y):
            r = np.sqrt((crd[-2]-crd[-4])**2+(crd[-1]-crd[-3])**2)
            theta = np.arctan2(crd[-1]-crd[-3], crd[-2]-crd[-4])
            Er, Et = self._CalcE(x, y, obj)
            nx = r*np.cos(theta)+Er*np.cos(Et)
            ny = r*np.sin(theta)+Er*np.sin(Et)
            theta = np.arctan2(ny, nx)
            x = x+r*np.cos(theta)
            y = y+r*np.sin(theta)
            crd += [x, y]
            i += 1
        if obj.charge > 0:
            c = '#F00'
        else:
            c = '#00F'
        return self.canvas.create_line(crd, fill=c)

    def _CalcE(self, x, y, obj):
        Ex, Ey = 0, 0
        ratio = 5E3
        for o in self.object:
            if obj.charge > 0:
                k = -1
            else:
                k = 1
            Er = k*ratio*o.charge/((o.x-x)**2+(o.y-y)**2)
            Et = np.arctan2(o.y-y, o.x-x)
            Ex += Er*np.cos(Et)
            Ey += Er*np.sin(Et)
        Er = np.sqrt(Ex**2+Ey**2)
        Et = np.arctan2(Ey, Ex)
        return Er, Et

    def _is_line_crush(self, x, y):
        for o in self.object:
            if o.is_crush(x, y):
                return False
        return True


master = tk.Tk()
canvas = tk.Canvas(master, width=500, height=500, bg='#000')
canvas.pack()
control(canvas)
master.mainloop()
