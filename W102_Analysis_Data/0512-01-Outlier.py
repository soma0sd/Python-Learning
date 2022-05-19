import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

v = 2
a = -0.4

def gen_data(x):
    y = v*x+a*x*x+np.random.rand(len(x))*0.5
    for _ in range(int(len(y)/3)):
        y[np.random.randint(0, len(y))] += (np.random.rand()-0.3)*3
    return y

x = np.arange(0, 4, 0.05)
y = gen_data(x)
fit = np.poly1d(np.polyfit(x, y, 2))
std = np.sqrt(np.mean((y-fit(x))**2))

new_x = []
new_y = []
for _x, _y in zip(x, y):
    if np.abs(_y-fit(_x)) < std:
        new_x.append(_x)
        new_y.append(_y)
new_fit = np.poly1d(np.polyfit(new_x, new_y, 2))

plt.plot(x, y, '.k')
plt.plot(new_x, new_y, '.r')
plt.plot(x, fit(x), '--b', label="before")
plt.plot(x, new_fit(x), '--k', label="after")
plt.plot(x, v*x+a*x*x+0.25, 'r', label='real')
plt.legend()
plt.savefig("0512-01-Outlier.png", bbox_inches='tight')
