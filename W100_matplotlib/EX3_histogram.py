"""

히스토그램 그리기
===================

데이터파일인 `hist_data.csv <EX3_DATA_>`_ 는 1904줄의 1차원 배열이며
각 줄마다 측정한 수치가 들어있습니다.

.. literalinclude:: hist_data.csv
   :language: text
   :linenos:
   :lines: 1-3

.. _EX3_DATA: https://github.com/soma0sd/Python-Learning/blob/main/W101_Plotting_Data/hist_data.csv

`EX3_histogram.py <EX3_>`_

.. _EX3: https://github.com/soma0sd/Python-Learning/blob/main/W101_Plotting_Data/EX2_plotting_data.py

.. literalinclude:: EX3_histogram.py
   :language: python
   :linenos:
   :lines: 28-

.. image:: EX3_histogram.png

"""
import os
import numpy as np
import matplotlib.pyplot as plt

data_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "hist_data.csv")

if __name__ == "__main__":
    data = np.loadtxt(data_path)
    n, bins, p = plt.hist(data, bins=40, color="#00796B")
    plt.title("Energy Spectrum")
    plt.xlabel("Energy(keV)")
    plt.ylabel("Intensity #")
    plt.xlim(0, 12)
    plt.grid()
    plt.savefig("EX3_histogram.png", bbox_inches="tight")