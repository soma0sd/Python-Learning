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
        if self.opt['r']**2 < ix**2+iy**2:
            return True
        else:
            return False


class AddMenu:
    def __init__(self, canvas, **kw):
        self.opt = {'w': 500, 'h': 50, 'maxima': 5}
        self.opt.update(kw)
        self.canvas = canvas
        self.btn = []
        # Menu Draw
        maxi = self.opt['maxima']
        width = self.opt['w']
        cy = self.opt['h']/2
        for i in range(maxi*2+1):
            if i == maxi:
                continue
            SingleCharge(canvas, (i+1)*width/(maxi*2+2), cy, i-maxi)


master = tk.Tk()
canvas = tk.Canvas(master, width=500, height=500, bg='#000')
canvas.pack()
AddMenu(canvas)
master.mainloop()
