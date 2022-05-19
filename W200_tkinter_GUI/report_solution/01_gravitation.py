# -*- coding: utf-8 -*-
"""
Created on 2016-09-12

@ Author: soma0sd
@ Disc: (과제힌트 1)중력: 입자의 궤적
@ License: MIT
"""
import tkinter as tk
import numpy as np
import time
"""
CONSTANT
"""
canvasW = 800
canvasH = 800
scale = 1/2E5  # 픽셀당 m
tscale = 4E2  # 시간 가속
frame_time = 0.05  # 프레임 시간

G = 6.67408E-14  # m^3 kg^-1 s^2, 중력상수
earth_mass = 5.972E24   # kg, 지구의 질량
earth_r = 6317000  # m, 지구 반지름(평균)
m1 = 11567  # kg, 허블망원경 기준
m1_count = 300  # 위성 발사갯수
v0 = 11000 + 5000*np.random.randn(m1_count)  # 속도: 정규분포
T0 = np.random.rand(m1_count)*np.pi*2*30/360-(np.pi/8)
y0 = canvasH/2*np.random.rand(m1_count) - canvasH/4
# 각도: 0-60도 랜덤


def next_position(ix, iy, iv, theta):
    global G, frame_time, tscale, scale, eX, eY, dr
    iv *= scale
    dt = tscale*frame_time
    rx, ry = (eX-ix)/scale, (eY-iy)/scale
    r = np.sqrt(rx**2 + ry**2)
    if r < dr:
        return 0, 0, 0, 0, 0
    rt = np.arctan2(ry, rx)
    a = G*earth_mass/(r**2)
    dx = (iv*np.cos(theta))*dt + (a*np.cos(rt))*(dt**2)/2
    dy = (iv*np.sin(theta))*dt + (a*np.sin(rt))*(dt**2)/2
    fx, fy = ix+dx, iy+dy
    theta = np.arctan2(dy, dx)
    return dx, dy, fx, fy, theta


def run():
    global canv, v0, T0, y0, m1_count, eX, eY, dr, frame_time
    comet = []
    ix = 2
    for m in range(m1_count):
        iy = eY + y0[m]
        v = v0[m]
        theta = T0[m]
        obj = canv.create_rectangle(ix-2, iy-2, ix+2, iy+2, fill='#F00')
        comet.append([obj, ix, iy, v, theta])
    while True:
        time.sleep(frame_time)
        for m in range(m1_count):
            obj, ix, iy = comet[m][0], comet[m][1], comet[m][2]
            v, theta = comet[m][3], comet[m][4]
            dx, dy, x, y, ft = next_position(ix, iy, v, theta)
            canv.move(obj, dx, dy)
            comet[m] = [obj, x, y, v, theta, ft]
            if (eX-dr) <= x <= (eX+dr) and (eY-dr) <= y <= (eY+dr):
                canv.delete(obj)
        canv.update()

master = tk.Tk()
canv = tk.Canvas(master, width=canvasW, height=canvasH)
canv.pack()

eX, eY = canvasW/2, canvasH/2
dr = scale*earth_r
earth_obj = canv.create_oval(eX-dr, eY-dr, eX+dr, eY+dr)

canv.after(0, run)
master.mainloop()
