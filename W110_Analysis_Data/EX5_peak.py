"""
.. image:: EX5_peak.png

`EX5_peak.py <EX5_>`_

.. _EX5: https://github.com/soma0sd/Python-Learning/blob/main/W110_Analysis_Data/EX5_peak.py

.. literalinclude:: EX5_peak.py
   :language: python
   :linenos:
   :lines: 14-

"""
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def append(*args):
    # 데이터를 합치는 함수
    data = np.array([])
    for arg in args:
        data = np.append(data, arg)
    return data

"""
Gaussian Fit: 중심점과 반치폭을 찾는다
"""
def gaussian(x, A, mu, sigma):
    return A*np.exp(-(x-mu)**2/(2*sigma**2))

# 데이터 생성
n = 80000; chn = 400
back  = randn(n)*50
peak1 = randn(int(n/50))*1.5+24
peak2 = randn(int(n/30))*3.5+60

if __name__ == "__main__":
    data = append(back, peak1, peak2)
    # 히스토그램 생성
    hist, ch = np.histogram(data, bins=chn, range=(0, 100))
    # bins: 채널 수, range: 범위
    ch = ch[1:]  # 채널 보정

    """
    예상되는 구간 설정
    """
    p1_ch, p1_hist = ch[20*4:30*4], hist[20*4:30*4]
    p2_ch, p2_hist = ch[50*4:70*4], hist[50*4:70*4]

    plt.figure(figsize=(10, 9))
    ax = plt.subplot(3, 1, 1)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 300)
    ax.bar(ch, hist, color='k', label="rawdata")
    ax.bar(p1_ch, p1_hist, color='r', label="Peak1")
    ax.bar(p2_ch, p2_hist, color='b', label="Peak2")
    ax.legend()

    """
    Background 제거: Background를 1차함수로 가정한다.
    """
    p1_bk_fit = np.poly1d(np.polyfit([p1_ch[0], p1_ch[-1]], [p1_hist[0], p1_hist[-1]], 1))
    p1_hist = p1_hist-p1_bk_fit(p1_ch)
    p2_bk_fit = np.poly1d(np.polyfit([p2_ch[0], p2_ch[-1]], [p2_hist[0], p2_hist[-1]], 1))
    p2_hist = p2_hist-p2_bk_fit(p2_ch)

    ax = plt.subplot(3, 1, 2)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 300)
    ax.bar(p1_ch, p1_hist, color='r', label="Peak1")
    ax.bar(p2_ch, p2_hist, color='b', label="Peak2")
    ax.legend()


    _param1, _ = curve_fit(gaussian, p1_ch, p1_hist, p0=[150, 25, 1])
    _param2, _ = curve_fit(gaussian, p2_ch, p2_hist, p0=[100, 60, 2])

    ax = plt.subplot(3, 1, 3)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 300)
    ax.bar(p1_ch, p1_hist, color='k')
    ax.bar(p2_ch, p2_hist, color='k')
    ax.plot(p1_ch, gaussian(p1_ch, *_param1), "r", label="Peak1", lw=4)
    ax.plot(p2_ch, gaussian(p2_ch, *_param2), "b", label="Peak2", lw=4)
    p1_tx = "$\mu$ {:.2f}\nFWHM {:.2f}".format(_param1[1], _param1[2]*2.3548)
    p2_tx = "$\mu$ {:.2f}\nFWHM {:.2f}".format(_param2[1], _param2[2]*2.3548)
    ax.text(_param1[1], 200, p1_tx)
    ax.text(_param2[1], 200, p2_tx)
    ax.legend()

    plt.savefig("EX5_peak.png", bbox_inches='tight')
