# -*- coding: utf-8 -*-
"""
Created on 2016-09-07

@ Author: soma0sd
@ Path: GUI/04_entry.py
@ Disc: 간단한 텍스트 입력을 받아오는 엔트리를 사용해본다
@ License: MIT
"""
from tkinter import Tk, Frame, Canvas, Entry, StringVar, Button, W, E
from numpy import random


def random_walk():
    global run, obj, can, pos, result
    while run:
        pos += 2
        if pos >= 299:
            pos = 0
            for o in obj:
                x = can.coords(o)[1]+1
                for i in range(10):
                    if x > (i+1)*20:
                        continue
                    elif x < (i+1)*20:
                        result[i] += 1
                        break
            print(result)
            break
        for o in obj:
            can.move(o, 2, random.randint(5)-2)
        can.update()


def go():
    global obj, can, run, pos, member
    lim = int(member.get())
    if pos == 0:
        obj = [can.create_rectangle(0, 99, 2, 101) for i in range(lim)]
    run = True
    can.after(0, random_walk)


def stop():
    global run, can
    run = False

result = [0]*10
pos = 0
master = Tk()

frame_main = Frame(master, width=400, height=200)
frame_canv = Frame(frame_main, width=300, height=200, bg='#FFF')
frame_menu = Frame(frame_main, width=100, height=200, bg='#777')
frame_main.pack(side='top')
frame_canv.pack(side='left')
frame_menu.pack()

can = Canvas(frame_canv, width=300, height=200)
can.pack()

member = StringVar()
member.set(100)
entry = Entry(frame_menu, textvariable=member)
entry.grid(row=0, column=1, columnspan=2, sticky=W)

btn_go = Button(frame_menu, text="go", command=go)
btn_stop = Button(frame_menu, text="stop", command=stop)
btn_go.grid(row=1, column=1, sticky=W+E)
btn_stop.grid(row=1, column=2, sticky=W+E)

master.mainloop()
