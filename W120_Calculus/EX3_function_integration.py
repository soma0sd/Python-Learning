"""
.. image:: EX3_function_integration.png

`EX3_function_integration.py <EX3_>`_

.. _EX3: https://github.com/soma0sd/Python-Learning/blob/main/W120_Calculus/EX3_function_integration.py

.. literalinclude:: EX3_function_integration.py
   :language: python
   :linenos:
   :lines: 14-

"""
import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid

h = 0.01
min_x = 1
max_x = 5


def f(x):
    return 3 * x ** 2 + 2 * x + 6


def int_f(func, x_min, x_max, h):
    output = 0
    x = np.arange(x_min, x_max, h)
    for idx in range(len(x) - 1):
        output += (func(x[idx]) + func(x[idx + 1])) * h / 2
    return output


if __name__ == "__main__":
    x = np.linspace(0, 8)
    x_inf = np.arange(min_x, max_x, h)
    y_inf = f(x_inf)
    x_inf = np.concatenate(([x_inf[0]], x_inf, [x_inf[-1]]))
    y_inf = np.concatenate(([0], y_inf, [0]))

    plt.plot(x, f(x))
    plt.fill(x_inf, y_inf, "r", alpha=0.5)
    plt.text(0.1, 55, f"TZ int: {int_f(f, min_x, max_x, h):.3f}")
    plt.text(0.1, 65, f"SCIPY: {trapezoid(f(x_inf), x_inf, h):.3f}")
    plt.grid(True)
    plt.xlim(0, 8)
    plt.ylim(0, 200)
    plt.savefig("EX3_function_integration.png", bbox_inches='tight')
