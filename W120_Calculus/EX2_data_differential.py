"""
.. image:: EX2_data_differential.png

`EX2_data_differential.py <EX2_>`_

.. _EX2: https://github.com/soma0sd/Python-Learning/blob/main/W120_Calculus/EX2_data_differential.py

.. literalinclude:: EX2_data_differential.py
   :language: python
   :linenos:
   :lines: 14-

"""
import os

os.chdir(os.path.abspath(os.path.dirname(__file__)))

"""데이터의 미분량
소스코드의 실행 디렉토리와 데이터파일의 디렉토리가 일치하도록 조정
"""
import numpy as np
import matplotlib.pyplot as plt

x = []
y = []

with open("data.csv", "r") as f:
    for line in f.readlines():
        _x, _y = [float(i) for i in line.split(" ")]
        x.append(_x)
        y.append(_y)


def g(x, y):
    new_x = []
    new_y = []
    for idx in range(len(x) - 1):
        new_x.append((x[idx] + x[idx + 1]) / 2)
        new_y.append((y[idx + 1] - y[idx]) / (x[idx + 1] - x[idx]))
    return new_x, new_y


if __name__ == "__main__":
    fit = np.poly1d(np.polyfit(x, y, 2))
    fit_x = np.linspace(0, 1)
    fit_y = fit(fit_x)

    # 그래프 1: 원시데이터
    ax1 = plt.subplot(2, 1, 1)
    ax1.set_title("Original function")
    ax1.set_xlim(0, 1)
    ax1.set_ylim(-2, 2)
    ax1.axes.xaxis.set_ticklabels([])
    ax1.plot(fit_x, fit_y, "k--")
    ax1.scatter(x, y)
    ax1.grid(True)

    # 그래프 2: 미분한 데이터
    ax2 = plt.subplot(2, 1, 2)
    ax2.set_title("Differential function")
    ax2.set_xlim(0, 1)
    ax2.set_ylim(-20, 20)
    ax2.plot(fit_x[:-1], np.diff(fit_y) / (fit_x[1] - fit_x[0]), "k--")
    ax2.scatter(*g(x, y))
    ax2.grid(True)

    plt.savefig("EX2_data_differential.png", bbox_inches='tight')
