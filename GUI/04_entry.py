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
    """
    랜덤워크 함수.
    각 요소들이 x 방향으로 2씩 전진하면서 y축으로는 랜덤하게 움직이도록 만드는 함수
    """
    global run, obj, can, pos, result
    while run:
        pos += 2
        if pos >= 299:  # 화면 끝에 도달하면 정지
            pos = 0
            for o in obj:  # 도달한 오브젝트들의 y값을 도수분포표로 출력하는 루프
                x = can.coords(o)[1]+1
                for i in range(10):
                    if x > (i+1)*20:
                        continue
                    elif x < (i+1)*20:
                        result[i] += 1
                        break
            print(result)
            break
        for o in obj:  # 각요소가 [dx, yy] 만큼 움직이도록 루프
            can.move(o, 2, random.randint(5)-2)
        can.update()  # 캔버스 업데이트


def go():
    """
    애니메이션 초기화+실행 함수
    일시정지상태일 경우 남은 이동을 수행한다.
    """
    global obj, can, run, pos, member
    lim = int(member.get())
    if pos == 0:
        obj = [can.create_rectangle(0, 99, 2, 101) for i in range(lim)]
    run = True
    can.after(0, random_walk)


def stop():
    """
    일시정지 함수. random_walk의 while루프에 False를 줘서 임의로 정지시킴
    """
    global run, can
    run = False


"""
본문
2개의 프레임을 선언해서 캔버스와 메뉴 영역을 나눔
"""
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

"""
엔트리 요소
직접 타이핑을 통해 프로그램 안에서 변수를 통제
"""
member = StringVar()
member.set(100)
entry = Entry(frame_menu, textvariable=member)
entry.grid(row=0, column=1, columnspan=2, sticky=W)
# columnspan: 열1과 열2에 걸쳐서 레이아웃

"""
버튼
[go]와 [stop]버튼을 배치
"""
btn_go = Button(frame_menu, text="go", command=go)
btn_stop = Button(frame_menu, text="stop", command=stop)
btn_go.grid(row=1, column=1, sticky=W+E)
btn_stop.grid(row=1, column=2, sticky=W+E)

master.mainloop()
