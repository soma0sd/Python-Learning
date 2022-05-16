# -*- coding: utf-8 -*-
"""
tkinter GUI의 기본적인 구조를 익힌다.

@author: soma0sd
"""
import tkinter as tk

app = tk.Tk()
app.title("app")
app.mainloop()
print("프로그램 종료 후")

"""
Tk는 하나의 GUI 응용프로그램을 나타낸다
mainloop앞의 모든 명령을 적용한 뒤에 GUI를 표시하고,
GUI를 종료하면 mainloop 다음의 명령이 실행된다.
"""
