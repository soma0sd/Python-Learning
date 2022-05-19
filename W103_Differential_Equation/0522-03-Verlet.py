import numpy as np
import matplotlib.pyplot as plt
"""
벌렛 방법
"""
x0 = 0; v0 = 1; dt = 0.1; t_max = 20
t = np.arange(0, t_max, dt)
x, v = np.zeros(len(t)), np.zeros(len(t))
x[0] = x0; v[0] = v0;

def a(x):
    return -x

x[1] = x[0] + v[0]*dt + 0.5*a(x[0])*dt*dt
for i in range(2, len(t)):
    x[i] =  2*x[i-1] - x[i-2] + a(x[i-1])*dt*dt

plt.plot(t, x)
plt.savefig("0522-03-Verlet.png", bbox_inches='tight')
