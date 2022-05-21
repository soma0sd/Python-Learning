"""
.. image:: EX4_gaussian.png

`EX4_gaussian.py <EX4_>`_

.. _EX4: https://github.com/soma0sd/Python-Learning/blob/main/W110_Analysis_Data/EX4_gaussian.py

.. literalinclude:: EX4_gaussian.py
   :language: python
   :linenos:
   :lines: 14-

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x = [0.267, 0.533, 0.800, 1.067, 1.333,
    1.600, 1.867, 2.133, 2.400, 2.667,
    2.933, 3.200, 3.467, 3.733, 4.000,
    4.267, 4.533, 4.800, 5.067, 5.333,
    5.600, 5.867, 6.133, 6.400, 6.667,
    6.933, 7.200, 7.467, 7.733, 8.000]

y = [0.143, 0.220, 0.292, 0.315, 0.357,
    0.577, 0.625, 0.661, 0.619, 0.756,
    0.643, 1.000, 0.810, 0.792, 0.714,
    0.726, 0.589, 0.381, 0.369, 0.238,
    0.244, 0.208, 0.089, 0.060, 0.060,
    0.060, 0.030, 0.018, 0.012, 0.000]

x = np.array(x)
y = np.array(y)

def gaussian(x, A, mu, sigma):
    return A*np.exp(-(x-mu)**2/(2*sigma**2))


if __name__ == "__main__":
    _param, _ = curve_fit(gaussian, x, y)
    new_x = np.linspace(0, 8)
    new_y = gaussian(new_x, *_param)

    plt.plot(x, y, '.k')
    plt.plot(new_x, new_y, '--r')
    txt = "A {:.2f}\n$\mu$ {:.2f}\n$\sigma$ {:.2f}".format(*_param)
    plt.text(6, 0.8, txt)
    plt.savefig("EX4_gaussian.png", bbox_inches='tight')
