"""

.. image:: EX1_euler_method.png

`EX1_euler_method.py <EX1_>`_

.. _EX1: https://github.com/soma0sd/Python-Learning/blob/main/W104_Differential_Equation/EX1_euler_method.py

.. literalinclude:: EX1_euler_method.py
   :language: python
   :linenos:
   :lines: 14-
"""
import numpy as np
import matplotlib.pyplot as plt

dt = 0.1
t = np.arange(0, 10, dt)
x = np.zeros(len(t))

def dxdt(x):
    return np.cos(x)

if __name__ == "__main__":
    for i in range(1, len(t)):
        x[i] = x[i-1]+dxdt(t[i-1])*dt
    plt.plot(t, x, label="Euler", lw=2)
    plt.plot(t, np.sin(t), label="sin(t)", lw=2)
    plt.grid()
    plt.legend()
    plt.savefig("EX1_euler_method.png", bbox_inches='tight')
