# -*- coding: utf-8 -*-
"""
Created on 2016-09-08

@ Author: soma0sd
@ Disc: matplotlib를 tkinter GUI에서 출력
@ License: MIT

사용하기 전에...
- 문제: matplotlib의 conda 버전과 tkinter의 충돌
- 해결법: pip버전으로 matplotlib 재설치
1) 시작 -> Anaconda -> Anaconda Promp실행
2) conda uninstall matplotlib 명령 -> y
3) pip install matplotlib 명령 -> y
4) spyder 실행 후 %matplotlib 입력
5) "Using matplotlib backend: TkAgg"메시지 확인
5) 다른 종류의 백엔드라면 %matplotlib tk 명령
"""
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk


fig = Figure()
plt = fig.add_subplot(111)
plt.plot([1, 2], [1, 2])

root = tk.Tk()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
root.update()
root.mainloop()
