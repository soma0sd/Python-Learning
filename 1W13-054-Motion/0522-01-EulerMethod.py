import numpy as np
import matplotlib.pyplot as plt
"""
오일러 방법
"""
dt = 0.1
t = np.arange(0, 10, dt)
x = np.zeros(len(t))

def dxdt(x):
    return np.cos(x)

for i in range(1, len(t)):
    x[i] = x[i-1]+dxdt(t[i-1])*dt
plt.plot(t, x, label="Euler", lw=2)
plt.plot(t, np.sin(t), label="sin(t)", lw=2)
plt.grid()
plt.legend()
plt.savefig("0522-01-EulerMethod.png", bbox_inches='tight')
