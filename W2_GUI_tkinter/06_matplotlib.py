# -*- coding: utf-8 -*-
"""
Created on 2016-09-08

@ Author: soma0sd
@ Disc: matplotlib를 tkinter GUI에서 출력
@ License: MIT

사용하기 전에...
- 문제: matplotlib의 conda 버전과 tkinter의 충돌
- 해결법: pip버전으로 matplotlib 재설치
1) 시작 -> Anaconda -> Anaconda Prompt실행
2) conda uninstall matplotlib 명령 -> y
3) pip install matplotlib 명령 -> y
4) spyder 실행 후 %matplotlib 입력
5) "Using matplotlib backend: TkAgg"메시지 확인
5) 다른 종류의 백엔드라면 %matplotlib tk 명령
"""
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy.random as random


def generate():
    global frame2, hist, sub, fig, randset
    bins = mu+sigma*random.randn(100)
    print(type(sub))
    randset = list(randset) + list(bins)
    hist = sub.hist(randset, 50)
    fig.canvas.draw()


mu, sigma = 100, 10
master = tk.Tk()
frame1 = tk.Frame(master, width=100, height=300)
frame2 = tk.Frame(master, width=300, height=300)
frame1.pack(side='left')
frame2.pack()

fig, sub = plt.subplots(1, 1)
randset = mu + sigma*random.randn(100)
hist = sub.hist(randset, 50)
canvas = FigureCanvasTkAgg(fig, master=frame2)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

btn1 = tk.Button(frame1, text="generate", command=generate)
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

master.mainloop()
