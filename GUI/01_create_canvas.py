# -*- coding: utf-8 -*-
"""
Created on 2016-09-06

@ Author: soma0sd

@ Path: GUI/01_create_canvas.py

@ Disc: 캔버스 만들어보기

@ License: MIT
"""
from tkinter import Tk, Canvas, mainloop
"""
tkinter: 위젯 형식의 GUI 라이브러리
tkinter.Tk: 프로그램 윈도우 관리자
tkinter.Canvas: 캔버스 생성, 관리
tkinter.mainloop: 창을 출력하는 함수
"""
master = Tk()
master.title("ex01")
"""
master안에 캔버스를 생성
"""
w = Canvas(master, width=300, height=200)
w.pack()
"""
캔버스에 사각형 추가
"""
w.create_rectangle(
    0, 0,
    w.winfo_screenwidth(), w.winfo_screenheight(),
    fill="#cc651d"
    )
w.create_rectangle(
    100, 50,  # 사각형을 그리기 시작할 지점
    200, 150,  # 사각형 그리기가 끝나는 지점
    fill="#ffc57e"  # 색상: "웹색상표" 참조
    )
"""
캔버스에 선 추가
"""
w.create_line(
    0, 100,
    300, 0,
    fill="#331dcc",
    width=2
    )
"""
캔버스에 텍스트 입력
"""
w.create_text(
    100, 30,  # 텍스트의 위치
    text="충북대학교 물리학과",  # 텍스트의 내용
    fill="#330033"  # 텍스트의 색상
    )
"""
캔버스에 원 그리기
"""
w.create_oval(
    50, 50,  # 원 시작시점 (사각형의 내부를 채우는 원을 그린다)
    100, 100,  # 원이 끝나는 지점
    fill="#696299",  # 원 채우기
    width=3,  # 선 두께
    outline="#f42288"  # 선 색상
    )

mainloop()
