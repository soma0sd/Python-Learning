# -*- coding: utf-8 -*-
"""
Created on 2016-09-08

@ Author: soma0sd
@ Disc: 표준패키지 random과 numpy.random의 비교
@ License: MIT
"""
import time
import random as ran1
from numpy import random as ran2

count = 500000
rands1 = []
rands2 = []
t0 = time.time()

for i in range(count):
    rands1.append(ran1.random())  # 한개의 [0, 1]난수를 생성
t1 = time.time()

for i in range(count):
    rands2.append(ran2.random())  # 한개의 [0, 1]난수를 생성
t2 = time.time()

print("생성하는 난수: {:,}개".format(count))
print("표준 패키지: {:.4f} sec".format(t1-t0))
print(" numpy 모듈: {:.4f} sec".format(t2-t1))
