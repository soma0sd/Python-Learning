# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 13:21:37 2016
@author: soma0sd
"""
import tkinter as tk
import numpy as np
import time


class QMS:
    def __init__(self):
        self.power = False
        self.Vx = 180
        self.voltage = [0, 0]
        self.particle = []
        self.master = tk.Tk()
        self.master.title('QMS')
        self.create_frame()
        self.master.mainloop()

    def create_frame(self):
        self.canvas = tk.Canvas(self.master, width=400, height=300)
        self.canvas.pack(side='left')
        self.canvas.create_line(0, 100, 400, 100)
        self.canvas.create_line(0, 200, 400, 200)
        _ = self.canvas.create_text(2, 2, text='Low Mass Filter', anchor='nw')
        self.canvas.itemconfig(_, fill='#F00')
        _ = self.canvas.create_text(2, 102, text='High Mass Filter')
        self.canvas.itemconfig(_, fill='#00F', anchor='nw')
        self.frame_menu = tk.Frame(self.master, width=100, bg='#000')
        self.frame_menu.pack(side='top')
        self.create_menu()
        self.setup_canvas()

    def create_menu(self):
        self.menu_btn = {}
        self.menu_btn['power'] = tk.Button(self.frame_menu, text='Power ON')
        self.menu_btn['power'].config(relief='groove', bg='#000', fg='#FFF')
        self.menu_btn['power'].config(command=self._cmd_power)
        self.menu_btn['power'].grid(row=0, column=0, columnspan=2, sticky='we')
        self.menu_btn['particle'] = tk.Button(self.frame_menu, text='Samples')
        self.menu_btn['particle'].config(relief='groove', bg='#000', fg='#FFF')
        self.menu_btn['particle'].config(command=self._cmd_particle)
        self.menu_btn['particle'].grid(row=1, columnspan=2, sticky='we')
        self.menu_btn['reset'] = tk.Button(self.frame_menu, text='reset')
        self.menu_btn['reset'].config(relief='groove', bg='#000', fg='#FFF')
        self.menu_btn['reset'].config(command=self._cmd_reset)
        self.menu_btn['reset'].grid(row=2, column=0, columnspan=2, sticky='we')
        _ = tk.Label(self.frame_menu, text='', bg='#000', fg='#FFF')
        _.grid(row=3, column=0, columnspan=2, sticky='we')
        _ = tk.Label(self.frame_menu, text='Program', bg='#000', fg='#FFF')
        _.grid(row=4, column=0, columnspan=2, sticky='we')
        self.menu_btn['DCV'] = tk.StringVar()
        self.menu_btn['ACV'] = tk.StringVar()
        self.menu_btn['Freq'] = tk.StringVar()
        self.menu_btn['DCV'].set(10)
        self.menu_btn['ACV'].set(10)
        self.menu_btn['Freq'].set(3)
        _ = tk.Label(self.frame_menu, text='DCV', bg='#000', fg='#FFF')
        _.grid(row=5, column=0, sticky='we')
        _ = tk.Entry(self.frame_menu, width=3)
        _.config(textvariable=self.menu_btn['DCV'])
        _.grid(row=5, column=1)
        _ = tk.Label(self.frame_menu, text='ACV', bg='#000', fg='#FFF')
        _.grid(row=6, column=0, sticky='we')
        _ = tk.Entry(self.frame_menu, width=3)
        _.config(textvariable=self.menu_btn['ACV'])
        _.grid(row=6, column=1)
        _ = tk.Label(self.frame_menu, text='Freq', bg='#000', fg='#FFF')
        _.grid(row=7, column=0, sticky='we')
        _ = tk.Entry(self.frame_menu, width=3)
        _.config(textvariable=self.menu_btn['Freq'])
        _.grid(row=7, column=1)

    def setup_canvas(self):
        self.rod = {}
        self.rod['HN'] = self.canvas.create_rectangle(10, 20, 390, 30)
        self.rod['HS'] = self.canvas.create_rectangle(10, 70, 390, 80)
        self.rod['LN'] = self.canvas.create_rectangle(10, 120, 390, 130)
        self.rod['LS'] = self.canvas.create_rectangle(10, 170, 390, 180)
        self.hist = []
        for i in range(1, 20):
            x = 380*i/20
            data = {}
            _ = self.canvas.create_rectangle(x-8, 280, x+8, 280, fill='#000')
            data['id'] = _
            data['value'] = 0
            self.hist.append(data)
            self.canvas.create_text(x, 280, text=i, anchor='n')
        self.canvas.after(0, self.animation)

    def _cmd_particle(self):
        data = {}
        x = np.random.randint(-3, 3)
        y = np.random.randint(-3, 3)
        m = np.random.randint(1, 20)
        _ = self.canvas.create_oval(0, 47-x, 8, 55-x, fill='#F00')
        data['Hid'] = _
        _ = self.canvas.create_oval(0, 147-y, 8, 155-y, fill='#F00')
        data['Lid'] = _
        data['Vy'] = 0
        data['Vz'] = 0
        data['mass'] = m
        self.particle.append(data)

    def _cmd_power(self):
        self.power = not self.power
        if self.power:
            self.menu_btn['power'].config(text='Power OFF')
        else:
            self.menu_btn['power'].config(text='Power ON')
            self.voltage = [0, 0]

    def _cmd_reset(self):
        for h in self.hist:
            self.canvas.delete(h['id'])
        self.hist = []
        for i in range(1, 20):
            x = 380*i/20
            data = {}
            _ = self.canvas.create_rectangle(x-8, 280, x+8, 280, fill='#000')
            data['id'] = _
            data['value'] = 0
            self.hist.append(data)
            self.canvas.create_text(x, 280, text=i, anchor='n')

    def animation(self):
        t0 = time.time()
        while True:
            try:
                w = float(self.menu_btn['Freq'].get())/(2*np.pi)
                ac = float(self.menu_btn['ACV'].get())
                dc = float(self.menu_btn['DCV'].get())
            except:
                pass
            if self.power:
                self.voltage[0] = dc+ac*np.cos(w*t0)
                self.voltage[1] = -dc-ac*np.cos(w*t0+np.pi)
            rate = time.time()-t0
            for p in self.particle:
                codH = self.canvas.coords(p['Hid'])
                codL = self.canvas.coords(p['Lid'])
                y = codH[0]+2
                z = codL[0]+2
                Ay = self.voltage[0]*10*((1/(y-30)**2)+(1/(y-70)**2))/p['mass']
                Az = self.voltage[1]*10*((1/(z-130)**2)+(1/(z-170)**2))/p['mass']
                p['Vy'] += Ay*rate
                p['Vz'] += Az*rate
                self.canvas.move(p['Hid'], self.Vx*rate, p['Vy']*rate)
                self.canvas.move(p['Lid'], self.Vx*rate, p['Vz']*rate)
                if codH[0] > 400:
                    self.canvas.delete(p['Hid'])
                    self.canvas.delete(p['Lid'])
                    self.hist_handle(p['mass'])
                    self.particle.remove(p)
                elif codH[1] < 30 or codH[1] > 70:
                    self.canvas.delete(p['Hid'])
                    self.canvas.delete(p['Lid'])
                    self.particle.remove(p)
                elif codL[1] < 130 or codL[1] > 170:
                    self.canvas.delete(p['Hid'])
                    self.canvas.delete(p['Lid'])
                    self.particle.remove(p)
            t0 = time.time()
            self.canvas.update()

    def hist_handle(self, m):
        self.hist[m-1]['value'] += 1
        lim = max([i['value'] for i in self.hist])
        v = 70/lim
        for h in self.hist:
            cod = self.canvas.coords(h['id'])
            y = h['value'] * v
            self.canvas.coords(h['id'], cod[0], cod[3]-y, cod[2], cod[3])


QMS()
