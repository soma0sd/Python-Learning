# -*- coding: utf-8 -*-
"""
Created on 2016-09-08

@ Author: soma0sd
@ Disc: pi값을 찾아서 콘솔에 출력
@ License: MIT
"""
from numpy import random
import numpy as np
import matplotlib.pyplot as plt

lim = 10000
gap = 100

count, pix = ([], [])
x, y = ([], [])

i = 1
dot_in = 0
while i <= lim:
    px, py = (random.random(), random.random())
    x.append(px)
    y.append(py)
    if np.sqrt(px**2+py**2) <= 1:
        dot_in += 1
    if i % gap == 0:
        count.append(i)
        pix.append(4 * dot_in / i)
    i += 1

rx, ry = ([], [])
for theta in np.arange(0, np.pi/2, 0.1):
    rx.append(np.cos(theta))
    ry.append(np.sin(theta))

fig, (a1, a2) = plt.subplots(ncols=2)
a1.set_title('Ranbom dot positions', fontsize=14, fontweight='bold')
a2.set_title('Count vs PI', fontsize=14, fontweight='bold')
a1.plot(x, y, ".")
a1.plot(rx, ry, "-r", linewidth=2.0)
a1.set_xlabel("X position")
a1.set_ylabel("Y position")
a2.plot(count, pix)
a2.set_xlabel("count")
a2.set_ylabel("pi")
