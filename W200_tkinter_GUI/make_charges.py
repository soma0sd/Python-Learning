# -*- coding: utf-8 -*-
"""
Created on 2016-09-22
@ Author: soma0sd
@ License: MIT
"""
import tkinter as tk
import numpy as np


class menu_btn:
    """
    전하 선택메뉴 클래스
    """
    def __init__(self, canvas, posx: int, posy: int, charge: int):
        self.Canvas = canvas
        self.Position = (posx, posy)
        if charge > 0:
            self.Item = self.Canvas.create_oval(
                posx-15, posy-15, posx+15, posy+15, fill='#F00')
        else:
            self.Item = self.Canvas.create_oval(
                posx-15, posy-15, posx+15, posy+15, fill='#00F')
        self.Canvas.create_text(self.Position, text=str(charge), fill='#FFF')
        self.Charge = charge

    def is_MouseOn(self, event):
        posx = self.Position[0] - event.x
        posy = self.Position[1] - event.y
        if posx**2 + posy**2 < 15**2:
            print('on charge: '+str(self.Charge))
            return True
        else:
            return False

    def clone(self):
        x = np.random.randint(30, 370)
        y = np.random.randint(30, 370)
        return objects(self.Canvas, x, y, self.Charge)


class objects:
    """
    생성된 전하를 관리하는 클래스
    """
    def __init__(self, canvas, posx: int, posy: int, charge: int):
        self.Canvas = canvas
        self.Position = (posx, posy)
        if charge > 0:
            self.Item = self.Canvas.create_oval(
                posx-15, posy-15, posx+15, posy+15, fill='#F00')
        else:
            self.Item = self.Canvas.create_oval(
                posx-15, posy-15, posx+15, posy+15, fill='#00F')
        self.text = self.Canvas.create_text(
            self.Position, text=str(charge), fill='#FFF')
        self.Charge = charge

    def is_MouseOn(self, event):
        posx = self.Position[0] - event.x
        posy = self.Position[1] - event.y
        if posx**2 + posy**2 < 40:
            return True
        else:
            return False

    def move(self, event):
        self.Position = (event.x, event.y)
        posx, posy = event.x, event.y
        self.Canvas.coords(self.Item, posx-15, posy-15, posx+15, posy+15)
        self.Canvas.coords(self.text, posx, posy)


"""
전역함수
"""
def ClickAct(event):
    global MenuBar, canvas, objs, selobj
    selobj = None
    if event.x > 400:
        for t in MenuBar:
            if t.is_MouseOn(event) is True:
                objs.append(t.clone())
    else:
        for t in objs:
            if t.is_MouseOn(event) is True:
                selobj = t
                break


def DragAct(event):
    global selobj
    if selobj is not None:
        selobj.move(event)

"""
메인함수
"""
master = tk.Tk()
canvas = tk.Canvas(master, width=500, height=400, bg='#FFF')
canvas.pack()
canvas.create_rectangle(400, 0, 500, 400, fill='#AAA')

MenuBar = []
MenuBar.append(menu_btn(canvas, 430, 50, 1))
MenuBar.append(menu_btn(canvas, 470, 50, -1))
MenuBar.append(menu_btn(canvas, 430, 100, 2))
MenuBar.append(menu_btn(canvas, 470, 100, -2))
MenuBar.append(menu_btn(canvas, 430, 150, 3))
MenuBar.append(menu_btn(canvas, 470, 150, -3))
MenuBar.append(menu_btn(canvas, 430, 200, 4))
MenuBar.append(menu_btn(canvas, 470, 200, -4))


objs = []
selobj = None
canvas.bind("<Button-1>", ClickAct)
canvas.bind("<B1-Motion>", DragAct)

master.mainloop()
