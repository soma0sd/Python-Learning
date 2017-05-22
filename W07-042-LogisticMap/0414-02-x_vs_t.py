import numpy as np
import matplotlib.pyplot as plt

r = np.arange(0, 4, 0.5)    # r의 범위
x0 = 0.5                    # x의 초기위치
t = range(100)              # 시행 횟수

def logistic(x, r):
    return x*r*(1-x)

plt.rc('font', family='serif')
plt.figure(figsize=(10, 5))           # 그래프의 크기를 인치단위로 정한다
plt.xlabel(r"$x_{i}$", fontsize=16)
plt.ylabel(r"$x_{i+1}$", fontsize=16)

for _r in r:
    _x = [x0]
    for step in t[:-1]:
        _x.append(logistic(_x[-1], _r))
    plt.plot(t, _x, label="r:{:.1f}".format(_r))

plt.legend()
plt.savefig("0414-02-x_vs_t.png", bbox_inches='tight')
