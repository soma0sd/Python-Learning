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
    """
    클릭했을 때 원을 클릭했는지 배경을 클릭했는지를 판단.
    이후 드래그에 따라 요소가 움직일지 말지를 결정
    """
    global obj, can, onTarget
    minx = can.coords(obj)[0]
    miny = can.coords(obj)[1]
    maxx = can.coords(obj)[2]
    maxy = can.coords(obj)[3]
    if minx < e.x < maxx and miny < e.y < maxy:
        onTarget = True
    else:
        onTarget = False


def onDrag(e):
    """
    만약 원을 클릭했을 때, 드래그하는 동안 원이 마우스를 따라가도록 하는 함수
    """
    global obj, can, onTarget
    if not onTarget:
        return None
    can.coords(obj, e.x-10, e.y-10, e.x+10, e.y+10)


def web():
    """
    원의 위치에 따라 영향받는 주변 환경을 표현
    1/r 법칙에 따름
    """
    global can, line1, line2, obj
    ratio = 300
    while True:
        cx = can.coords(obj)[0]+10
        cy = can.coords(obj)[1]+10
        for y in range(0, 500, 50):
            pos1 = ()
            pos2 = ()
            for x in range(0, 501, 10):
                r = np.sqrt((x-cx)**2+(y-cy)**2)
                if r == 0:
                    m = ratio
                else:
                    m = ratio / r
                pos1 += (x, y)
                pos2 += (x, y-m)
            can.delete(line1[int(y/50)])
            can.delete(line2[int(y/50)])
            line1[int(y/50)] = [can.create_line(pos1, fill='#000')]
            line2[int(y/50)] = [can.create_line(pos2, fill='#f00',
                                dash=(3, 2))]
        can.update()

"""
본문
캔버스를 선언하고 원과 선들을 초기화
"""
master = Tk()
can = Canvas(master, width=500, height=500)
obj = can.create_oval(240, 240, 260, 260, fill='#aafcdf')
can.pack()

# 라인 초기화
line1 = [can.create_line(0, 0, 1, 1)]*11
line2 = [can.create_line(0, 0, 1, 1)]*11

# 애니메이션 구동
can.after(0, web)
onTarget = False

# bind: 미리 정해져 있는 입력에 따라서 함수를 실행
# 사용자의 드래그 동작은 클릭과 클릭한 후 이동으로 구성되어 있다.
can.bind('<Button-1>', onClick)
can.bind('<B1-Motion>', onDrag)

master.mainloop()
