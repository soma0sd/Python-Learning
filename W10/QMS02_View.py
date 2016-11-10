# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 22:55:41 2016

@author: soma0sd

캔버스를 관리하는 클래스를 생성한다.
"""

class view:
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
  def set_lines(self, cx, cy, cz, acolor):
    import numpy as np
    self.reset()  # 캔버스 리셋
    if not len(cx) == len(cy) == len(cz) == len(acolor):
      print('Error(view.set_lines): 입력된 행렬의 크기가 다릅니다')
      return None
    _d = (self.viewr.winfo_reqheight()-4)/2  # 캔버스 Y 보정치
    for ac, ay, az, col in zip(cx, cy, cz, acolor):
      print(ac, np.array(ay)+_d, az, col)

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

if __name__ == '__main__':
  import tkinter as tk
  root = tk.Tk()
  v = view(root, width=300, height=100, bg='#FFF')
  v.pack()
  v.set_lines([[2, 4], [6, 8]], [[3, 5], [7, 9]], [[-1, -2], [-3, -4]], [1, 2])
  root.mainloop()