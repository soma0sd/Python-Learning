"""

.. image:: EX2_euler_cromer.png

`EX2_euler_cromer.py <EX2_>`_

.. _EX2: https://github.com/soma0sd/Python-Learning/blob/main/W104_Differential_Equation/EX2_euler_cromer.py

.. literalinclude:: EX2_euler_cromer.py
   :language: python
   :linenos:
   :lines: 15-

"""
import numpy as np
import matplotlib.pyplot as plt

dt = 0.1
t = np.arange(0, 10, dt)
xE = np.zeros(len(t))
xC = np.zeros(len(t))

def dxdt(x):
    return np.cos(x)

if __name__ == "__main__":
    for i in range(1, len(t)):
        xE[i] = xE[i-1]+dxdt(t[i-1])*dt
        xC[i] = xC[i-1]+dxdt(t[i])*dt
    plt.plot(t, xE, label="Euler", lw=2)
    plt.plot(t, xC, label="E-C", lw=2)
    plt.plot(t, np.sin(t), label="sin(t)", lw=2)
    plt.grid()
    plt.legend()
    plt.savefig("EX2_euler_cromer.png", bbox_inches='tight')
