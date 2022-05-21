"""

데이터 파일을 읽고 그래프로 그리기
====================================

데이터파일인 `data.csv <EX2_DATA_>`_ 은 아래와 같이 공백으로 구분한 두 실수로 작성되어 있습니다.

.. _EX2_DATA: https://github.com/soma0sd/Python-Learning/blob/main/W101_Plotting_Data/data.csv

이 파일의 첫 번째 열은 x값 두 번째 값은 y값이라고 약속했을 때 이 데이터를 그래프로 그리려고 합니다.

.. literalinclude:: data.csv
   :language: text
   :linenos:
   :lines: 1-3

`EX2_plotting_data.py <EX2_>`_

.. _EX2: https://github.com/soma0sd/Python-Learning/blob/main/W101_Plotting_Data/EX2_plotting_data.py

.. literalinclude:: EX2_plotting_data.py
   :language: python
   :linenos:
   :lines: 29-

.. image:: EX2_plotting_data.png

"""
import os
import matplotlib.pyplot as plt

x = []
y = []

data_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data.csv")

with open(data_path, "r") as f:
    for line in f.readlines():
        items = line.split(" ")
        x.append(float(items[0]))
        y.append(float(items[1]))

if __name__ == "__main__":
    plt.scatter(x, y)
    plt.xlim(0, 1)
    plt.ylim(-1.5, 1.5)
    plt.grid(True)
    plt.savefig("EX2_plotting_data.png", bbox_inches="tight")