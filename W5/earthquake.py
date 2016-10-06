# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 14:45:39 2016

@author: soma0sd
"""
import tkinter as tk
import numpy as np
import time


class geometry(tk.Canvas):
    """
    geometry 클래스
    tkinter의 Canvas를 가져온다. 이 클래스는 기존 Canvas의 기능을 확장하는 개념
    """
    wave_v = 50  # px per seconds

    def __init__(self, *arg, **kw):
        tk.Canvas.__init__(self, *arg, **kw)
        self.t0 = 0
        self.pack()
        self.is_run = True  # 초기화를 위한 while loop 제어 변수
        self.epicenter = {'x': 0, 'y': 0, 'obj': 0}  # 진앙데이터
        """
        관측소 데이터
        N: 관측소 번호, [x, y]: 위치, obj: 캔버스 내부ID
        t: 기록된 시간
        * 캔버스를 가로, 세로로 각각 삼등분하여 배치 -> [xd, yd] 참조
        """
        xd, yd = (self.winfo_reqwidth()-4)/3, (self.winfo_reqheight()-4)/3
        detector1 = {'N': 1, 'x': xd*1.5, 'y': yd, 'obj': 0, 't': None}
        detector2 = {'N': 2, 'x': xd, 'y': yd*2, 'obj': 0, 't': None}
        detector3 = {'N': 3, 'x': xd*2, 'y': yd*2, 'obj': 0, 't': None}
        self.detector = [detector1, detector2, detector3]

    def earthquake_run(self):
        self.is_run = True  # ->(L23)
        t0 = time.time()  # 지진이 일어난 시각을 기록
        """
        캔버스 크기(w, h)를 가져와 랜덤으로 지진이 발생
        지진파의 속도는 [self.wave_v]->(L17)
        [_o]는 진앙을 표시하는 oval
        """
        w, h = self.winfo_reqwidth()-4, self.winfo_reqheight()-4
        x = self.epicenter['x'] = np.random.randint(4, w)
        y = self.epicenter['y'] = np.random.randint(4, h)
        _o = self.create_oval(x-4, y-4, x+4, y+4, fill='#F00')
        self.epicenter['obj'] = _o
        self.tag_raise(_o)  # tag_raise는 객체가 다른 객체 위로 오도록 만듬
        """
        캔버스 좌상단에 지진 발생 이후 경과시간을 표시하는 부분
        """
        rate = "{:.1f} sec".format(time.time()-self.t0)
        rate_txt = self.create_text(2, 2, text=rate, anchor='nw')
        # anchor='nw' 옵션은 문자의 기준점을 북(n)서(w)에 잡겠다는 뜻
        """
        관측소 배치 (사각형)
        """
        for det in self.detector:
            if det['N'] == 1:
                c = '#00F'
            elif det['N'] == 2:
                c = '#0FF'
            else:
                c = '#FF0'
            xd, yd = det['x'], det['y']
            _ = self.create_rectangle(xd-4, yd-4, xd+4, yd+4)
            self.itemconfig(_, fill=c)
            det['obj'] = _
        """
        지진파가 전파하는 것을 표현
        """
        _o = self.create_oval(x, y, x, y, fill='#FAA')
        self.tag_lower(_o)
        while self.is_run:
            rate = time.time()-t0  # 경과시간을 실시간 업데이트
            _r = self.wave_v*rate
            self.coords(_o, x-_r, y-_r, x+_r, y+_r)  # 지진파, 시간에 따라 확장
            for d in self.detector:
                if _r**2 >= (d['x']-x)**2+(d['y']-y)**2 and d['t'] is None:
                    """
                    만약 관측소가 지진파의 범위 안에 들어온다면
                    """
                    d['t'] = rate
                    stxt = "D{}: {:.2f} sec".format(d['N'], rate)
                    self.create_text(d['x'], d['y']-12, text=stxt)
                    # 기록된 시간을 관측소 위에 표시
                    Detector_on(d)
                    # 전역함수 ->(L96)
            self.itemconfig(rate_txt, text="{:.1f} sec".format(rate))
            # 좌상단의 경과시간 업데이트
            self.update()  # 캔버스 업데이트


def Detector_on(det):
    """
    관측소에서 지진을 관측했을때 작동하는 전역함수
    2번 프레임(메뉴)에 버튼을 생성해서 [d_btns]에 담는다.
    """
    global frame2, lab, d_btns
    name = "Detector {}".format(det['N'])
    btn = tk.Button(frame2, text=name, relief='groove', bg='#000', fg='#FFF')
    btn.config(font=12, command=lambda *a: Detector_calc(det), width=10)
    # lambda는 약식함수, 함수형 프로그래밍을 할 때 이용
    # 이 경우에는 생성과 동시에 자동으로 클랙액션 실행을 방지하기 위함
    btn.pack(side='top')
    d_btns.append(btn)


def Detector_calc(det):
    """
    관측소의 관측시간을 토대로 예측 범위를 그린다.
    """
    global lab
    r = det['t']*lab.wave_v
    if det['N'] == 1:
        c = '#00F'
    elif det['N'] == 2:
        c = '#0FF'
    else:
        c = '#FF0'
    _ = lab.create_oval(det['x']-r, det['y']-r, det['x']+r, det['y']+r)
    lab.itemconfig(_, outline=c, width=3)


def Canvas_Clear():
    """
    지진 시뮬레이터를 초기화시킨다.
    """
    global lab, d_btns
    lab.is_run = False
    for det in lab.detector:
        det['t'] = None
    for btn in d_btns:
        btn.destroy()
    lab.delete('all')

d_btns = []  # 메뉴의 관측소 버튼을 담아두는 리스트

master = tk.Tk()
master.title('Earthquake')
# 프레임 생성 1: 캔버스, 2: 메뉴
frame1 = tk.Frame(master, width=400, height=400, bg='#000')
frame2 = tk.Frame(master, width=100, height=400, bg='#000')
frame1.pack(side='left')
frame2.pack(side='top')
# geometry 클래스 생성. 캔버스와 동일한 사용.
# 클래스의 __init__에 pack()을 포함하고 있으므로 pack은 불필요 ->(L22)
lab = geometry(frame1, width=400, height=400, bg='#FFF')
# 기본 버튼 (Run, Clear) 생성
btn = tk.Button(frame2, text='Run', relief='groove', bg='#000', fg='#FFF')
btn.config(font=12, command=lab.earthquake_run, width=10)
btn.pack(side='top')
btn = tk.Button(frame2, text='Clear', relief='groove', bg='#000', fg='#FFF')
btn.config(font=12, command=Canvas_Clear, width=10)
btn.pack(side='top')

master.mainloop()
