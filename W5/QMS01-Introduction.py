# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:35:28 2016
@author: soma0sd
"""
import tkinter as tk
import numpy as np
import time


class QMS(tk.Canvas):
    """
    평면에서 이중극으로 변환해서 시뮬레이션 하는 프로그램
    """
    def __init__(self, *arg, **kw):
        tk.Canvas.__init__(self, *arg, **kw)
        self.vx = 180  # 가로방향 속도
        self.pack()
        self._create_rods()
        self.after(0, self.animations)  # 에니메이션 작동
        self.rod_voltage = False  # 전극 작동 스위치
        self.ions = []  # 이온 리스트

    def _create_rods(self):
        """
        캔버스 초기화, 실험실 Draw
        """
        w, h = self.winfo_reqwidth(), self.winfo_reqheight()
        N = self.create_rectangle(0, 0, w, 30, fill='#000')
        S = self.create_rectangle(0, h, w, h-30, fill='#000')
        self.rods = {'N': N, 'S': S, 'V': 0}

    def rod_on(self):
        """
        전극 스위치 True는 False로 False는 True로
        """
        self.rod_voltage = not self.rod_voltage
        if not self.rod_voltage:  # 만약 스위치가 꺼져있다면
            self.rods['V'] = 0

    def create_ion(self):
        """
        이온생성
        """
        h = self.winfo_reqheight()/2+2
        ind = self.create_oval(0, h-5, 10, h+5, fill='#F00')
        chg = np.random.randint(1, 4)
        tid = self.create_text(5, h, text=str(chg), fill='#FFF', font=('', 8))
        self.ions.append({'Oid': ind, 'Tid': tid, 'chg': chg, 'vy': 0, 'm': 1})

    def move_ion(self, ion, rate):
        """
        이온 이동 함수
        """
        w, h = self.winfo_reqwidth(), self.winfo_reqheight()
        pos = self.coords(ion['Tid'])
        Fn = 8.99E9*1.602E-7*self.rods['V']*ion['chg']/(pos[1]-30)**2
        Fs = 8.99E9*1.602E-7*self.rods['V']*ion['chg']/(pos[1]-h-30)**2
        ion['vy'] += (Fn-Fs)*rate/ion['m']
        self.move(ion['Oid'], self.vx*rate, ion['vy']*rate)
        self.move(ion['Tid'], self.vx*rate, ion['vy']*rate)
        if pos[0] > w or not 30 < pos[1] < h-30:
            self.delete(ion['Oid'])
            self.delete(ion['Tid'])
            ind = self.ions.index(ion)
            del self.ions[ind]

    def attachs(self, f, v):
        """
        외부 슬라이드바와 실시간 연결
        """
        self.Freq = f
        self.Volt = v

    def animations(self):
        """
        에니메이션
        """
        t0 = time.time()
        while True:
            td = time.time()-t0
            if self.rod_voltage:
                fr = self.Freq.get()
                vo = self.Volt.get()
                w = fr/(2*np.pi)
                if np.cos(w*t0) >= 0:
                    cp = "#{:X}00".format(int(15*np.cos(w*t0)))
                    cn = "#00{:X}".format(int(15*np.cos(w*t0)))
                    self.rods['V'] = vo*np.cos(w*t0)
                    self.itemconfig(self.rods['N'], fill=cp)
                    self.itemconfig(self.rods['S'], fill=cn)
                else:
                    cp = "#00{:X}".format(int(-15*np.cos(w*t0)))
                    cn = "#{:X}00".format(int(-15*np.cos(w*t0)))
                    self.rods['V'] = vo*np.cos(w*t0)
                    self.itemconfig(self.rods['N'], fill=cp)
                    self.itemconfig(self.rods['S'], fill=cn)
            if len(self.ions) > 0:
                for ion in self.ions:
                    self.move_ion(ion, td)
            self.update()
            t0 += td


master = tk.Tk()
"""
레이아웃 생성
"""
frame1 = tk.Frame(master, bg='#000')
frame2 = tk.Frame(master, bg='#000')
frame1.pack(side='left')
frame2.pack()
"""
클래스 호출
"""
lab = QMS(frame1, width=500, height=150)
"""
라벨 생성 (그리드 사용)
"""
_ = tk.Label(frame2, text='Freq')
_.config(bg='#000', fg='#FFF')
_.grid(row=0, column=0)
_ = tk.Label(frame2, text='Volt')
_.config(bg='#000', fg='#FFF')
_.grid(row=0, column=1)
"""
슬라이드바 생성
"""
f = tk.Scale(frame2, from_=0, to=100)
f.config(relief='groove', bg='#000', fg='#FFF')
f.grid(row=1, column=0)
v = tk.Scale(frame2, from_=0, to=100)
v.config(relief='groove', bg='#000', fg='#FFF')
v.grid(row=1, column=1)
lab.attachs(f, v)  # 클래스와 연결
"""
버튼 생성
"""
_ = tk.Button(frame2, text='voltage', command=lab.rod_on)
_.config(relief='groove', bg='#000', fg='#FFF')
_.grid(row=2, column=0, columnspan=2, sticky='we')
_ = tk.Button(frame2, text='ion', command=lab.create_ion)
_.config(relief='groove', bg='#000', fg='#FFF')
_.grid(row=3, column=0, columnspan=2, sticky='we')

master.mainloop()
