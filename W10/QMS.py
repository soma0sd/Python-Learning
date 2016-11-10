# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 14:23:19 2016
@author: soma0sd
"""
import tkinter as tk
import numpy as np

"""
보조 클래스 import
동일 폴더에 아래의 서브모듈을 함께 넣어둘 것
"""
from QMS01_ColorMap import cmap as qcmap
from QMS02_View import view as qview

"""
초기변수 설정
  dt: 시간간격 [second]
  mass_min: 입자 질량 최소치 [u]
  mass_max: 입자 질량 최대치 [u]
  ion_E: 이온의 운동에너지 [eV]
  rod_r: QMS의 반지름 [m]
  rod_w: QMS의 이온 진행방향 길이 [m]
  rod_fr: QMS의 AC전원 진동수 [kHz]
  rod_ac: time=0에서의 AC 전원 [V]
  rod_dc: DC 전원 [V]
"""
dt = 1E-8
mass_min = 20
mass_max = 40
ion_E = 2
rod_r = 0.05
rod_w = 0.1
rod_fr = 3
rod_ac = 1
rod_dc = 1

"""
GUI 변수 설정
  view_w: 캔버스 가로길이 [px]
  view_h: 캔버스 세로길이 [px]
  menu_w: 메뉴 너비 [px]
"""
view_w = 400
view_h = 150
menu_w = 100

"""
상수 목록
"""
q =  1.602176565E-19  # 기본전하량 [C]
cm = 1.660538782E-27  # 원자질량 [kg]
k =  8.987551787E9    # 클롱 힘 상수 [N m^2 / C^2]
ev = 1.60217646E-19   # 전자볼트 [J]


"""
환경변수 설정 ('_'로 시작하는 변수는 보조변수)
  color_map: 색상맵
  mass_range: 질량 스펙트럼
"""
_color_point = [[0, (0, 0, 0)], [0.5, (0, 0, 255)], [1,(255, 150, 150)]]
mass_range = range(mass_min, mass_max)
color_map = qcmap(_color_point, mass_range)


"""
계산 변수
  z2px: 매트릭 가로좌표를 픽셀 x좌표로 변환
  xy2px: 매트릭 세로좌표를 픽셀 y좌표로 변환

계산 함수
  line_make: 하나의 질량을 입력받아 경로를 출력한다
"""
z2px = view_w/rod_w
xy2px = view_h/rod_r

def line_make(mass):
  global q, cm, ev, z2px, xy2px
  global dt, ion_E, rod_r, rod_w, view_w, view_h, color_map
  dz = np.sqrt(2*ev*ion_E/(mass*cm))*dt
  x, y, z = 0, 0, 0
  ax, ay, az= [x], [y], [z]
  debug = 0  # 포인트 디버깅: dt 조정용
  while -view_h/2 < x < view_h/2 and -view_h/2 < y < view_h/2 and z < view_w:
    z += z2px*dz
    x += z2px*dz/mass
    ax += [x]
    ay += [y]
    az += [z]
    debug += 1
  print(debug)
  return ax, ay, az, color_map.get_colorcode(mass)


"""
GUI 구동
"""
root = tk.Tk()
root.title('QSM Simulation')

view = qview(root, width=view_w, height=view_h, bg='#FFF')
view.grid(row=0, column=0, sticky='news')

cx, cy, cz, ac = [], [], [], []
for m in mass_range:
  x, y, z, c = line_make(m)
  cx.append(x)
  cy.append(y)
  cz.append(z)
  ac.append(c)
view.set_lines(cx, cy, cz, ac)

frame_menu = tk.Frame(root, bg='#000', width=menu_w)
frame_menu.grid(row=0, column=1, sticky='ns')

root.mainloop()

