# -*- coding: utf-8 -*-
"""
Created on Wed May 23 21:22:38 2018

@author: soma
"""
import tkinter as tk
import math
import random
import threading

class geo:
    delay = 0.025
    speed = 2

    def __init__(self, width=300, height=300):
        self.root = tk.Tk()
        self.root.title("지진 관측소 문제")

        self._setup_opt = {}
        self._setup_opt['width'] = width
        self._setup_opt['height'] = height
        self._setup_opt['background'] = "#FFF"

        self._calc_args()

        self.canvas = tk.Canvas(self.root, **self._setup_opt)
        self.canvas.pack()

        self.marker = None

    def signal_time(key):
        return self.observes[key].arrival_time()

    def observer_x(key):
        return self.observes[key].x

    def observer_y(key):
        return self.observes[key].y

    def mark(self, x, y):
        self.marker = _marker(self, x, y)

    def _calc_args(self):
        w = self._setup_opt['width']
        h = self._setup_opt['height']

        self.wave = _wave(self)
        self.observes = {}
        self.observes["A"] = _observe(self, self.wave, "A", w/2, h/3)
        self.observes["B"] = _observe(self, self.wave, "B", w/3, h*2/3)
        self.observes["C"] = _observe(self, self.wave, "C", w*2/3, h*2/3)

    def draw(self):
        self.wave.draw()
        self.observes["A"].draw()
        self.observes["B"].draw()
        self.observes["C"].draw()
        if not self.marker is None:
            self.marker.draw()
            self.marker.result(self.wave)

    def run(self):
        self.draw()
        self.root.mainloop()


class _marker:
    def __init__(self, root, x, y):
        self.root = root
        self.x = x
        self.y = y

    def draw(self):
        c = self.root.canvas
        c.create_oval(
            _get_coords(self.x, self.y, 5),
            fill="red", width=0)

    def result(self, wave):
        c = self.root.canvas
        dx = self.x - wave.x
        dy = self.y - wave.y
        r = math.sqrt(dx**2 + dy**2)
        if r <= 20:
            c.create_text(self.x, self.y - 15, text="성공", fill="red")
        else:
            c.create_text(self.x, self.y - 15, text="실패", fill="red")


class _observe:
    def __init__(self, root, wave, name, x, y):
        self.name = name
        self.root = root
        self.wave = wave
        self.x = x
        self.y = y

    def arrival_time(self):
        dx = self.x - self.wave.x
        dy = self.y - self.wave.y
        r = math.sqrt(dx**2 + dy**2)
        v = self.root.speed / self.root.delay
        return r / v

    def result(self):
        c = self.root.canvas
        c.create_text(self.x, self.y - 30,
                      text="관측소 "+self.name)
        c.create_text(self.x, self.y - 15,
                      text="시간: {:.2f}초 ".format(self.arrival_time()))

    def draw(self):
        c = self.root.canvas
        c.create_rectangle(*_get_coords(self.x, self.y, 5))
        threading.Timer(self.arrival_time(), self.result).start()


class _wave:
    target_r = 20

    def __init__(self, root):
        self.root = root

        w = root._setup_opt['width']
        h = root._setup_opt['height']
        self.x = w/4 + random.random() *w/2
        self.y = h/4 + random.random()*h/2

        self.len = 1

    def draw(self):
        c = self.root.canvas
        c.create_oval(
            _get_coords(self.x, self.y, 20),
            fill="#AAD", width=0)
        self.wave = c.create_oval(_get_coords(self.x, self.y, 1))
        self.run()

    def run(self):
        c = self.root.canvas
        w = self.root._setup_opt['width']
        h = self.root._setup_opt['height']
        delay = self.root.delay
        self.len += self.root.speed
        c.coords(self.wave, _get_coords(self.x, self.y, self.len))
        if self.len < min([w*2/3, h*2/3]):
            threading.Timer(delay, self.run).start()


def _get_coords(cx, cy, r):
    x1, x2 = cx - r, cx + r
    y1, y2 = cy - r, cy + r
    return x1, y1, x2, y2


if __name__ == "__main__":
    app = geo()
    app.mark(150, 150)
    app.run()
