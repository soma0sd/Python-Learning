# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 22:55:41 2016

@author: soma0sd

캔버스를 관리하는 클래스를 생성한다.
@ 이전 주차의 모듈에서 변화
"""

class qview:
  def __init__(self, master, **kw):
    import tkinter
    self.frame = tkinter.Frame(master)
    # 캔버스 초기화
    self.viewx = tkinter.Canvas(self.frame, **kw)
    self.viewy = tkinter.Canvas(self.frame, **kw)
    self.viewr = tkinter.Canvas(self.frame, **kw)
    # 캔버스 제목 달기
    self.viewx.create_text(4, 2, text='x-axis', anchor='nw')
    self.viewy.create_text(4, 2, text='y-axis', anchor='nw')
    self.viewr.create_text(4, 2, text='result', anchor='nw')
    # 캔버스 레이아웃
    self.viewx.grid(row=0, column=0)
    self.viewy.grid(row=1, column=0)
    self.viewr.grid(row=2, column=0)

  """
  코어 함수
  @ set_lines: 나열 가능한 좌표와 색상 세트를 받아와서 캔버스에 표시
    좌표와 색상은 크기가 같은 집합이어야 한다.
  """
  def set_lines(self, cx, cy, cz, acolor, mass):
    import numpy as np
    self.reset()  # 캔버스 리셋
    if not len(cx) == len(cy) == len(cz) == len(acolor):
      print('Error(view.set_lines): 입력된 행렬의 크기가 다릅니다')
      return None
    # ViewX와 ViewY를 그린다
    _d = (self.viewr.winfo_reqheight()-4)/2  # 캔버스 Y 보정치
    for ax, ay, az, c in zip(cx, cy, cz, acolor):
      ax = list(np.array(ax)+_d)
      ay = list(np.array(ay)+_d)
      v1, v2 = [], []
      for i in range(len(ax)):
        v1 += [az[i], ax[i]]
        v2 += [az[i], ay[i]]
      self.viewx.create_line(v1, fill=c)
      self.viewy.create_line(v2, fill=c)
    # 결과창을 그린다. 현재는 컬러맵만 지원
    _d = self.viewr.winfo_reqwidth()/(len(mass)+1)
    _w = (_d/2) - 2
    _h = self.viewr.winfo_reqheight()-4
    for i, m, c in zip(range(len(mass)), mass, acolor):
      x = (i+1)*_d
      self.viewr.create_rectangle(x-_w, _h, x+_w, _h-15, fill=c)
      self.viewr.create_text(x, _h, text=m, anchor='s', fill='#FFF')

  """
  기능 함수
  @ reset: 캔버스를 모두 초기화
  """
  def reset(self):
    self.viewx.delete('all')
    self.viewy.delete('all')
    self.viewr.delete('all')
    self.viewx.create_text(4, 2, text='x-axis', anchor='nw')
    self.viewy.create_text(4, 2, text='y-axis', anchor='nw')
    self.viewr.create_text(4, 2, text='result', anchor='nw')

  """
  지원함수
  """
  def pack(self, **kw):
    self.frame.pack(**kw)

  def grid(self, **kw):
    self.frame.grid(**kw)