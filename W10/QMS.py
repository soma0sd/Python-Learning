# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 14:23:19 2016
@author: soma0sd
"""
import tkinter as tk

"""
보조 클래스 import
동일 폴더에 아래의 서브모듈을 함께 넣어둘 것
"""
from QMS01_ColorMap import cmap as qcmap
from QMS02_View import view as qview

"""
기본변수 설정
  mass_min: 입자 질량 최소치 [u]
  mass_max: 입자 질량 최대치 [u]
  ion_E: 이온의 운동에너지 [eV]
  rod_r: QMS의 반지름 [m]
  rod_w: QMS의 이온 진행방향 길이 [m]
  view_w: 캔버스 가로길이 [px]
  view_h: 캔버스 세로길이 [px]
"""
mass_min = 20
mass_max = 40
ion_E = 0
rod_r = 0
rod_w = 0
view_w = 300
view_h = 100
menu_w = 100

"""
상수 목록
"""
q =  1.602176565E-19  # 기본전하량 [C]
me = 1.660538782E-27  # 원자질량 [kg]
k =  8.987551787E9    # 클롱 힘 상수 [N m^2 / C^2]
ev = 1.60217646E-19   # 전자볼트 [J]


"""
환경변수 설정 ('_'로 시작하는 변수는 보조변수)
  color_map: 색상맵
  mass_range: 질량 스펙트럼
"""
_color_point = [[0, (0, 0, 0)], [0.5, (255, 0, 0)], [1,(255, 150, 150)]]
mass_range = range(mass_min, mass_max)
color_map = qcmap(_color_point, mass_range)
print(type(color_map))


"""
GUI 구동
"""
root = tk.Tk()
root.title('QSM Simulation')

view = qview(root, width=view_w, height=view_h, bg='#FFF')
view.grid(row=0, column=0, sticky='news')

frame_menu = tk.Frame(root, bg='#000', width=menu_w)
frame_menu.grid(row=0, column=1, sticky='ns')

root.mainloop()

