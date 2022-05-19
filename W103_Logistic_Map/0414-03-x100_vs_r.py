import numpy as np
import matplotlib.pyplot as plt

r   = np.linspace(2, 4, 100)  # r의 범위
x0  = 0.5                     # x의 초기위치
n_i = 100                     # 버리는 계산
n_r = 10                      # 기록할 계산

def logistic(x, r):
    return x*r*(1-x)

plt.rc('font', family='serif')
plt.figure(figsize=(10, 5))
plt.xlabel(r"$r$", fontsize=16)
plt.ylabel(r"$x$", fontsize=16)

for _r in r:
    _xt = x0
    _x = []
    for step in range(n_i):
        # 버리는 계산
        _xt = logistic(_xt, _r)
    for step in range(n_r):
        # 기록할 계산
        _xt = logistic(_xt, _r)
        _x.append(_xt)
    plt.plot([_r]*len(_x), _x, '.r')
"""
pyplot.plot의 약식옵션
'.r': 빨간(r) 점(.)으로 표시한다.
'-b': 파란(b) 실선(-)
':g': 녹색(g) 점선(:)
'--k': 검정(k) 데쉬(--)
"""
plt.savefig("0414-03-x100_vs_r.png", bbox_inches='tight')
