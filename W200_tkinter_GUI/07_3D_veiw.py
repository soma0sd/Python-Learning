# -*- coding: utf-8 -*-
"""
Created on 2016-09-08

@ Author: soma0sd
@ Disc: 3D를 2D에서 표현하는 방법(연구용 데모)
@ License: MIT
"""
import tkinter as tk
import numpy as np


def onResize(event):
    global canv1, canv1_w, canv1_h
    e_w, e_h = event.width-4, event.height-4
    scalex, scaley = e_w/canv1_w, e_h/canv1_h
    canv1.scale("all", 0, 0, scalex, scaley)
    canv1_w, canv1_h = e_w, e_h


def onClick(event):
    global msX, msY
    msX, msY = event.x, event.y


def onDrag(event):
    dx, dy = event.x-msX, event.y-msY
    RTP_position(600, dx/10, dy/10, 50)


def RTP_position(R: float, iX: float, iY: float, scale: float=1.0):
    global canv1, coord, polygons, canv1_w, canv1_h, tset
    global canv2, navX, navY, tX, tY
    if len(polygons) != 0:
        for o in polygons:
            canv1.delete(o)
        for o in tset:
            canv1.delete(o)
        polygons = []
        tset = []
    tX += np.arctan2(iX, R)
    tY += np.arctan2(iY, R)
    ux, uy = 80*np.cos(tX)+100, 80*np.sin(tX)+100
    canv2.coords(navX, ux-5, uy-5, ux+5, uy+5)
    ux, uy = 80*np.cos(tY)+100, (80*np.sin(tY)*(1-np.sin(np.deg2rad(60))))+100
    canv2.coords(navY, ux-5, uy-5, ux+5, uy+5)
    cx, cy = canv1_w/2, canv1_h/2
    cX, cY, cZ = np.cos(np.arctan2(iX, R)), np.cos(np.arctan2(iY, R)), 1.0
    sX, sY, sZ = np.sin(np.arctan2(iX, R)), np.sin(np.arctan2(iY, R)), 0.0
    trans = [[cY*cZ, -sZ*cY, sY],
             [cZ*(-sY)*(-sX), cZ*cX, -sX*cY],
             [cZ*(-sY)*cX, cZ*sX, cY*cX]]
    for i in range(len(coord)):
        ix = coord[i][0]*trans[0][0]
        ix += coord[i][1]*trans[0][1]
        ix += coord[i][2]*trans[0][2]
        iy = coord[i][0]*trans[1][0]
        iy += coord[i][1]*trans[1][1]
        iy += coord[i][2]*trans[1][2]
        iz = coord[i][0]*trans[2][0]
        iz += coord[i][1]*trans[2][1]
        iz += coord[i][2]*trans[2][2]
        coord[i] = [ix, iy, iz]
    coset = [[coord[i][0]*scale+cx]+[coord[i][1]*scale+cy] for i in [0, 1, 2, 3]]
    polygons.append(canv1.create_polygon(coset, outline='#000', width=2, fill='#A4C', stipple="gray75"))
    coset = [[coord[i][0]*scale+cx]+[coord[i][1]*scale+cy] for i in [2, 3, 4, 5]]
    polygons.append(canv1.create_polygon(coset, outline='#000', width=2, fill='#CCA', stipple="gray75"))
    coset = [[coord[i][0]*scale+cx]+[coord[i][1]*scale+cy] for i in [4, 5, 6, 7]]
    polygons.append(canv1.create_polygon(coset, outline='#000', width=2,                             fill='#F00', stipple="gray75"))
    coset = [[coord[i][0]*scale+cx]+[coord[i][1]*scale+cy] for i in [0, 3, 4, 7]]
    polygons.append(canv1.create_polygon(coset, outline='#000', width=2,                             fill='#FF0', stipple="gray75"))
    coset = [[coord[i][0]*scale+cx]+[coord[i][1]*scale+cy] for i in [1, 0, 7, 6]]
    polygons.append(canv1.create_polygon(coset, outline='#000', width=2,                             fill='#0FF', stipple="gray75"))
    for i in range(len(coord)):
        tset.append(canv1.create_text(coord[i][0]*scale+cx, coord[i][1]*scale+cy, text=str(i)))

master = tk.Tk()
frame1 = tk.Frame(master)
frame2 = tk.Frame(master)
frame3 = tk.Frame(frame2)
frame1.pack(side='left', fill=tk.BOTH, expand=tk.YES)
frame2.pack(side='top')
frame3.pack(side='top', fill=tk.BOTH, expand=tk.YES)

canv1_w, canv1_h = 400, 400
canv1 = tk.Canvas(frame1, width=canv1_w, height=canv1_h, bg='#FFFFFF')
canv2 = tk.Canvas(frame2, width=200, height=200, bg="#000000")
canv1.pack(fill=tk.BOTH, expand=tk.YES)
canv2.pack(fill=tk.BOTH, expand=tk.YES)

coord = [[-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
         [-1, 1, 1], [1, 1, 1], [1, -1, 1], [-1, -1, 1]]
polygons = []
tset = []

tX, tY = 0, 0
canv2.create_oval(20, 20, 180, 180, outline="#0F0")
d = 80*np.sin(np.deg2rad(60))
canv2.create_oval(20, 20+d, 180, 180-d, outline="#0F0")
navX = canv2.create_oval(175, 95, 185, 105, fill="#FFF")
navY = canv2.create_oval(175, 95, 185, 105, outline="#66F", width=3)

RTP_position(300, 0, 0, 50)

msX, msY = 0, 0
canv1.bind("<Configure>", onResize)
canv1.bind('<Button-1>', onClick)
canv1.bind('<B1-Motion>', onDrag)
master.mainloop()
