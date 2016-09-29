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


master = tk.Tk()
canvas = tk.Canvas(master, width=500, height=500, bg='#000')
canvas.pack()
control(canvas)
master.mainloop()
