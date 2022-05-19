# -*- coding: utf-8 -*-
"""
Created on 2016-09-07

@ Author: soma0sd
@ Path: GUI/03_button.py
@ Disc: 프레임과 버튼을 사용해본다
@ License: MIT
"""
from tkinter import Tk, Canvas, Frame, Button
from numpy import random

master = Tk()

frame_left = Frame(master, width=400, height=400, bg="#FFFFFF")
frame_right = Frame(master, width=100, height=400, bg="#676767")
frame_left.pack(side='left')
frame_right.pack(side='top')


count = 0  # 캔버스에 그려진 오브젝트의 숫자를 세는 변수
can = Canvas(frame_left, width=400, height=400, bg="#FFFFFF")
tx_counter = can.create_text(20, 10, text="0")  # 오브젝트의 갯수 표시
can.pack()


def add_obj():
    """
    랜덤한 x, y지점에 크기가 [5, 5]인 원을 그리는 버튼명령
    """
    global count, can, tx_counter
    count += 1
    can.delete(tx_counter)
    tx_counter = can.create_text(20, 10, text=str(count))
    x, y = (random.randint(395), random.randint(395))
    can.create_oval(x, y, x+5, y+5, fill="#000")


def clear_can():
    """
    캔버스를 초기화 하는 버튼명령
    """
    global can, tx_counter, count
    can.destroy()
    can = Canvas(frame_left, width=400, height=400, bg="#FFFFFF")
    tx_counter = can.create_text(20, 10, text="0")
    can.pack()
    count = 0

"""
버튼 선언, commend변수에 버튼명령 담기
"""
btn_add = Button(frame_right, text="Add", width=10, command=add_obj)
btn_clear = Button(frame_right, text="clear", width=10, command=clear_can)
btn_add.pack()
btn_clear.pack()

master.mainloop()
