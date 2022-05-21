"""
.. image:: EX4_data_integration.png

`EX4_data_integration.py <EX4_>`_

.. _EX4: https://github.com/soma0sd/Python-Learning/blob/main/W120_Calculus/EX4_data_integration.py

.. literalinclude:: EX4_data_integration.py
   :language: python
   :linenos:
   :lines: 14-

"""
import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.integrate import trapezoid

# 데이터 읽어들이기
bins, count = [], []
with open("hist_data.csv", "r") as f:
    for line in f.readlines():
        _b, _c = [float(i) for i in line.split(",")]
        bins.append(_b)
        count.append(_c)

# 모델 함수
def particle(x, a, b, c):
    return a * np.exp(-((x - b) ** 2) / (2 * c ** 2))


def model(x, a_0, a_1, a_2, a_3, a_4, a_5):
    p_a = particle(x, a_0, a_1, a_2)
    p_b = particle(x, a_3, a_4, a_5)
    return p_a + p_b

if __name__ == "__main__":
    popt, pcov = curve_fit(model, bins, count, p0=[100, 1, 0.1, 100, 4, 0.1])
    xdata = np.linspace(0, 4, 100)

    print(popt)

    p_a_value = trapezoid(particle(xdata, *popt[:3]), xdata)
    p_b_value = trapezoid(particle(xdata, *popt[3:]), xdata)

    print(f"Particle A: {p_a_value:.2f}")
    print(f"Particle B: {p_b_value:.2f}")
    print(f"Proportion particle data (A/B): {p_a_value/p_b_value:.3f}")
    print(f"Proportion particle reference (A/B): {6000/10000:.3f}")

    plt.plot(xdata, model(xdata, *popt), "k")
    plt.plot(xdata, particle(xdata, *popt[:3]), "r")
    plt.plot(xdata, particle(xdata, *popt[3:]), "b")
    plt.bar(bins, count, 0.05, color="#AAA")
    plt.savefig("EX4_data_integration.png", bbox_inches='tight')
