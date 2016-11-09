# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 14:29:06 2016
@author: soma0sd

color map을 만드는 방법
"""
import tkinter as tk
import numpy as np


"""
다른 문서에서도 이용할 수 있도록 클레스를 제작한다
"""
class cmap:
  def __init__(self, points, grid):
    d = len(grid)
    data = {}
    for i, x in enumerate(grid):
      pos = i/d
      for j in range(len(points)-1):
        if points[j][0] <= pos <= points[j+1][0]:
          ratio = (pos-points[j][0])/(points[j+1][0]-points[j][0])
          rgbi = np.array(points[j][1])
          rgbf = np.array(points[j+1][1])
          rgbd = ratio*(rgbf-rgbi)
          rgb = rgbi+rgbd
          c = "#{:02X}{:02X}{:02X}".format(int(rgb[0]), int(rgb[1]), int(rgb[2]))
          data[x] = c
    self.map = data

  def get_colorcode(self, x):
    return self.map[x]


if __name__ == '__main__':
  """
  초기조건
  웹 색상을 기준으로 다중 포인트 그래디언트 생성

  @ point
    각 컬러세트는 해당 포인트가 위치하는 [0, 1]의 부동소수점,
    해당하는 [0, 255]의 정수형 RGB 색상값으로 이루어져 있다.

  @ grid
    나열 가능한 숫자형 변수
  """
  point = [[0, (0, 0, 0)], [0.5, (255, 0, 0)], [1,(255, 150, 150)]]
  grid = np.arange(50, 255, 5)

  """
  tkinter의 Canvas에 적용한 예
  """
  root = tk.Tk()
  root.title('Color maping')
  canvas = tk.Canvas(root, width=300, height=150, bg='#FFF')
  canvas.pack()
  _ = cmap(point, grid)
  for x in grid:
    canvas.create_rectangle(x, 50, x+5, 100,fill=_.get_colorcode(x), width=0)
  root.mainloop()
