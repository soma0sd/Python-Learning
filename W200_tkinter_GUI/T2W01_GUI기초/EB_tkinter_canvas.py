# -*- coding: utf-8 -*-
"""
tkinter GUI에 캔버스를 추가한다.

@author: soma0sd
"""
import tkinter as tk

app = tk.Tk()  # GUI 시작
canvas = tk.Canvas(app, width=400, height=300, bg="#FFF")
canvas.pack()
"""
## Canvas의 선언
>>>tkinter.Canvas($상위, $옵션)
캔버스는 배치 이후에도 내용을 수정할 수 있는 그리기 요소.
  $상위(필수): 상위 레이아웃을 나타낸다.
  $옵션: 추가속성들을 정한다. 쉼표로 구분한다.
    * width: 정수형 너비(px)
    * height: 정수형 높이(px)
    * bg/background: 16진수 배경색

## tkinter의 색상
색상은 일반적으로 16진수를 이용한다.
3자리와 6자리 표시중에서 선택할 수 있다.
각 자릿수는 빨강(R), 초록(G), 파랑(B)의 정도를 나타내며
"#RGB" 혹은 "#RRGGBB"로 나타낸다.

## Canvas의 배치
>>>tkinter.Canvas.pack()
"""
cx = 200
cy = 150
for r, b in zip(range(150, 10, -20), range(0, 16, 2)):
    color = "#F{}F".format(hex(b)[-1])
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill=color)
"""
## 캔버스 아이템
>>>Canvas.create_{도형}($위치, $속성)
참고: http://effbot.org/tkinterbook/canvas.htm

캔버스에 그림을 그린다.
예시인 oval(타원)은 두 점(x1, y1, x2, y2)을 꼭지점으로 하는 직사각형에 외접하는
타원을 그린다.
"""
app.mainloop()  # GUI 끝
