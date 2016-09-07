# -*- coding: utf-8 -*-
"""
Created on 2016-09-06

@ Author: soma0sd
@ Path: GUI/02_animation.py
@ Disc: 캔버스에서 애니메이션 구동
@ License: MIT
"""
from tkinter import Tk, Canvas
import numpy as np
import time

master = Tk()
master.title("animation")
can = Canvas(master, width=400, height=200)
can.pack()
can.create_rectangle(0, 0, 400, 200, fill="#ffffff")
"""
원 그리기
"""
ovals = []
for x in range(20):
    for y in range(10):
        obj = can.create_oval(x*20, y*20, (x+1)*20, (y+1)*20)
        ovals.append(obj)
"""
움직일 선을 그리면서 초기위치정보 저장
"""
lines = []
position = []
for x in range(20):
    for y in range(10):
        theta = (x / 20) * 2 * np.pi
        r = 10
        bx = (x+0.5)*20
        by = (y+0.5)*20
        position.append((bx, by, r, theta))
        mx = r * np.cos(theta)
        my = r * np.sin(theta)
        obj = can.create_line(bx, by, bx+mx, by+my)
        lines.append(obj)
can.pack()


def animation():
    """
    에니메이션 함수
    선을 매 시간마다 새로 그림
    """
    global lines, position, can
    while True:  # 프로그램 종료시까지 루프
        time.sleep(0.025)  # 0.025초 만큼 정지
        for i in range(len(lines)):
            ix, iy, r, theta = position[i]
            theta += (1/30)*2*np.pi
            mx = r * np.cos(theta)
            my = r * np.sin(theta)
            can.delete(lines[i])  # 기존라인 삭제
            lines[i] = can.create_line(ix, iy, ix+mx, iy+my)
            # 새로운 라인 생성
            position[i] = (ix, iy, r, theta)
            # 새로운 라인 위치정보 저장
        can.update()  # 캔버스 업데이트

master.after(0, animation)
master.mainloop()
