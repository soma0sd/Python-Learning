# -*- coding: utf-8 -*-
"""
Created on 2016-09-09

@ Author: soma0sd
@ Disc: 클래스를 사용하는 방법을 살펴본다.
@ 과제: 클래스의 모자란 부분을 채워서 벡터연산 클래스를 완성하라
@ License: MIT
"""


class vector:
    def __init__(self, x: float, y: float, z: float):
        self.coord = [x, y, z]

    def __add__(self, b):  # '+'
        a = self.coord
        self.coord = [a[0]+b.coord[0], a[0]+b.coord[0], a[0]+b.coord[0]]
        return self.coord

    def __sub__(self, b):  # '-'
        ...

    def cross(self, b):  # 외적
        ...

    def dot(self, b):  # 내적
        ...

    def __xor__(self, b):  # '^' 외적
        return self.cross(b)

    def __mul__(self, b):  # '*' 내적
        return self.dot(b)

    def __repr__(self):
        return self.coord.__repr__()


a = vector(1, 2, 3)
b = vector(3, 2, 4)
print("A={}, B={}".format(a, b))
print("A+B =", a+b)
print("A-B =", a-b)
print("A cross B =", a^b)
print("A dot B =", a*b)
