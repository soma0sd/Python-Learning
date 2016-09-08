# -*- coding: utf-8 -*-
"""
Created on 2016-09-08

@ Author: soma0sd
@ Path: GUI/06_game1.py
@ Disc: 캔버스에서 키보드를 이용해 요소 이동시키기
@ License: MIT
"""
from tkinter import Tk, Canvas


def pre(e):
    global canv, user
    if e.keysym == 'Up':
        canv.move(user, 0, -3)
    elif e.keysym == 'Down':
        canv.move(user, 0, 3)
    elif e.keysym == 'Left':
        canv.move(user, -3, 0)
    elif e.keysym == 'Right':
        canv.move(user, 3, 0)
    canv.update()


master = Tk()
canv = Canvas(master, width=500, height=300)
canv.pack()

user = canv.create_oval(245, 145, 255, 155, fill="#000000")

master.bind('<Key>', pre)

master.mainloop()
