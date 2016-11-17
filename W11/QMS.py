# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 21:48:58 2016
@author: soma0sd
QMS 메인 프로그램
이전 주차에는 효과적인 GUI를 위해 임시로 범위를 정했다.
이번 주는 실제 물리량을 활용한 시뮬레이션을 하도록 한다.
"""
import tkinter as tk
import numpy as np

"""
서브모듈 import
"""
from lib_ColorMap import cmap
from lib_View import qview

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
dt = 1E-7
mass_min = 60
mass_max = 80
ion_E = 2
rod_r = 0.05
rod_w = 0.1
rod_fr = 61
rod_ac = 50
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
q =  1.60217657E-19   # 기본전하량 [C]
cm = 1.66053878E-27   # 원자질량 [kg]
ev = 1.60217646E-19   # 전자볼트 [J]


"""
환경변수 설정 ('_'로 시작하는 변수는 보조변수)
  color_map: 색상맵
  mass_range: 질량 스펙트럼
"""
_color_point = [[0, (0, 0, 0)], [0.5, (0, 0, 255)], [1,(255, 150, 0)]]
mass_range = range(mass_min, mass_max+1)
color_map = cmap(_color_point, mass_range)

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
  global rod_ac, rod_dc, rod_fr, rod_r
  global dt, ion_E, view_w, view_h, color_map
  dz = np.sqrt(2*ev*ion_E/(mass*cm))*dt
  x, y = np.random.randn()*15, np.random.randn()*15
  x, y = 0.01, 0.01
  z, t = 0, 0
  px, py, pz= [x], [y], [z]
  debug = 0  # 포인트 디버깅: dt 조정용
  xy_max = view_h/(2*xy2px)
  z_max = view_w/(xy2px)
  vx, vy = 0, 0
  while -xy_max < x < xy_max and -xy_max < y < xy_max and z < z_max:
    t += dt
    v = rod_dc+rod_ac*np.cos(2*np.pi*rod_fr*1E3*t)
    vx += -2*q*v*x*dt/(mass*cm*rod_r**2)
    vy += 2*q*v*y*dt/(mass*cm*rod_r**2)
    z += dz
    x += vx*dt
    y += vy*dt
    px += [xy2px*x]
    py += [xy2px*y]
    pz += [z2px*z]
    debug += 1
  print(debug)
  return px, py, pz, color_map.get_colorcode(mass)

def plot():
  global dt, rod_ac, rod_dc, rod_fr
  global view
  cx, cy, cz, ac = [], [], [], []
  for m in mass_range:
    x, y, z, c = line_make(m)
    cx.append(x)
    cy.append(y)
    cz.append(z)
    ac.append(c)
  view.set_lines(cx, cy, cz, ac, mass_range)
  view.viewr.create_text(4, 20,
                         text="dt: {:.2E} sec".format(dt), anchor='nw')
  view.viewr.create_text(4, 32,
                         text="AC: {:} V".format(rod_ac),
                         anchor='nw')
  view.viewr.create_text(4, 44,
                         text="DC: {:.1f} V".format(rod_dc),
                         anchor='nw')
  view.viewr.create_text(4, 56,
                         text="fr: {:.1f} kHz".format(rod_fr),
                         anchor='nw')

def action(code, val):
  global plot, rod_ac, rod_dc, rod_fr
  if code is 'ac':
    rod_ac += val
  elif code is 'dc':
    rod_dc += val
  elif code is 'fr':
    rod_fr += val
  plot()


"""
GUI 구동
"""
root = tk.Tk()
root.title('QSM Simulation')

view = qview(root, width=view_w, height=view_h, bg='#FFF')
view.grid(row=0, column=0, sticky='news')

frame_menu = tk.Frame(root, bg='#000', width=menu_w)
frame_menu.grid(row=0, column=1, sticky='ns')

plot()

l_ac = tk.Label(frame_menu, text='AC Volt', bg='#000', fg='#FFF')
l_ac.grid(row=0, column=0, rowspan=2, sticky='news')
b_ac_u = tk.Button(frame_menu, text='up', bg='#000', fg='#FFF')
b_ac_u.config(command=lambda *x: action('ac', 10))
b_ac_u.grid(row=0, column=1, sticky='news')
b_ac_d = tk.Button(frame_menu, text='down', bg='#000', fg='#FFF')
b_ac_d.config(command=lambda *x: action('ac', -10))
b_ac_d.grid(row=1, column=1, sticky='news')

l_ac = tk.Label(frame_menu, text='DC Volt', bg='#000', fg='#FFF')
l_ac.grid(row=2, column=0, rowspan=2, sticky='news')
b_ac_u = tk.Button(frame_menu, text='up', bg='#000', fg='#FFF')
b_ac_u.config(command=lambda *x: action('dc', 0.1))
b_ac_u.grid(row=2, column=1, sticky='news')
b_ac_d = tk.Button(frame_menu, text='down', bg='#000', fg='#FFF')
b_ac_d.config(command=lambda *x: action('dc', -0.1))
b_ac_d.grid(row=3, column=1, sticky='news')

l_ac = tk.Label(frame_menu, text='Frequency', bg='#000', fg='#FFF')
l_ac.grid(row=4, column=0, rowspan=2, sticky='news')
b_ac_u = tk.Button(frame_menu, text='up', bg='#000', fg='#FFF')
b_ac_u.config(command=lambda *x: action('fr', 1))
b_ac_u.grid(row=4, column=1, sticky='news')
b_ac_d = tk.Button(frame_menu, text='down', bg='#000', fg='#FFF')
b_ac_d.config(command=lambda *x: action('fr', -1))
b_ac_d.grid(row=5, column=1, sticky='news')

root.mainloop()
