# -*- coding: utf-8 -*-
"""
Created on 2016-09-09

@ Author: soma0sd
@ Disc: 클래스를 사용하는 방법을 살펴본다.
@ 과제: 클래스의 모자란 부분을 채워서 벡터연산 클래스를 완성하라
@ License: MIT
"""


class vector:
    """
    클래스 선언, 패키지 처럼 사용할 수 있는 함수와 변수들의 세트를 만든다
    """
    def __init__(self, x: float, y: float, z: float):
        """
        처음 불러왔을 때 바로 설정해야 하는 변수가 있거나 실행해야 할 명령이
        있을 때 사용한다.
        """
        self.coord = [x, y, z]

    def __add__(self, b):
        """
        클래스는 변수형처럼 사용할 수 있다. __add__는 A + B나 A += B와 같은
        더하기 명령에서 클래스를 어떻게 처리할지를 정한다.
        """
        a = self.coord
        self.coord = [a[0]+b.coord[0], a[0]+b.coord[0], a[0]+b.coord[0]]
        return self.coord

    def __sub__(self, b):
        """
        __sub__는 A - B나 A -= B와 같은 빼기 명령에서
        클래스를 어떻게 처리할지를 정한다.
        """
        ...

    def cross(self, b):  # 외적 함수
        ...

    def dot(self, b):  # 내적 함수
        ...

    def __xor__(self, b):
        """
        __xor__은 A ^ B와 같은 연산자를 만날 경우에 클래스를
        어떻게 처리할지를 정한다. vecter 클래스에서는 외적을 실행한다.
        """
        return self.cross(b)

    def __mul__(self, b):
        """
        __mul__은 A * B와 같은 연산자를 만날 경우에 클래스를
        어떻게 처리할지를 정한다. vecter 클래스에서는 내적을 실행한다.
        """
        return self.dot(b)

    def __repr__(self):
        """
        __repr__은 클래스를 프린트 했을 때, 즉 print(A)와 같은 명령에서
        콘솔에 어떻게 표시할지를 정한다. str(문자열)만 받을 수 있다.
        이 함수에서는 다른 클래스(list)의 __repr__을 받아와 사용한다.
        """
        return self.coord.__repr__()


a = vector(1, 2, 3)
b = vector(3, 2, 4)
print("A={}, B={}".format(a, b))
print("A+B =", a+b)
print("A-B =", a-b)
print("A cross B =", a^b)
print("A dot B =", a*b)
