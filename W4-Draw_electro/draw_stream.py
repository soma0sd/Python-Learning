# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 18:03:10 2016
@author: soma0sd
"""
import tkinter as tk
import numpy as np


class SingleCharge:
    """
    전하 오브젝트 클래스
    """
    def __init__(self, canvas, x, y, charge, **kw):
        """
        초기화와 함께 타원과 텍스트를 그린다
        """
        self.opt = {'r': 15}  # 키워드 옵션
        self.opt.update(kw)  # 키워드 옵션 업데이트
        self.canvas = canvas  # 상속받을 캔버스
        self.x = x  # x 좌표
        self.y = y  # y 좌표
        self.charge = charge  # 전하량
        # Draw Charge
        r = self.opt['r']
        if charge > 0:
            c = '#F00'
        if charge < 0:
            c = '#00F'
        self.oval = canvas.create_oval(x-r, y-r, x+r, y+r, fill=c)
        self.text = canvas.create_text(x, y, text=str(charge), fill='#FFF')

    def is_crush(self, x, y):
        """
        충돌판정, 전기력선과 마우스 클릭 액션에 사용
        """
        ix = x - self.x
        iy = y - self.y
        if self.opt['r']**2 > ix**2+iy**2:
            return True
        else:
            return False

    def clone(self, **kw):
        """
        복제, 랜덤한 위치에 동일한 종류의 전하를 그린다.
        x=00, y=00 키워드를 이용해서 직접 지정도 가능
        """
        option = {'x': np.random.randint(30, 470),
                  'y': np.random.randint(80, 470)}
        option.update(kw)
        return SingleCharge(self.canvas, option['x'],  option['y'],
                            self.charge)

    def move(self, x, y):
        """
        이동, 자신을 움직이는 함수.
        텍스트와 타원을 함꼐 움직이고, 자신의 위치를 재정의한다.
        """
        self.x = x
        self.y = y
        r = self.opt['r']
        self.canvas.coords(self.oval, x-r, y-r, x+r, y+r)
        self.canvas.coords(self.text, x, y)

    def delete(self):
        """
        삭제, 캔버스로부터 타원과 텐스트를 삭제한다
        """
        self.canvas.delete(self.oval)
        self.canvas.delete(self.text)


class control:
    """
    캔버스 제어 클래스
    """
    def __init__(self, canvas, **kw):
        """
        초기화하면서 전하선택메뉴를 그린다.
        그리기가 완료되면 클릭, 드래그, 애니메이션을 바인드.
        """
        self.opt = {'w': 600, 'h': 50, 'maxima': 5}
        self.opt.update(kw)  # 키워드 옵션을 업데이트
        self.canvas = canvas  # 캔버스
        self.btn = []  # 전하 선택 버튼
        self.object = []  # 생성한 전하
        self._flag = None  # 전하 선택자
        # Menu Draw
        maxi = self.opt['maxima']
        width = self.opt['w']
        cy = self.opt['h']/2
        for i in range(maxi*2+1):
            if i == maxi:
                continue
            bt = SingleCharge(canvas, (i+1)*width/(maxi*2+2), cy, i-maxi)
            self.btn.append(bt)
        canvas.bind('<Button-1>', self.B1Action)
        canvas.bind('<B1-Motion>', self.B1Motion)
        canvas.after(0, self.animation)

    def B1Action(self, event):
        """
        클릭액션.
        메뉴를 클릭하면 전하생성, 생성 전하를 선택하면 이동 가능 플래그.
        """
        # Find active button
        self._flag = None
        for b in self.btn:  # 메뉴 루프
            if b.is_crush(event.x, event.y):
                self.object.append(b.clone())
        for o in self.object:  # 생성전하 루프
            if o.is_crush(event.x, event.y):
                self._flag = o

    def B1Motion(self, event):
        """
        드래그액션.
        클릭한 상태에서 움직일 때 플래그로 전달된 전하를 움직임.
        메뉴바 높이까지 끌어올리면 삭제
        """
        if self._flag is None:
            return None
        self._flag.move(event.x, event.y)
        if event.y < 50:
            self.delete_object(self._flag)

    def delete_object(self, obj):
        """
        전하 삭제. 드래그-이동에서 조건을 만족시키면 작동.
        캔버스에서 전하를 삭제하고, 내부 전하목록에서도 삭제
        """
        obj.delete()
        del self.object[self.object.index(obj)]
        return None  # 리턴을 줘서 반복실행으로 인한 오류를 막는다.

    def animation(self):
        """
        에니메이션.
        무한루프를 안에서 전기력선을 통제한다.
        """
        dr = 3  # 전기력선 간격, 좌표가 아니라 선의 길이로 판정
        lines = []
        while True:
            for li in lines:  # 기존 전기력선을 삭제하는 루프
                self.canvas.delete(li)
            lines = []
            for o in self.object:  # 전기력선을 생성하는 루프
                chg = o.charge
                N = np.abs(chg*4)  # 전하당 4개의 선을 그린다
                for li in range(N):
                    theta = np.pi*2*li/N
                    ix = o.x+o.opt['r']*np.cos(theta)
                    iy = o.y+o.opt['r']*np.sin(theta)
                    lines.append(self._draw_stream(ix, iy, dr, theta, o))
            self.canvas.update()

    def _draw_stream(self, ix, iy, r, theta, obj):
        """
        하나의 전기력선을 그리는 숨은 함수.
        """
        x, y = ix+r*np.cos(theta), iy+r*np.sin(theta)
        crd = [ix, iy, x, y]
        i = 0
        # 캔버스를 넘어가거나 전하를 만나면 그리기 종료
        while 0 < x < 600 and 50 < y < 600 and self._is_line_crush(x, y):
            r = np.sqrt((crd[-2]-crd[-4])**2+(crd[-1]-crd[-3])**2)
            theta = np.arctan2(crd[-1]-crd[-3], crd[-2]-crd[-4])
            Er, Et = self._CalcE(x, y, obj)
            nx = r*np.cos(theta)+Er*np.cos(Et)
            ny = r*np.sin(theta)+Er*np.sin(Et)
            theta = np.arctan2(ny, nx)
            x = x+r*np.cos(theta)
            y = y+r*np.sin(theta)
            crd += [x, y]
            i += 1
        if obj.charge > 0:  # 전기력선 색상 결정
            c = '#FAA'
        else:
            c = '#AAF'
        return self.canvas.create_line(crd, fill=c)

    def _CalcE(self, x, y, obj):
        """
        해당 지점의 전기장 계산,
        극좌표계 r, t를 출력
        """
        Ex, Ey = 0, 0
        ratio = 5E3
        for o in self.object:
            if obj.charge > 0:
                k = -1
            else:
                k = 1
            Er = k*ratio*o.charge/((o.x-x)**2+(o.y-y)**2)
            Et = np.arctan2(o.y-y, o.x-x)
            Ex += Er*np.cos(Et)
            Ey += Er*np.sin(Et)
        Er = np.sqrt(Ex**2+Ey**2)
        Et = np.arctan2(Ey, Ex)
        return Er, Et

    def _is_line_crush(self, x, y):
        """
        전기력선이 다른 전하와 충돌하는지 확인하는 함수
        """
        for o in self.object:
            if o.is_crush(x, y):
                return False
        return True


master = tk.Tk()
canvas = tk.Canvas(master, width=600, height=600, bg='#000')
canvas.pack()
control(canvas)  # 컨트롤 클래스
master.mainloop()
