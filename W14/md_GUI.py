# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 23:19:57 2016
@author: soma0sd
"""
class gui:
  def __init__(self):
    import tkinter as tk
    self.tk = tk
    self.root = tk.Tk()
    self.canvas = tk.Canvas(self.root, width=400, height=400, bg='#FFF')
    self.frame = tk.Frame(self.root)
    self.handle = {}
    self._frame_put()

  def _frame_put(self):
    tk = self.tk
    frame = self.frame
    """
    sub1: 실행, 초기화 버튼
    """
    sub1 = tk.Frame(frame, width=200)
    self.handle['run']   = b1 = tk.Button(sub1, text='RUN', width=10)
    self.handle['reset'] = b2 = tk.Button(sub1, text='RESET', width=10)
    b1.grid(row=0, column=0, sticky='w')
    b2.grid(row=0, column=1, sticky='e')
    sub1.grid(row=0, column=0, sticky='news')
    """
    sub2: 옵션 버튼
    """
    sub2 = tk.Frame(frame)
    lab1 = tk.Label(sub2, text='입자수')
    lab2 = tk.Label(sub2, text='온도')
    lab3 = tk.Label(sub2, text='분자량')
    lab1.grid(row=0, column=0, sticky='news')
    lab2.grid(row=1, column=0, sticky='news')
    lab3.grid(row=2, column=0, sticky='news')
    sub2.grid(row=2, column=0, sticky='news')
    """
    sub3: 분석창
    """
    sub3 = tk.Frame(frame)
    self.handle['bps'] = can1 = tk.Canvas(sub3, width=200, height=50)
    self.handle['avgT'] = can2 = tk.Canvas(sub3, width=200, height=50)
    can1.config(bg='#FFF')
    can2.config(bg='#FFF')
    can1.grid(row=0, column=0, sticky='news')
    can2.grid(row=2, column=0, sticky='news')
    sub3.grid(row=3, column=0, sticky='news')

  def mainloop(self):
    self.canvas.grid(row=0, column=0)
    self.frame.grid(row=0, column=1, sticky='news')
    self.root.mainloop()

