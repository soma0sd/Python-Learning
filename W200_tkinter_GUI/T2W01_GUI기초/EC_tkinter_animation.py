# -*- coding: utf-8 -*-
"""
tkinter 캔버스에 있는 도형을 움직여 애니메이션을 만든다.
  -Simple Pendulum

@author: soma0sd
"""
import tkinter as tk
import numpy as np
import time

l = 200  # [px] 진자의 길이
r = 7    # [px] 추의 반지름
T = 0.5  # [rad] 초기각도

app = tk.Tk()  # GUI 시작
canvas = tk.Canvas(app, width=300, height=400, bg="#FFF")
canvas.pack()

"""
도형 초기화 단계: 진자 생성
"""
cw = 150  # 화면 폭의 절반
ox = l*np.sin(T)
oy = l*np.cos(T)
line_id = canvas.create_line(cw, 0, cw+ox, oy)
pend_id = canvas.create_oval(cw+ox-r, oy-r, cw+ox+r, oy+r, fill='#00F')


def animation():
    """
    애니메이션 함수: v = -w*A*cos(wt-pi)
    """
    global canvas, t0

t0 = time.time()
app.after(0, animation)
app.mainloop()
