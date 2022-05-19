import numpy as np
import matplotlib.pyplot as plt
"""
오일러-크로머 방법
"""
dt = 0.1
t = np.arange(0, 10, dt)
xE = np.zeros(len(t))
xC = np.zeros(len(t))

def dxdt(x):
    return np.cos(x)

for i in range(1, len(t)):
    xE[i] = xE[i-1]+dxdt(t[i-1])*dt
    xC[i] = xC[i-1]+dxdt(t[i])*dt
plt.plot(t, xE, label="Euler", lw=2)
plt.plot(t, xC, label="E-C", lw=2)
plt.plot(t, np.sin(t), label="sin(t)", lw=2)
plt.grid()
plt.legend()
plt.savefig("0522-02-EulerCromer.png", bbox_inches='tight')
