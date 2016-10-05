# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 14:45:39 2016

@author: soma0sd
"""
import tkinter as tk
import numpy as np
import time


class geometry(tk.Canvas):
    wave_v = 50  # px per seconds

    def __init__(self, *arg, **kw):
        tk.Canvas.__init__(self, *arg, **kw)
        self.t0 = 0
        self.pack()
        xd, yd = (self.winfo_reqwidth()-4)/3, (self.winfo_reqheight()-4)/3
        self.epicenter = {'x': 0, 'y': 0, 'obj': 0}  # 진앙데이터
        # 관측소
        detector1 = {'N': 1, 'x': xd*1.5, 'y': yd, 'obj': 0, 't': None}
        detector2 = {'N': 2, 'x': xd, 'y': yd*2, 'obj': 0, 't': None}
        detector3 = {'N': 3, 'x': xd*2, 'y': yd*2, 'obj': 0, 't': None}
        self.detector = [detector1, detector2, detector3]

    def earthquake_run(self):
        t0 = time.time()
        w, h = self.winfo_reqwidth()-4, self.winfo_reqheight()-4
        x = self.epicenter['x'] = np.random.randint(4, w)
        y = self.epicenter['y'] = np.random.randint(4, h)
        _o = self.create_oval(x-4, y-4, x+4, y+4, fill='#F00')
        self.epicenter['obj'] = _o
        self.tag_raise(_o)
        rate = "{:.1f} sec".format(time.time()-self.t0)
        rate_txt = self.create_text(2, 2, text=rate, anchor='nw')
        _o = self.create_oval(x, y, x, y, fill='#FAA')
        self.tag_lower(_o)
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
        while True:
            rate = time.time()-t0
            _r = self.wave_v*rate
            self.coords(_o, x-_r, y-_r, x+_r, y+_r)
            for d in self.detector:
                if _r**2 >= (d['x']-x)**2+(d['y']-y)**2 and d['t'] is None:
                    d['t'] = rate
                    stxt = "D{}: {:.2f} sec".format(d['N'], rate)
                    self.create_text(d['x'], d['y']-12, text=stxt)
                    Detector_on(d)
            self.itemconfig(rate_txt, text="{:.1f} sec".format(rate))
            self.update()


def Detector_on(det):
    global frame2, lab
    name = "Detector {}".format(det['N'])
    btn = tk.Button(frame2, text=name, relief='groove', bg='#000', fg='#FFF')
    btn.config(font=12, command=lambda *a: Detector_calc(det), width=10)
    btn.pack(side='top')


def Detector_calc(det):
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


master = tk.Tk()
master.title('Earthquake')
frame1 = tk.Frame(master, width=400, height=400, bg='#000')
frame2 = tk.Frame(master, width=100, height=400, bg='#000')
frame1.pack(side='left')
frame2.pack(side='top')
lab = geometry(frame1, width=400, height=400, bg='#FFF')
btn = tk.Button(frame2, text='Run', relief='groove', bg='#000', fg='#FFF')
btn.config(font=12, command=lab.earthquake_run, width=10)
btn.pack(side='top')
btn = tk.Button(frame2, text='Clear', relief='groove', bg='#000', fg='#FFF')
btn.config(font=12, command=lambda *a: lab.delete('all'), width=10)
btn.pack(side='top')
master.mainloop()
