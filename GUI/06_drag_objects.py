# -*- coding: utf-8 -*-
"""
Created on 2016-09-07

@ Author: soma0sd
@ Path: GUI/06-drag-objects.py
@ Disc: 여러 오브젝트를 선택한 후 움직이기
@ License: MIT
"""
from tkinter import Tk, Canvas

master = Tk()
can = Canvas(master, width=500, height=500)
can.pack()

master.mainloop()
