# -*- coding: utf-8 -*-
"""
Created on 2016-09-08

@ Author: soma0sd
@ Disc: ramdom 결과물을 matplotlib에서 plot
@ License: MIT
"""
from matplotlib import pyplot as plt  # plot 패키지
from numpy import random

count = 100
x = random.rand(count)
y = random.rand(count)

plt.plot(x, y, ".")  # 결과를 그래프로 출력
