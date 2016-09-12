# -*- coding: utf-8 -*-
"""
Created on 2016-09-09

@ Author: soma0sd
@ Disc: fitting한 그래프를 적분한다
@ License: MIT

"""
import matplotlib.pyplot as plt
import numpy as np


def get_data():
    """
    1880년부터 2016년까지 월별 평균 기온 정보를 받아온다.
    csv는 쉼표와 줄바꿈문자를 이용해서 데이터를 구분하는 형식이다.
    """
    import requests
    url = 'http://data.giss.nasa.gov/gistemp/tabledata_v3/GLB.Ts+dSST.csv'
    data = str(requests.get(url).content)
    data = data.split('\\n')
    # \n은 줄바꿈문자. 온라인에서 정보를 받아와서 각 줄별로 리스트를 생성한다
    data = [row.split(',') for row in data]
    # 각 줄마다 쉼표로 분리해서 2차원 리스트를 만든다
    return (data[2:])[:-2]  # 데이터가 아닌 부분은 슬라이싱


"""
연평균기온 데이터
"""
data = get_data()
years = [int(row[0]) for row in data]
tempr = [float(row[13]) for row in data]
"""
다항식 fitting - 1차
"""
fitsp = np.linspace(years[0], years[-1], 100)
fit1 = np.poly1d(np.polyfit(years, tempr, 1))
"""
다항식 fitting - 9차
"""
fit9 = np.poly1d(np.polyfit(years, tempr, 9))
"""
PLOT
"""
plt.plot(years, tempr,':g',
         fitsp, fit1(fitsp), "--r",
         fitsp, fit9(fitsp), "--k")
