"""

함수의 그래프 그리기
=====================

$\\\sin(x)$ 함수를 지정한 범위 $[0, 3 \\\pi]$ 의 그래프로 출력합니다.

.. image:: EX1_plotting_function.png

`EX1_plotting_function.py <EX1_>`_

.. _EX1: https://github.com/soma0sd/Python-Learning/blob/main/W101_Plotting_Data/EX1_plotting_function.py

.. literalinclude:: EX1_plotting_function.py
   :language: python
   :linenos:
   :lines: 28-

np.linspace(0, 3)은 0부터 3사이 숫자를 일정 간격으로 50개(기본값) 만들어
numpy의 array 자료형으로 출력합니다. 출력 결과는 [0.00, 0.06, 0.12,..] 형태입니다.

np.linspace(xmin, xmax, ndata)는 xmin 부터 xmax 사이 숫자를 일정 간격으로
ndata 개수만큼 생성하여 numpy 의 array 자료형으로 출력합니다.

plt.grid(True)를 사용하여 그래프에 격자 보조선을 넣을 수 있습니다.

"""
import numpy as np
import matplotlib.pyplot as plt


def func(x):
    """$f(x)$ 함수"""
    return np.sin(x)

if __name__ == "__main__":
    x = np.linspace(0, np.pi * 3)
    plt.plot(x, func(x))
    plt.grid(True)
    plt.savefig("EX1_plotting_function.png")
