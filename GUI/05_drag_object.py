# -*- coding: utf-8 -*-
"""
Created on 2016-09-07

@ Author: soma0sd
@ Path: GUI/05_drag_object.py
@ Disc: 캔버스에서 드래그를 이용해 통해 물체를 움직이는 예제
@ License: MIT
"""
from tkinter import Tk, Canvas
import numpy as np


def onClick(e):
    global obj, can, onTaget
    minx = can.coords(obj)[0]
    miny = can.coords(obj)[1]
    maxx = can.coords(obj)[2]
    maxy = can.coords(obj)[3]
    if minx < e.x < maxx and miny < e.y < maxy:
        onTaget = True
    else:
        onTaget = False


def onDrag(e):
    global obj, can, onTaget
    if not onTaget:
        return None
    can.coords(obj, e.x-10, e.y-10, e.x+10, e.y+10)


def web():
    global can, linex, liney, obj
    ratio = 500
    while True:
        cx = can.coords(obj)[0]+10
        cy = can.coords(obj)[1]+10
        for y in range(0, 501, 10):
            posx = ()
            posy = ()
            for x in range(0, 501, 10):
                r = np.sqrt((x-cx)**2+(y-cy)**2)
                if r == 0:
                    m = ratio
                else:
                    m = ratio / r*2
                posx += (x, y-m)
                posy += (x, y)
            can.delete(linex[int(y/50)])
            can.delete(liney[int(y/50)])
            linex[int(y/50)] = [can.create_line(posx, fill='#f00', dash=(3, 2))]
            liney[int(y/50)] = [can.create_line(posy, fill='#000')]
        can.update()

master = Tk()
can = Canvas(master, width=500, height=500)
obj = can.create_oval(240, 240, 260, 260, fill='#aafcdf')
can.pack()

linex = [can.create_line(0, 0, 1, 1, fill='#f00', dash=(3, 2))]*11
liney = [can.create_line(0, 0, 1, 1, fill='#f00', dash=(3, 2))]*11

can.after(0, web)
onTaget = False
can.bind('<Button-1>', onClick)
can.bind('<B1-Motion>', onDrag)

master.mainloop()
