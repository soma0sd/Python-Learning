# -*- coding: utf-8 -*-
"""
Created on 2016-09-08

@ Author: soma0sd
@ Disc: pi값을 찾아서 콘솔에 출력
@ License: MIT
"""
from numpy import random
from numpy import sqrt

lim = 10000
gap = 1000

i = 1
dot_in = 0
while i <= lim:
    x, y = (random.random(), random.random())
    if sqrt(x**2+y**2) <= 1:
        dot_in += 1
    if i % gap == 0:
        print("{:10,}th pi: {:.4f}".format(i, 4 * dot_in / i))
    i += 1
